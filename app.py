import pandas as pd
from src.padronizacao import padronizar
from src.verificacao import realizarVerificacao
from src.tratamento import realizarTratamento, exibirDadosPosConversao, exibirDadosPosTratamento, realizarValidacaoNegativo

dados = pd.read_csv("data/raw/FastFoodNutritionMenuV3.csv")

valorPadronizado = padronizar(dados)

realizarVerificacao(valorPadronizado)

valorTratado = realizarTratamento(valorPadronizado)

exibirDadosPosConversao(valorTratado)

exibirDadosPosTratamento(valorTratado)

realizarValidacaoNegativo(valorTratado)






