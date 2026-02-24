from pandas import DataFrame

def padronizar(dados:DataFrame):
    dados.columns = (
    dados.columns
        .str.strip()
        .str.lower()
        .str.replace(r"\s+", "_", regex=True)   
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
)
    return dados;