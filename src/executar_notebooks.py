from pathlib import Path

import nbformat
from nbclient import NotebookClient


RAIZ_PROJETO = Path(__file__).resolve().parent.parent


def executar_notebook(nome_arquivo):
    """Executa um notebook e salva uma cópia com os resultados."""

    caminho_entrada = RAIZ_PROJETO / 'notebooks' / nome_arquivo

    pasta_saida = RAIZ_PROJETO / 'outputs' / 'notebooks'
    pasta_saida.mkdir(parents=True, exist_ok=True)

    caminho_saida = pasta_saida / nome_arquivo

    if not caminho_entrada.is_file():
        raise FileNotFoundError(
            f'Notebook não encontrado: {caminho_entrada}'
        )

    notebook = nbformat.read(caminho_entrada, as_version=4)

    executor = NotebookClient(
        notebook,
        kernel_name='ecommerce',
        timeout=600, 
        allow_errors=False,
        resources={
            'metadata': {
                'path': str(RAIZ_PROJETO)
            }
        }
    )

    print(f'Executando: {nome_arquivo}')

    executor.execute()

    nbformat.write(notebook, caminho_saida)

    print(f'Notebook executado salvo em: {caminho_saida}')

    return caminho_saida