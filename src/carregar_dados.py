from pathlib import Path
import pandas as pd


RAIZ_PROJETO = Path(__file__).resolve().parent.parent

CAMINHO_DADOS = RAIZ_PROJETO / 'data' / 'raw'


def carregar_dados(caminho_dados=CAMINHO_DADOS):
    """Carrega as seis tabelas utilizadas na preparação da base."""

    # Aceita tanto um caminho em texto quanto um objeto Path.
    caminho_dados = Path(caminho_dados)

    # Cada nome identifica uma tabela e seu respectivo arquivo.
    arquivos = {
        'reviews': 'olist_order_reviews_dataset.csv',
        'clientes': 'olist_customers_dataset.csv',
        'itens': 'olist_order_items_dataset.csv',
        'pedidos': 'olist_orders_dataset.csv',
        'produtos': 'olist_products_dataset.csv',
        'vendedores': 'olist_sellers_dataset.csv'
    }

    # Confere se todos os arquivos existem antes de iniciar a leitura.
    arquivos_ausentes = [
        nome_arquivo
        for nome_arquivo in arquivos.values()
        if not (caminho_dados / nome_arquivo).is_file()
    ]

    if arquivos_ausentes:
        raise FileNotFoundError(
            f'Arquivos não encontrados em {caminho_dados}: '
            + ', '.join(arquivos_ausentes)
        )

    # O dicionário guardará um DataFrame para cada tabela.
    tabelas = {}

    for nome_tabela, nome_arquivo in arquivos.items():
        tabelas[nome_tabela] = pd.read_csv(
            caminho_dados / nome_arquivo
        )

    return tabelas