import pandas as pd


def preparar_avaliacoes(df_reviews_raw):
    """Trata as avaliações conforme as regras do notebook de preparação."""

    df_reviews = df_reviews_raw.copy()

    for coluna in ['review_creation_date', 'review_answer_timestamp']:
        df_reviews[coluna] = pd.to_datetime(
            df_reviews[coluna],
            errors='coerce'
        ).astype('datetime64[ns]')

    df_reviews['review_score'] = pd.to_numeric(
        df_reviews['review_score'],
        errors='coerce'
    )

    df_reviews['review_event_timestamp'] = (
        df_reviews['review_answer_timestamp']
        .combine_first(df_reviews['review_creation_date'])
    )

    df_reviews = (
        df_reviews
        .dropna(subset=['order_id', 'review_score'])
        .loc[lambda df: df['review_score'].between(1, 5)]
        .sort_values(['order_id', 'review_event_timestamp'])
        .drop_duplicates(subset=['order_id'], keep='first')
        .drop_duplicates(subset=['review_id'], keep='first')
        .reset_index(drop=True)
        .copy()
    )

    df_reviews['review_ruim'] = df_reviews['review_score'].le(2)
    df_reviews['review_neutra'] = df_reviews['review_score'].eq(3)
    df_reviews['review_boa'] = df_reviews['review_score'].ge(4)

    assert df_reviews['order_id'].is_unique
    assert df_reviews['order_id'].notna().all()
    assert df_reviews['review_score'].notna().all()
    assert df_reviews['review_score'].between(1, 5).all()

    assert (
        df_reviews[['review_ruim', 'review_neutra', 'review_boa']]
        .sum(axis=1)
        .eq(1)
        .all()
    )

    return df_reviews


def preparar_pedidos_clientes(df_pedidos_raw, df_clientes_raw):
    """Relaciona pedidos aos clientes e converte as datas do pedido."""

    # Confere as chaves antes de juntar as tabelas.
    assert df_pedidos_raw['order_id'].is_unique
    assert df_pedidos_raw['order_id'].notna().all()
    assert df_pedidos_raw['customer_id'].notna().all()

    assert df_clientes_raw['customer_id'].is_unique
    assert df_clientes_raw['customer_id'].notna().all()

    # Acrescenta os dados do cliente a cada pedido.
    df_pedidos_clientes = (
        df_pedidos_raw
        .merge(
            df_clientes_raw,
            on='customer_id',
            how='left',
            validate='1:1'
        )
        .copy()
    )

    colunas_datas = [
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date'
    ]

    for coluna in colunas_datas:
        df_pedidos_clientes[coluna] = pd.to_datetime(
            df_pedidos_clientes[coluna],
            errors='coerce'
        ).astype('datetime64[ns]')

    assert len(df_pedidos_clientes) == len(df_pedidos_raw)
    assert df_pedidos_clientes['order_id'].is_unique
    assert df_pedidos_clientes['order_id'].notna().all()
    assert df_pedidos_clientes['customer_id'].is_unique

    return df_pedidos_clientes



def preparar_itens(df_itens_raw, df_produtos_raw, df_vendedores_raw):
    """Enriquece os itens com informações de produtos e vendedores."""

    # Confere as chaves das tabelas de produtos e vendedores.
    assert df_produtos_raw['product_id'].is_unique
    assert df_produtos_raw['product_id'].notna().all()

    assert df_vendedores_raw['seller_id'].is_unique
    assert df_vendedores_raw['seller_id'].notna().all()

    colunas_chave = [
        'order_id',
        'order_item_id',
        'product_id',
        'seller_id'
    ]

    assert df_itens_raw[colunas_chave].notna().all().all()

    df_itens = (
        df_itens_raw
        .merge(
            df_produtos_raw,
            on='product_id',
            how='left',
            validate='m:1'
        )
        .merge(
            df_vendedores_raw,
            on='seller_id',
            how='left',
            validate='m:1'
        )
        .copy()
    )

    df_itens['shipping_limit_date'] = pd.to_datetime(
        df_itens['shipping_limit_date'],
        errors='coerce'
    ).astype('datetime64[ns]')

    assert len(df_itens) == len(df_itens_raw)
    assert not df_itens.duplicated(
        subset=['order_id', 'order_item_id']
    ).any()

    assert df_itens['price'].notna().all()
    assert df_itens['freight_value'].notna().all()
    assert df_itens['price'].ge(0).all()
    assert df_itens['freight_value'].ge(0).all()

    df_itens['volume_item_cm3'] = (
        df_itens['product_length_cm']
        * df_itens['product_height_cm']
        * df_itens['product_width_cm']
    )

    df_itens['dimensoes_ausentes'] = (
        df_itens[
            [
                'product_length_cm',
                'product_height_cm',
                'product_width_cm'
            ]
        ]
        .isna()
        .any(axis=1)
    )

    df_itens['peso_ausente'] = df_itens['product_weight_g'].isna()
    df_itens['categoria_ausente'] = (
        df_itens['product_category_name'].isna()
    )

    return df_itens


def resumir_itens_por_pedido(df_itens):
    """Agrupa os itens e calcula os indicadores de cada pedido."""

    df_resumo = (
        df_itens
        .groupby('order_id')
        .agg(
            quantidade_itens=(
                'order_item_id', 'nunique'
            ),
            quantidade_produtos=(
                'product_id', 'nunique'
            ),
            quantidade_vendedores=(
                'seller_id', 'nunique'
            ),
            quantidade_categorias=(
                'product_category_name', 'nunique'
            ),
            valor_produtos=(
                'price', 'sum'
            ),
            valor_frete=(
                'freight_value', 'sum'
            ),
            peso_total_g=(
                'product_weight_g',
                lambda valores: valores.sum(min_count=1)
            ),
            volume_total_cm3=(
                'volume_item_cm3',
                lambda valores: valores.sum(min_count=1)
            ),
            possui_dimensoes_ausentes=(
                'dimensoes_ausentes', 'any'
            ),
            possui_peso_ausente=(
                'peso_ausente', 'any'
            ),
            possui_categoria_ausente=(
                'categoria_ausente', 'any'
            )
        )
        .reset_index()
        .copy()
    )

    df_resumo['valor_total'] = (
        df_resumo['valor_produtos']
        + df_resumo['valor_frete']
    )

    df_resumo['pct_frete'] = (
        df_resumo['valor_frete']
        / df_resumo['valor_produtos'].replace(0, pd.NA)
    )

    df_resumo['pedido_um_produto'] = (
        df_resumo['quantidade_produtos'].eq(1)
    )

    df_resumo['pedido_um_vendedor'] = (
        df_resumo['quantidade_vendedores'].eq(1)
    )

    assert df_resumo['order_id'].is_unique
    assert df_resumo['order_id'].notna().all()
    assert len(df_resumo) == df_itens['order_id'].nunique()
    assert df_resumo['quantidade_itens'].ge(1).all()
    assert df_resumo['quantidade_produtos'].ge(1).all()
    assert df_resumo['quantidade_vendedores'].ge(1).all()

    return df_resumo

def construir_base_analitica(
    df_pedidos_clientes,
    df_resumo_itens,
    df_avaliacoes
):
    """Reúne as tabelas e cria os indicadores da base analítica."""

    for tabela in [
        df_pedidos_clientes,
        df_resumo_itens,
        df_avaliacoes
    ]:
        assert tabela['order_id'].is_unique
        assert tabela['order_id'].notna().all()

    df_base = (
        df_pedidos_clientes
        .merge(
            df_resumo_itens,
            on='order_id',
            how='left',
            validate='1:1'
        )
        .merge(
            df_avaliacoes,
            on='order_id',
            how='left',
            validate='1:1'
        )
        .copy()
    )

    df_base['possui_itens'] = (
        df_base['quantidade_itens'].notna()
    )

    df_base['possui_avaliacao'] = (
        df_base['review_score'].notna()
    )

    df_base['pedido_entregue'] = (
        df_base['order_status'].eq('delivered')
    )

    df_base['delivery_delay_days'] = (
        df_base['order_delivered_customer_date']
        - df_base['order_estimated_delivery_date']
    ).dt.days

    df_base['is_late'] = pd.Series(
        pd.NA,
        index=df_base.index,
        dtype='boolean'
    )

    prazo_disponivel = df_base['delivery_delay_days'].notna()

    df_base.loc[prazo_disponivel, 'is_late'] = (
        df_base.loc[prazo_disponivel, 'delivery_delay_days']
        .gt(0)
    )

    assert len(df_base) == len(df_pedidos_clientes)
    assert df_base['order_id'].is_unique
    assert df_base['order_id'].notna().all()

    assert df_base.loc[
        ~prazo_disponivel, 'is_late'
    ].isna().all()

    return df_base