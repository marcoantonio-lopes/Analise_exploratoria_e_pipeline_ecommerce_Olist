# Revisão do relatório Pbi.pbix

Data: 19/10/2026. Avaliação somente de leitura: definições das cinco páginas no PBIX salvo, medidas e relacionamentos do modelo aberto, consultas DAX de conferência e imagens compartilhadas. Nenhuma medida, relacionamento ou visual foi alterado. A configuração de interações foi inspecionada e sua propagação foi testada por consultas; não foi executado um teste manual de todos os cliques na interface.

## Parecer

A distribuição e a identidade visual são consistentes. A estrutura de indicadores no topo, análise principal à esquerda e complementos à direita funciona bem. Não é necessário acrescentar gráficos. Antes da entrega final, corrigir o cartão de recompra, os tooltips herdados, a interação por estado e o rodapé de entregas. Há também diferenças de população que precisam ser explicitadas.

## Valores conferidos, sem seleção

| Página | Resultado verificado |
|---|---|
| Produtos e Categoria | 86.302 pedidos; 9.944 avaliações ruins; 11,52% |
| Entregas e Atrasos | 95.930 entregas analisadas; 6.492 atrasadas; 6,77% de atraso; 12.565 avaliações ruins; 13,10% de avaliações ruins |
| Vendedores | 1.236 vendedores; 91.327 participações pedido–vendedor elegíveis; 13,64% de avaliações ruins; 6,69% de atraso |
| Análise Geográfica | 95.930 pedidos; 13,10% de avaliações ruins; 6,77% de atraso |
| Recompra, apenas Boa/Neutra/Ruim | 82.333 clientes; 2.378 que recompraram; taxa correta 2,89% |
| Recompra, grupo Geral | 82.502 clientes; 2.534 que recompraram; taxa 3,07% |

Os totais diferentes entre páginas não são, por si só, erro: produtos têm restrições de itens e mínimos de volume; vendedores têm mínimo de pedidos e atribuição por participante. Não apresentar a soma por vendedor como quantidade de pedidos únicos de toda a base.

## Correções prioritárias

### 1. Recompra: cartão soma percentuais

No arquivo salvo, o cartão de taxa usa SOMA de `06_comparacao_taxas_recompra[taxa_recompra]`, limitado a Boa, Neutra e Ruim. Isso resulta em aproximadamente 8,07%, quando a taxa conjunta correta é 2.378 / 82.333 = 2,89%. A seleção de um único grupo pode mascarar o problema.

Substituir o campo do cartão por uma medida de razão entre somas, mantendo o filtro que permite somente Boa/Neutra/Ruim:

```dax
Taxa de recompra - grupos avaliados =
DIVIDE(
    SUM('06_comparacao_taxas_recompra'[clientes_que_recompraram]),
    SUM('06_comparacao_taxas_recompra'[total_clientes])
)
```

Formatar como percentual. Não remover indiscriminadamente os filtros dos grupos: essa tabela também contém linhas agregadas sobrepostas, como Geral, que não podem ser somadas aos grupos individuais.

### 2. Tooltips de três gráficos usam tabelas de outra análise

| Página e gráfico | Problema | Campo adequado |
|---|---|---|
| Entregas: distribuição de avaliações por situação | Quantidades de `03_ranking_categorias` | `02_comparacao_atraso[total_pedidos]` e `[reviews_ruins]` |
| Entregas: avaliações ruins por faixa de atraso | Quantidades de `03_ranking_produtos` | `02_atrasos_por_faixa[quantidade]` e `[reviews_ruins]` |
| Vendedores: ranking de atraso | Um tooltip de quantidade usa `03_ranking_produtos` | `05_ranking_vendedores[quantidade_pedidos]`; manter também pedidos com prazo conhecido |

As barras podem estar corretas e, ainda assim, o tooltip mostrar valores sem relação com a barra. Conferir todos os campos após duplicar uma página.

### 3. Geografia: seleção de estado não alcança a taxa de atraso

O ranking usa `04_ranking_estados[customer_state]`. Com os relacionamentos atuais, esse filtro não chega à tabela `09_estados_atraso_avaliacao`, usada pela taxa de atraso.

Teste: filtrando SP, RJ ou MG pela coluna da tabela de ranking, a taxa permanece em 6,77%. Pela dimensão `DimUFCliente[customer_state]`, os resultados são SP 4,49%, RJ 12,08% e MG 4,57%.

Usar a coluna da dimensão no eixo do ranking. Isso permite filtrar as duas tabelas por estado. Gráficos já agregados por região não necessariamente responderão a um estado: decidir se permanecem como comparação regional, desativando a interação, ou recalcular a análise regional a partir do detalhe por estado. Não ativar relacionamentos bidirecionais indiscriminadamente.

### 4. Entregas: rodapé descreve uma restrição que não existe nessa análise

O rodapé salvo diz “com um único item”. A análise de entregas usa pedidos entregues, avaliados e com informação de atraso conhecida, sem essa restrição de item único.

Texto sugerido: **Pedidos entregues, avaliados e com informação de prazo conhecida. Avaliações ruins: notas 1 e 2. Evolução agrupada pelo mês de entrega.**

### 5. Recompra: população dos cartões difere da comparação por atraso

Os cartões e o gráfico Boa/Neutra/Ruim usam 82.333 clientes avaliados. A tabela `10_recompra_por_atraso` inclui 82.502 clientes, incluindo 169 sem avaliação. Portanto, o gráfico por situação de entrega não representa exatamente a mesma população dos cartões.

Escolher uma regra comum, se os dados disponíveis permitirem, ou explicitar a diferença. Não é possível eliminar o grupo sem avaliação desse agregado por atraso apenas relacionando tabelas: é preciso ter esse recorte na origem ou detalhe por cliente.

O grupo sem avaliação contém 156 clientes que recompraram entre 169 (92,31%). A taxa muito diferente merece uma investigação da regra de inclusão na origem; não é prova automática de erro, mas altera o total geral.

## Interações e filtros a limpar

- Entregas, distribuição: remover o Top 10 herdado de categorias de produtos.
- Entregas, faixas: remover o Top 3 herdado de produtos.
- Geografia, gráfico por região: remover o Top 3 herdado de produtos.
- Recompra, gráfico por atraso: remover o Top 3 herdado de produtos.
- Recompra, mediana: revisar o filtro herdado de `10_atraso_por_avaliacao`; manter o filtro pertinente à tabela de tempo.

Esses filtros não demonstram, isoladamente, erro nos valores atuais; são configurações alheias ao objetivo do visual e podem confundir manutenção e interações.

Na recompra, selecionar uma barra de `06_comparacao_taxas_recompra[grupo]` filtra os cartões da mesma tabela, mas não garante que a mediana de outra tabela responda. Para a seleção por avaliação alcançar taxa e tempo, usar `DimGrupoRecompra` nos eixos compatíveis. Isso não cria o cruzamento avaliação × situação de entrega, ausente no agregado por atraso.

O mesmo cuidado vale para selecionar uma situação em `02_comparacao_atraso`: não pressupor que isso filtre automaticamente a base temporal ou a tabela de faixas. Manter análises contextuais fixas pode ser apropriado, desde que a interface não sugira que estão filtradas.

## Gráfico temporal: conta correta, leitura que exige contexto

| Mês de entrega | Entregas | Atrasadas | Taxa |
|---|---:|---:|---:|
| Julho/2018 | 5.820 | 78 | 1,34% |
| Agosto/2018 | 8.293 | 553 | 6,67% |
| Setembro/2018 | 56 | 56 | 100% |
| Outubro/2018 | 3 | 3 | 100% |

O pico final é real nesse recorte, mas tem volume muito menor. Não interpretá-lo como 100% dos pedidos comprados naquele mês: o eixo é o mês da entrega. A proximidade do fim da base também limita a comparação.

Manter volume e atrasadas no tooltip; acrescentar observação sobre os meses finais. Preferir linha sem suavização, pois os pontos são taxas mensais observadas. O arquivo tem suavização ativa. Há ainda um título oculto do eixo Y “% de avaliações ruins”: atualizar para “Taxa de atraso (%)” para evitar erro se for reativado.

## Títulos, subtítulos e rótulos

| Item | Sugestão |
|---|---|
| Produtos: “Produtos por taxa de avaliação” | “Produtos com maior taxa de avaliações ruins” |
| Entregas: distribuição | “Distribuição das avaliações por situação de entrega” |
| Entregas: faixas | “Taxa de avaliações ruins por faixa de atraso” |
| Vendedores: dispersão | “Taxa de atraso × taxa de avaliações ruins” |
| Geografia: barras agrupadas | “Taxa de avaliações ruins por região e situação de entrega” |
| Recompra: clientes analisados, mantendo o recorte atual | “Clientes avaliados analisados” ou explicar o recorte no rodapé |
| Recompra: tooltip “Total de recompras” | “Clientes que recompraram” |

Os subtítulos com “Explore…” são coerentes com o propósito das páginas. Padronizar capitalização e usar “avaliações ruins” em todas as páginas em vez de alternar com “negativas”. Informar Top 10 e Top 5 nos rankings de vendedores quando esses limites forem mantidos. No ranking de produtos, não é necessário prometer três produtos quando o filtro pode retornar menos.

Diferenças para a taxa geral, quando exibidas no tooltip geográfico, devem ser identificadas em **pontos percentuais**, não como variação percentual relativa.

## Rodapés e interpretação

- **Produtos:** regra de item único e mínimos de 30 pedidos por categoria e 5 por produto é pertinente. Manter.
- **Entregas:** remover item único, conforme correção acima.
- **Vendedores:** manter mínimo de 10 pedidos e atribuição da avaliação do pedido a cada vendedor participante. Isso evita confundir soma de participações com pedidos únicos.
- **Geografia:** manter localização do cliente, elegibilidade e cálculo separado por situação. Não confundir UF do cliente com UF do vendedor.
- **Recompra:** manter a explicação de pelo menos 90 dias observáveis, recompra até o fim da base e contagem a partir da compra de referência. Não chamar de “taxa de recompra em 90 dias”. A regra admite novos pedidos antes da entrega de referência; portanto, não permite concluir que a avaliação ou o atraso causou a recompra posterior. Explicitar também o recorte sem avaliação usado em cada visual.

A mediana de tempo está coerente no nível de uma linha por grupo. A agregação atual por SOMA funciona nesse nível, mas não deve ser usada para calcular uma mediana global ou combinar grupos. É preciso recalcular no detalhe para isso.

## Visualização

Manter layout e cores: há hierarquia e consistência entre páginas, sem a densidade excessiva do exemplo inicial. Os principais ajustes visuais são pequenos:

1. Aumentar legibilidade dos rodapés, especialmente recompra; aproveitar maior largura disponível.
2. IDs completos de vendedores e produtos são difíceis de ler. Usar um identificador curto e único para exibição, preservando ID completo no tooltip e nos relacionamentos.
3. Padronizar casas decimais das taxas, unidades e títulos dos eixos.
4. Preservar cores com significado consistente dentro de cada comparação e uma legenda explícita; a cor laranja identifica a medida principal em várias páginas, não uma categoria universal.
5. Evitar adicionar outro gráfico apenas para preencher espaço. Reservar espaço para o menu lateral antes do ajuste final, caso ele seja incluído.

## Verificação após os ajustes

- Recompra: Todos → 82.333 / 2.378 / 2,89%; Boa → 64.233 / 1.920 / 2,99%; Neutra → 6.972 / 181 / 2,60%; Ruim → 11.128 / 277 / 2,49%, mantendo o recorte avaliado.
- Geografia: SP → taxa de atraso 4,49%; RJ → 12,08%, se o cartão deve responder ao estado.
- Entregas: total fixo 95.930; seleção de atrasados 6.492 nos cartões que devem responder.
- Passar o mouse em barras distintas e confirmar que os volumes pertencem à tabela e ao grupo exibidos.
- Limpar seleções, salvar e reabrir o PBIX para confirmar o estado inicial da apresentação.

As consultas validam a coerência com os dados carregados e com as regras inspecionadas; não constituem reconciliação independente de todas as linhas da fonte bruta.
