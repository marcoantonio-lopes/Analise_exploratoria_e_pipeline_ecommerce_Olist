# Proposta de modelagem — e-commerce

Avaliação dos arquivos locais em 28/09/2026. Este documento é uma proposta: não altera o PBIX, as bases ou os notebooks. Os resumos disponíveis em disco não são necessariamente todos os que estão importados atualmente.

## Decisão inicial

Preservar os resumos do pandas e conectá-los a dimensões próprias, formando várias estrelas pequenas com dimensões compartilhadas. Não ligar resumos diretamente entre si. Não usar as bases detalhadas como pontes entre resumos. Adicionar fatos detalhadas apenas para páginas que precisem recalcular indicadores por data ou outras combinações ausentes dos resumos.

## Evidências verificadas

- Base de pedidos: 99.441 linhas; order_id e customer_id únicos; 96.096 customer_unique_id distintos.
- Itens: 112.650 linhas; (order_id, order_item_id) único; nenhum item com order_id ausente na base de pedidos.
- Produtos nos itens: 32.951 IDs, nenhum nulo; sem conflitos por ID em categoria, peso, comprimento, altura e largura.
- Vendedores nos itens: 3.095 IDs, nenhum nulo; sem conflitos por ID em cidade e estado.
- Todos os IDs dos resumos de produtos/vendedores conferidos existem na base de itens; categorias dos resumos também correspondem às categorias da base, considerando sem_categoria.
- 122 customer_unique_id têm mais de uma combinação de cidade/estado. Não escolher uma localização arbitrária para uma dimensão de cliente único.
- Rankings de vendedores: 1.236 vendedores elegíveis em cada arquivo. Ranking por avaliação e ranking por atraso não devem ser concatenados para totais.
- Resumos de produtos do notebook 08: seleções fixas de 10 produtos; um arquivo possui 19 combinações produto/situação e outro 20. Ausência de combinação não deve ser automaticamente interpretada como erro.
- Resumos por categoria do notebook 08: 20 linhas em cada arquivo, categoria × situação.
- Estados/situação: 54 linhas; regiões/situação: 10. Chaves compostas sem duplicidades.
- Análises de produtos dos notebooks 03 e 08 usam pedidos entregues, avaliados e com exatamente um item. Preservar esse recorte em futuras medidas.
- CSVs dos resumos usam ponto e vírgula e vírgula decimal; CSVs detalhados encontrados usam vírgula como separador. Importar com configurações apropriadas, sem uma configuração única para todos.

## Dimensões propostas e conexões

Cada dimensão deve ter chave única, sem nulos, e os relacionamentos devem filtrar da dimensão para o resumo. Preferir cardinalidade 1:* mesmo quando o resumo atualmente tem apenas uma linha por chave; não aceitar automaticamente 1:1 com filtro bidirecional.

| Dimensão (nova) | Chave e origem | Tabelas de destino e coluna |
|---|---|---|
| DimProduto | product_id; extrair IDs e atributos consistentes de itens_pedidos | 03_ranking_produtos; 08_produtos_atraso_avaliacao; 08_produtos_maiores_atrasos — product_id |
| DimCategoriaAnalise | categoria; união distinta de categoria_analise/categoria dos resumos | 03_ranking_categorias[categoria_analise]; 08_categorias_atraso_avaliacao[categoria]; 08_categorias_maiores_atrasos[categoria] |
| DimVendedor | seller_id; extrair de itens_pedidos com cidade/estado | 05_ranking_vendedores[seller_id]; 05_ranking_vendedores_atraso[seller_id] |
| DimUFVendedor | UF; união dos estados de vendedores e resumos | 05_ranking_estados_vendedores[seller_state]; 05_ranking_vendedores[seller_state]; 05_ranking_vendedores_atraso[seller_state] |
| DimUFCliente | UF; união distinta dos estados de clientes; pode incluir nome e região | 04_ranking_estados[customer_state]; 09_estados_atraso_avaliacao[customer_state] |
| DimRegiaoAnalise | regiao_chave; norte, nordeste, centro_oeste, sudeste, sul | 04_ranking_regioes[regiao_chave]; 09_regioes_atraso_avaliacao[regiao_chave] |
| DimSituacaoEntrega | situacao_chave; atrasado, no_prazo e sem_informacao quando existir | 02_comparacao_atraso; os quatro resumos 08_; os dois resumos 09_; 10_recompra_por_atraso; 10_recompra_avaliacao_atraso — criar situacao_chave a partir da coluna de situação correspondente |
| DimGrupoRecompra | grupo; união dos rótulos dos resumos 06/07 | 06_comparacao_taxas_recompra[grupo]; 06_resumo_tempo_recompra[grupo]; 07_grupos_teste_recompra[grupo] |
| DimGrupoAvaliacaoReferencia | grupo_avaliacao; Boa, Neutra, Ruim, Sem avaliação | 10_atraso_por_avaliacao[grupo_avaliacao]; 10_recompra_avaliacao_atraso[grupo_avaliacao] |

As dimensões de UF de cliente e vendedor devem ser separadas: são papéis geográficos distintos. Não criar, ao mesmo tempo, caminhos por DimUFVendedor → DimVendedor → resumo e por DimUFVendedor → resumo. Nesta proposta, os dois filtros chegam diretamente ao resumo, sem ligação entre as dimensões.

Categoria pode continuar como atributo de DimProduto para filtrar os resumos por produto. DimCategoriaAnalise atende aos resumos por categoria. Inicialmente não ligar as duas dimensões. Se for necessário um único filtro de categoria para ambos os grupos, preparar categoria_chave também nos resumos por produto e ligar a dimensão diretamente a eles, após validar a correspondência; não criar um segundo caminho pela DimProduto.

Região no resumo estadual pode vir de DimUFCliente; DimRegiaoAnalise atende aos resumos já agregados por região. Um filtro de estado não pode decompor um total regional. Se precisar de um único filtro regional entre as duas análises, preparar região nos resumos estaduais e conectar uma dimensão regional comum por um único caminho.

## Padronizações antes dos relacionamentos

- Preservar colunas originais; acrescentar chaves de integração nas cópias para o Power BI.
- Mapear atrasado e Atrasado para atrasado; no_prazo e No prazo para no_prazo; Sem informação para sem_informacao. Não classificar nulos como No prazo.
- Mapear Centro-Oeste e centro_oeste para centro_oeste; padronizar as outras regiões.
- Categorias: conservar os códigos existentes e sem_categoria para ausência, de acordo com os notebooks. Rótulos de exibição podem ser separados das chaves.
- IDs como texto; não converter códigos identificadores para números.
- O grupo de recompra e a avaliação do pedido de referência são papéis diferentes. Não unificar apenas porque compartilham rótulos Boa/Ruim.

## Tabelas que ficam independentes inicialmente

| Tabela | Motivo |
|---|---|
| 02_atrasos_por_faixa | Resumo por faixa de dias de atraso; não contém produto, estado ou data. Usar faixa_atraso no próprio visual. |
| 03_faixas_peso | Resumo por faixa de peso; não responde a filtros de produto/data sem base mais detalhada. |
| 03_faixas_preco | Resumo por faixa de preço; mesmo limite. |
| 03_faixas_volume | Resumo por faixa de volume; mesmo limite. |
| 07_teste_recompra | Uma comparação estatística fixa entre dois grupos. Não relacionar grupo_1 ou grupo_2 para sugerir recálculo do teste. |

Dimensões de faixas só são necessárias se os mesmos intervalos forem compartilhados com outras fatos. Não conectar as três colunas chamadas faixa entre si: peso, preço e volume medem coisas distintas.

## Limites dos resumos

- Não recebem relacionamento com calendário: não contêm a granularidade temporal necessária.
- Posição de ranking, elegibilidade, top 10/top 100 e referências globais continuam sendo as calculadas no Python.
- Filtro de situação afeta apenas tabelas que preservam situação. Não recalcula um ranking geral sem essa coluna.
- Médias, percentuais, medianas e valores repetidos por grupo não podem ser somados indiscriminadamente. Sua revisão é a etapa posterior à modelagem.
- Geral e Qualquer avaliação, nos resumos de recompra, sobrepõem-se a outros grupos. Não somar todas as linhas para um total.
- Contagens de pedidos por vendedor podem repetir pedidos compartilhados. Somá-las não produz pedidos únicos.
- Relações compartilham rótulos de filtro, não tornam universos de análise diferentes automaticamente comparáveis. Exibir recortes nas páginas.

## Expansão futura com dados detalhados

- FatoPedidos: derivar da base_analitica_pedidos, mantendo uma linha por order_id e os tratamentos já realizados. DimDataCompra → data_compra (somente data); DimUFCliente → customer_state; outras dimensões segundo necessidade.
- FatoItens: derivar de itens_pedidos, mantendo (order_id, order_item_id). DimProduto → product_id; DimVendedor → seller_id. Acrescentar somente as chaves de cliente/local/data necessárias via merge muitos-para-um com pedidos, sem replicar valores totais do pedido como valores aditivos do item.
- A dimensão por customer_unique_id pode guardar a identidade, mas a localização deve representar a compra ou seguir uma regra histórica explícita, dadas as 122 identidades com mudança de localização.
- Não usar filtro bidirecional para forçar produto/vendedor a filtrar pedidos. Planejar medidas de pedidos distintos ou fatos de análise no recorte adequado.
- Para análises 03/08 dinâmicas, pode-se exportar o conjunto intermediário de pedidos de um item já preparado nesses notebooks; isso preserva o tratamento e evita reimplementar toda a lógica no DAX.
- Recompra dinâmica exige preservar seleção do pedido de referência, janela observável e definição de recompra. Não basta contar clientes com mais de um pedido.

## Ordem de implantação e validação

1. Começar por vendedores: DimVendedor e os dois rankings por seller_id. Usar o identificador da dimensão como filtro.
2. Acrescentar DimUFVendedor e as três conexões por seller_state, sem ligá-la à DimVendedor nesta proposta.
3. Preparar produtos, categorias e geografia de clientes.
4. Padronizar situação de entrega e regiões antes de suas ligações.
5. Separar os grupos de recompra dos grupos de avaliação do pedido de referência.
6. Validar dimensões únicas, chaves órfãs, tipos e um único caminho de filtro.
7. Comparar linhas/indicadores de um vendedor, produto e estado conhecidos com os CSVs; confirmar que limpar filtros restaura os resultados de referência.
8. Manter páginas ou visuais de recorte fixo claramente identificados. Validar que filtros sem suporte não sugerem que esses resultados foram recalculados.

Nenhuma relação deve usar posicao, percentuais, quantidades, médias ou valores monetários como chave.
