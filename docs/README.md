# Documentação e manutenção

- [Conclusões](conclusoes.md): interpretações e limitações estatísticas; revisão manual.
- [Operação do Power BI](../power_bi/README.md): integração local com Power Automate.
- [Registro de duplicatas removidas](limpeza_duplicatas.json): arquivo removido,
  cópia preservada e SHA-256 de cada conteúdo.

## O que é essencial

- `executar_pipeline.py`, `src/`, `requirements.txt` e `.venv/`.
- Seis entradas em `data/raw/` e notebooks de análise 02 a 10 em `notebooks/`.
- Kernel Jupyter `ecommerce`, registrado conforme o README principal.
- Saídas em `data/processed/` e `outputs/`, consumidas por notebooks e Power BI.
- PBIX ativo e fluxo configurado no Power Automate para a etapa visual.

O notebook 01 é referência executável da preparação; `teste.ipynb` é uma
validação manual. Não entram no fluxo automático, mas não são arquivos quebrados.
As cópias em `outputs/notebooks/` contêm resultados e têm função diferente das fontes.

## Limpeza realizada

Foram removidas 18 cópias com conteúdo idêntico por SHA-256: 16 em `backups/`
e duas bases em `data/processed_validacao/`. Cada conteúdo continua disponível
no caminho registrado no manifesto. Não foram removidas versões históricas diferentes.

Foi removido `pbi_inspect_readonly.py`: script pontual com porta fixa
`localhost:52266`, caminho absoluto e download/execução de um servidor externo.
Ele não era importado pelo pipeline e dependia de uma sessão antiga do Desktop.
O retrato de modelo que ele produziu foi preservado como evidência histórica.

`output/lider/` contém imagens e ferramentas de outro trabalho; foi preservado,
pois não é duplicata comprovada nem parte defeituosa do pipeline. `xnotebook/`
e versões únicas em `backups/` também foram mantidas. Os dois PBIX encontrados
não são idênticos e não foram excluídos ou renomeados.

## Correção funcional

O pipeline não executa o notebook 01. Antes, os CSVs detalhados só eram
exportados por esse notebook, podendo ficar antigos mesmo após uma execução
bem-sucedida do pipeline. A exportação agora também ocorre em
`executar_pipeline.py`, preservando os formatos e caminhos usados anteriormente.

## Verificação após a limpeza

O pipeline completo terminou com código de saída 0 e executou os notebooks 02 a 10.
As bases mantiveram 99.441 pedidos (42 colunas) e 112.650 itens (22 colunas).
Os dois CSVs detalhados foram comparados com a serialização dos respectivos Parquets.
A sintaxe dos módulos, os links dos READMEs e a existência das cópias preservadas
no manifesto também foram conferidos. Os avisos do Jupyter sobre o event loop
do Windows e o transporte TCP não interromperam a execução.

Esta verificação executou o Python; não executou a interface do Power Automate
nem atualizou ou salvou o PBIX. Para refletir as novas tabelas no relatório,
use o fluxo local já configurado ou atualize o Power BI manualmente.
