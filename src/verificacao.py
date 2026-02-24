from pandas import DataFrame

def realizarVerificacao(valorPadronizado:DataFrame):
    print("Linhas e colunas do dataset:", valorPadronizado.shape)
    print('--------------------')

    print("Colunas:")
    print(valorPadronizado.columns.tolist())
    print('--------------------')

    print("\nInformacoes:")
    valorPadronizado.info()
    print('--------------------')

    print("\nValores nulos existentes:")
    print(valorPadronizado.isnull().sum())
    print('--------------------')

    print("\ndados duplicados:", valorPadronizado.duplicated().sum())
    