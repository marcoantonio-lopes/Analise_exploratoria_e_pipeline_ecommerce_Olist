from pathlib import Path

from src.executar_notebooks import executar_notebook

import pandas as pd

from src.carregar_dados import carregar_dados

from src.preparar_dados import (
    preparar_avaliacoes,
    preparar_pedidos_clientes,
    preparar_itens,
    resumir_itens_por_pedido,
    construir_base_analitica
)


def main():
    tabelas = carregar_dados()

    avaliacoes = preparar_avaliacoes(tabelas['reviews'])

    pedidos_clientes = preparar_pedidos_clientes(
        tabelas['pedidos'],
        tabelas['clientes']
    )

    itens = preparar_itens(
        tabelas['itens'],
        tabelas['produtos'],
        tabelas['vendedores']
    )

    resumo_itens = resumir_itens_por_pedido(itens)

    base_analitica = construir_base_analitica(
        pedidos_clientes,
        resumo_itens,
        avaliacoes
    )

    print('Base analítica:', base_analitica.shape)
    print('Base de itens:', itens.shape)

    print(
        'Pedidos sem itens:',
        (~base_analitica['possui_itens']).sum()
    )

    print(
        'Pedidos sem avaliação:',
        (~base_analitica['possui_avaliacao']).sum()
    )

    print(
        'Pedidos sem cálculo de atraso:',
        base_analitica['is_late'].isna().sum()
    )
    

    raiz_projeto = Path(__file__).resolve().parent
    pasta_processados = raiz_projeto / 'data' / 'processed'


    pasta_processados.mkdir(parents=True, exist_ok=True)

    caminho_base = (
        pasta_processados / 'base_analitica_pedidos.parquet'
    )

    caminho_itens = (
        pasta_processados / 'itens_pedidos.parquet'
    )

    base_analitica.to_parquet(caminho_base, index=False)
    itens.to_parquet(caminho_itens, index=False)

    base_salva = pd.read_parquet(caminho_base)
    itens_salvos = pd.read_parquet(caminho_itens)

    pd.testing.assert_frame_equal(
        base_analitica,
        base_salva,
        check_exact=True
    )

    pd.testing.assert_frame_equal(
        itens,
        itens_salvos,
        check_exact=True
    )

    # O notebook 01 é uma referência manual e não roda neste pipeline.
    # Atualiza também as fontes detalhadas CSV usadas nas consultas do Power BI.
    pasta_csv = raiz_projeto / 'outputs' / 'tabelas' / 'csv'
    pasta_csv.mkdir(parents=True, exist_ok=True)
    for nome, tabela in (
        ('base_analitica_pedidos', base_analitica),
        ('itens_pedidos', itens),
    ):
        # Preserva o formato do notebook 01: vírgula e ponto decimal.
        tabela.to_csv(pasta_csv / f'{nome}.csv', index=False, encoding='utf-8-sig')

    print('Bases salvas e exportação conferida.')
    print('Base analítica:', caminho_base)
    print('Base de itens:', caminho_itens)
    
    notebooks_analise = [
        '02_atrasos.ipynb',
        '03_produtos.ipynb',
        '04_regioes.ipynb',
        '05_vendedores.ipynb',
        '06_taxa_recompra.ipynb',
        '07_inferencia_recompra.ipynb',
        '08_produtos_categorias_atraso_avaliacao.ipynb',
        '09_regioes_estados_atraso_avaliacao.ipynb',
        '10_recompra_atraso_avaliacao.ipynb'
    ]

    for nome_notebook in notebooks_analise:
        executar_notebook(nome_notebook)
    
    print('Pipeline concluído: bases, notebooks, tabelas e gráficos atualizados.')

if __name__ == '__main__':
    main()

    
