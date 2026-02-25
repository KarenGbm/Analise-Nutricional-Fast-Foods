import pandas as pd

coluna_conversao_numero = [
        'calories',
        'calories_from_fat',
        'total_fat_g',
        'saturated_fat_g',
        'trans_fat_g',
        'cholesterol_mg',
        'sodium_mg',
        'carbs_g',
        'fiber_g',
        'sugars_g',
        'protein_g',
        'weight_watchers_pnts'
    ]

colunas_dividir = [
        'weight_watchers_pnts',
        'sodium_mg',
        'cholesterol_mg'
    ]

def realizarTratamento(dados: pd.DataFrame):
    
    dados = dados.drop_duplicates().copy() 
    print("Quantidade de duplicatas após tratamento:", dados.duplicated().sum())
    print('--------------------')

    for coluna in coluna_conversao_numero:
        dados[coluna] = pd.to_numeric(dados[coluna], errors='coerce')
    

    for item in colunas_dividir:
        dados[item] = dados[item]/10

    return dados

def exibirDadosPosConversao(dados:pd.DataFrame):
    print('dados string para numericos: ', dados.dtypes)

def exibirDadosPosTratamento(dados:pd.DataFrame):
    print("\n quantidade de Nulos após conversão numérica:")
    print(dados[coluna_conversao_numero].isnull().sum())
    print('--------------------')

    print("\nEstatísticas pós conversão:")
    print(dados[coluna_conversao_numero].describe())
    print('--------------------')

    print("\nEmpresas existentes:")
    print(dados["company"].unique())
    print('--------------------')

def realizarValidacaoNegativo(dados:pd.DataFrame):
    for coluna in coluna_conversao_numero:
        negativos = (dados[coluna] < 0).sum()
    if negativos > 0:
        print(f"{coluna}: {negativos} valores negativos")

