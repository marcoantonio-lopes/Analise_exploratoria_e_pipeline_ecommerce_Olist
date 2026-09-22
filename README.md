# Análise de e-commerce — Olist

Projeto de análise exploratória sobre avaliações de pedidos, atrasos, produtos, regiões, vendedores e recompra. O objetivo é identificar padrões que orientem investigações sobre a experiência de compra, sem atribuir causalidade às diferenças observadas.

## Resultados e análises

As interpretações e limitações estão em [docs/conclusoes.md](docs/conclusoes.md). Os notebooks de análise estão em `notebooks/`, com gráficos exportados para `outputs/graficos/` e tabelas para `outputs/tabelas/parquet/` e `outputs/tabelas/csv/`. O pipeline prepara os arquivos para o Power BI; a construção do relatório é uma etapa separada.

## Estrutura

```text
src/                         # Leitura, preparação e execução dos notebooks
notebooks/                   # Notebooks originais de preparação e análise
data/raw/                    # CSVs de entrada
data/processed/              # Bases Parquet geradas
outputs/notebooks/           # Cópias executadas das análises
outputs/graficos/            # Imagens exportadas pelos notebooks
outputs/tabelas/parquet/     # Resultados para reutilização nas análises
outputs/tabelas/csv/         # Os mesmos resultados para importar no Power BI
docs/conclusoes.md           # Conclusões e limitações
executar_pipeline.py         # Comando de execução do fluxo completo
requirements.txt             # Versões das dependências diretas
```

`backups/` e `xnotebook/` são materiais históricos e não entram no pipeline. A pasta `data/processed_validacao/`, se existir, é resultado da conferência inicial e não é mais alimentada pelo fluxo.

## Dados necessários

O projeto utiliza tabelas do conjunto de e-commerce da Olist. Disponibilize os seis CSVs abaixo em `data/raw/`, mantendo os nomes e a estrutura das colunas. O pipeline não baixa os dados automaticamente.

- `olist_order_reviews_dataset.csv`
- `olist_customers_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_orders_dataset.csv`
- `olist_products_dataset.csv`
- `olist_sellers_dataset.csv`

Os arquivos originais são somente lidos. Os resultados refletem os CSVs fornecidos; novos dados podem mudar as contagens e os gráficos.

## Instalação no Windows (PowerShell)

Ambiente verificado: Python 3.12. Abra o terminal na raiz do projeto e execute:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --user --name ecommerce --display-name "Python (ecommerce)"
```

Não é necessário ativar o ambiente para usar esses comandos. Se `.venv` já existir, pule sua criação. O arquivo de dependências fixa as bibliotecas diretas, incluindo `statsmodels` para o teste estatístico do notebook 07; as dependências transitivas são resolvidas pelo pip.

O registro do kernel é necessário para o executor de notebooks. Se mover o projeto, recrie o ambiente virtual no novo local e registre novamente o kernel `ecommerce`, pois seu registro aponta para o executável Python do ambiente.

## Executar o pipeline

```powershell
.\.venv\Scripts\python.exe executar_pipeline.py
```

O comando:

1. Carrega os seis CSVs.
2. Trata avaliações, relaciona pedidos e clientes e prepara os itens.
3. Resume os itens por pedido e constrói a base analítica.
4. Executa as verificações de chaves, contagens e regras presentes nas funções.
5. Salva os dois Parquets em `data/processed/` e confere a leitura contra os resultados em memória.
6. Executa os notebooks `02_atrasos` a `10_recompra_atraso_avaliacao`, em sequência e em kernels novos.
7. Em cada análise, monta os gráficos e depois executa uma única seção final de exportações: tabelas em Parquet/CSV e figuras em PNG. Os gráficos são capturados em memória antes de fechar as figuras e gravados no final.
8. Salva cópias executadas, com tabelas e gráficos visíveis, em `outputs/notebooks/`.

A mensagem `Pipeline concluído: bases, notebooks, tabelas e gráficos atualizados.` indica que todas as etapas terminaram. Arquivos de saída com os mesmos nomes são substituídos. Os notebooks originais não são sobrescritos pelo executor. Se uma etapa falhar, o processo interrompe e mostra o erro; saídas das etapas anteriores permanecem gravadas (não há reversão automática).

### Tabelas de vendedores para Power BI

O notebook `05_vendedores.ipynb`, já incluído no pipeline, exporta automaticamente em `outputs/tabelas/parquet/`, com cópias CSV em `outputs/tabelas/csv/`:

- `05_ranking_vendedores.parquet`: ranking completo por taxa de avaliações ruins.
- `05_ranking_vendedores_atraso.parquet`: ranking completo por taxa de atraso.

Cada arquivo contém uma linha por vendedor elegível (mínimo de 10 pedidos entregues e avaliados), incluindo posição, estado, contagens, nota média e proporções numéricas de 0 a 1. A exportação preserva as regras e a ordenação do notebook e confere a leitura dos arquivos contra os DataFrames em memória. Não se limita aos 20 vendedores exibidos no notebook.

No Power BI, importe os CSVs pelo conector Texto/CSV (separador ponto e vírgula e localidade Português do Brasil para números) e formate as colunas `pct_` como porcentagem. Os rankings são alternativas de ordenação do mesmo conjunto de vendedores; não concatene os dois arquivos para calcular totais. A posição é global e não é recalculada ao filtrar. As tabelas são agregadas por vendedor, sem detalhamento mensal. Pedidos compartilhados aparecem para cada vendedor envolvido, portanto somar suas contagens não produz o total de pedidos únicos.

### Outras tabelas de resultados para Power BI

As seções finais de exportação geram os arquivos abaixo em `outputs/tabelas/`. Os rankings originais são completos; os quatro resultados do notebook 08 preservam explicitamente suas seleções de top 10:

| Notebook | Arquivos em ambos os formatos |
| --- | --- |
| `02_atrasos` | `02_comparacao_atraso`, `02_atrasos_por_faixa` |
| `03_produtos` | `03_ranking_produtos`, `03_ranking_categorias`, `03_faixas_preco`, `03_faixas_peso`, `03_faixas_volume` |
| `04_regioes` | `04_ranking_estados`, `04_ranking_regioes` |
| `05_vendedores` | `05_ranking_vendedores`, `05_ranking_vendedores_atraso`, `05_ranking_estados_vendedores` |
| `06_taxa_recompra` | `06_comparacao_taxas_recompra`, `06_resumo_tempo_recompra` |
| `07_inferencia_recompra` | `07_teste_recompra`, `07_grupos_teste_recompra` |
| `08_produtos_categorias_atraso_avaliacao` | `08_produtos_atraso_avaliacao`, `08_categorias_atraso_avaliacao`, `08_produtos_maiores_atrasos`, `08_categorias_maiores_atrasos` |
| `09_regioes_estados_atraso_avaliacao` | `09_estados_atraso_avaliacao`, `09_regioes_atraso_avaliacao` |
| `10_recompra_atraso_avaliacao` | `10_atraso_por_avaliacao`, `10_recompra_por_atraso`, `10_recompra_avaliacao_atraso` |

Todos os outputs de tabelas e gráficos usam o prefixo de dois dígitos do notebook de origem (`02_` a `10_`). As bases internas em `data/processed/` mantêm os nomes atuais. Se já houver consultas no Power BI, atualize seus caminhos para os novos nomes.

Todos os nomes acima recebem a extensão `.parquet` na subpasta `parquet/` e `.csv` na subpasta `csv/`. As pastas são criadas na execução. Os dois formatos são exportados a partir do mesmo DataFrame, sem índice. Os CSVs usam separador `;`, vírgula decimal e codificação UTF-8 com BOM (`utf-8-sig`). As novas exportações conferem a leitura dos Parquets contra os resultados em memória. A coluna `faixa_atraso`, originalmente no índice, é preservada como coluna no arquivo. As taxas permanecem numéricas, sem a formatação visual do notebook.

O notebook `07_inferencia_recompra` lê `outputs/tabelas/parquet/06_comparacao_taxas_recompra.parquet`: execute primeiro o notebook 06 ou o pipeline para gerar o arquivo no novo caminho. Arquivos antigos diretamente em `outputs/tabelas/` não são apagados nem atualizados pelas novas exportações. As bases de `data/processed/` mantêm seus caminhos.

Essas tabelas são resumos dos recortes já definidos nas análises: filtros no Power BI não recuperam detalhes ausentes nem recalculam posições globais, medianas ou percentis. Na recompra, os grupos `Geral` e `Qualquer avaliação` se sobrepõem aos demais e não devem ser somados a eles.

`07_teste_recompra` contém uma linha com grupos, contagens, taxas, diferença em pontos percentuais, intervalo de confiança, estatística Z, p-valor, nível de significância e decisão do teste. O resultado representa a comparação geral Boa menos Ruim; filtros de atraso, estado ou período no Power BI não recalculam esse teste. Significância estatística não demonstra causalidade.

### Gráficos e dependências entre notebooks

- **07:** `07_teste_recompra.png`, com as taxas dos grupos e o intervalo de confiança da diferença. Depende da tabela exportada pelo 06.
- **08:** oito PNGs com prefixo `08_`, comparando avaliações ruins e composição das entregas para cada um dos quatro top 10. Depende das bases detalhadas e dos rankings exportados pelo 03.
- **09:** quatro PNGs com prefixo `09_`, mostrando avaliações ruins e composição das entregas por estado e região.
- **10:** três PNGs com prefixo `10_`, mostrando atrasos por avaliação, recompra por atraso e recompra por avaliação e atraso.

Os gráficos anteriores continuam em `outputs/graficos/`. Nos notebooks 02–10 há somente três blocos Markdown breves: pergunta/objetivo, gráficos e exportações. O 01 não monta gráficos; o notebook de teste apenas valida as bases. Os originais ficam sem resultados antigos; execute-os manualmente ou consulte as cópias de `outputs/notebooks/` para visualizar resultados atualizados.

## Executar uma análise com os Parquets existentes

```powershell
.\.venv\Scripts\python.exe -c "from src.executar_notebooks import executar_notebook; executar_notebook('02_atrasos.ipynb')"
```

Para execução manual no VS Code, selecione o kernel `Python (ecommerce)` e execute as células do início ao fim. Os notebooks localizam a raiz a partir da pasta de trabalho e de seus ancestrais: abra-os dentro do projeto. Isso também funciona nas cópias em `outputs/notebooks/`.

O notebook `01_preparacao_base_analitica.ipynb` permanece como referência da preparação e não é executado pelo pipeline, que já realiza essa etapa pelas funções de `src/`. Se executado manualmente, ele grava os Parquets em `data/processed/` na seção final. `teste.ipynb` é uma conferência manual das chaves e não entra na lista de análises.

## Regras principais

- A base analítica tem uma linha por pedido; a base de itens usa a chave `order_id` + `order_item_id`.
- Avaliações ruins: notas 1 e 2; neutras: 3; boas: 4 e 5.
- As avaliações seguem a ordenação e a deduplicação por pedido e por `review_id` adotadas na preparação.
- Pedidos sem itens ou sem avaliação permanecem na base analítica; cada análise define seu recorte.
- O atraso segue a diferença entre entrega e previsão com `.dt.days > 0`. Datas ausentes mantêm o indicador de atraso ausente.
- Produtos: pedidos entregues, avaliados e com um único item. Vendedores: relações pedido–vendedor, incluindo pedidos compartilhados.
- Recompra: primeira compra entregue observada como referência, mínimo de 90 dias observáveis após a entrega e novo pedido posterior à compra de referência, até o fim da base, com qualquer status. Não é uma taxa de recompra limitada a 90 dias.

As conclusões escritas em Markdown não são recalculadas. Revise-as quando os dados ou as regras mudarem. O pipeline automatiza cálculos e gráficos, não a interpretação dos resultados.

## Solução de problemas

- **Biblioteca não encontrada:** instale `requirements.txt` com o Python da `.venv`.
- **Kernel ecommerce não encontrado:** execute o comando de registro do kernel acima.
- **CSV não encontrado:** confira os seis arquivos em `data/raw/`.
- **Erro em uma célula:** examine o traceback; o executor interrompe no primeiro erro e usa limite de 600 segundos por célula.
- **Caminho do projeto não encontrado:** execute o notebook a partir da raiz ou de uma subpasta do projeto.

Execute sem a opção `-O` do Python, pois as validações atuais usam `assert`.
