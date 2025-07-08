import seaborn as sns
from scipy.stats import (
    levene,
    mannwhitneyu,
    ttest_ind,
)

def remove_outliers(dados, largura_bigodes=1.5):
    q1 = dados.quantile(0.25)
    q3 = dados.quantile(0.75)
    iqr = q3 - q1
    return dados[(dados >= q1 - largura_bigodes * iqr) & (dados <= q3 + largura_bigodes * iqr)]

def analise_levene(dataframe, alfa=0.05, centro='mean'):
    print('Teste de Levene')
    
    estatistica_levene, valor_p_levene = levene(
        *[dataframe[coluna] for coluna in dataframe.columns],
        center=centro,
        nan_policy='omit'
    )

    print(f'Est {estatistica_levene = :.3f}')
    if valor_p_levene > alfa:
        print(f'Variâncias iguais. (Valor p: {valor_p_levene:.3f})')
    else:
        print(f'Ao menos uma variância é diferente. (Valor p: {valor_p_levene:.3f})')

def analise_ttest_ind(
    dataframe,
    alfa=0.05,
    variancias_iguais=True,
    alternativa='two-sided',
):
    print("Teste t de Student")
    estatistica_ttest, valor_p_ttest = ttest_ind(
        *[dataframe[coluna] for coluna in dataframe.columns],
        equal_var=variancias_iguais,
        alternative=alternativa,
        nan_policy='omit'
    )

    print(f'{estatistica_ttest = :.3f}')
    if valor_p_ttest > alfa:
        print(f'Não reita a hipótese nula. (Valor p: {valor_p_ttest:.3f})')
    else:
        print(f'Rejeita a hipótese nula. (Valor p: {valor_p_ttest:.3f})')

def analise_mannwhitneyu(
    dataframe,
    alternativa='two-sided',
    alfa=0.05
):
    print("Teste de Nann-Whitneyu")
    estatistica_nw, valor_p_nw = mannwhitneyu(
        *[dataframe[coluna] for coluna in dataframe.columns],
        alternative=alternativa,
        nan_policy='omit'
    )


    print(f'{estatistica_nw = :.3f}')
    if valor_p_nw > alfa:
        print(f'Não reita a hipótese nula. (Valor p: {valor_p_nw:.3f})')
    else:
        print(f'Rejeita a hipótese nula. (Valor p: {valor_p_nw:.3f})')
