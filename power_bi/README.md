# Power BI e Power Automate

## Responsabilidades

1. `executar_pipeline.py` prepara as bases, executa os notebooks e exporta as tabelas.
2. O fluxo local `Pipeline ecommerce`, no Power Automate Desktop, executa o Python.
3. Após sucesso, o fluxo clica em Atualizar, aguarda a janela aparecer e desaparecer
   e salva o PBIX aberto no Power BI Desktop.

O comando Python sozinho não abre, atualiza ou salva o Power BI.
A exportação automática de PDF foi adiada e deve permanecer desabilitada.
Um PDF existente em disco é uma exportação manual e pode estar desatualizado.

## Uso diário

- Disponibilize os seis CSVs de entrada em `data/raw/`.
- Abra o relatório correto no Power BI Desktop, sem menus ou diálogos.
- Execute o fluxo salvo no Power Automate, mantendo a sessão do Windows desbloqueada.
- Não use mouse e teclado durante as ações de interface.
- Confira erros no Power BI e a data de modificação do PBIX após salvar.
- Não execute duas instâncias do pipeline ao mesmo tempo: as saídas têm nomes fixos.

O fluxo chama `C:\Dataset\ecommerce\.venv\Scripts\python.exe` com
`C:\Dataset\ecommerce\executar_pipeline.py` e só prossegue ao encontrar
`PIPELINE_OK` na saída do script PowerShell. Esse marcador pertence ao invólucro
do Power Automate, não ao programa Python. Preserve a verificação do código de saída.

A janela Atualizar desaparecer não comprova por si só ausência de erros. O fluxo
local ainda depende dos seletores da instalação e da conferência de falhas do Power BI.
Não há abertura automática do relatório nem geração de cópias por execução.

## Arquivos locais

Na revisão foram encontrados `../Pbi.pbix` e `../outputs/powerbi/relatorio.pbix`.
São arquivos diferentes, portanto ambos foram preservados. Confirme o caminho
do arquivo aberto antes de testar o salvamento; o nome encontrado em disco é
`relatorio.pbix`, no singular. Não renomeie o relatório sem revisar os seletores
do Power Automate. O salvamento atualiza o próprio arquivo aberto.

O fluxo do Power Automate é mantido no aplicativo e não está exportado neste
repositório. Copiar apenas esta pasta não transfere a automação para outro computador.

## Fontes dos dados

- Bases detalhadas: `outputs/tabelas/csv/base_analitica_pedidos.csv` e
  `itens_pedidos.csv`: vírgula, ponto decimal, UTF-8 com BOM.
- Resumos `02_` a `10_`: `outputs/tabelas/csv/`: ponto e vírgula,
  vírgula decimal, UTF-8 com BOM.
- Parquets detalhados: `data/processed/`; resumos: `outputs/tabelas/parquet/`.

O pipeline agora atualiza também os CSVs detalhados a cada execução. Os nomes,
colunas e formatos existentes foram mantidos. CSV e Parquet são saídas para
consumidores diferentes; não são duplicatas descartáveis.

## Auditoria histórica

`plano_modelagem.md` e `revisao_relatorio_2026-10-19.md` são análises datadas,
não descrições garantidas do estado atual do PBIX. `audit_layout.json`,
`audit_visual_summary.txt` e `../pbi_model_readonly.json` são retratos de inspeção.
Não são fontes do pipeline. `summarize_audit.py` recria o resumo do layout;
execute-o a partir da raiz do projeto. Não atualiza nem salva o relatório.
