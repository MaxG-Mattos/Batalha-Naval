import numpy as np
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def foi_derrotado(matriz):
    for p in matriz:
        for k in p:
            if k == 'N':
                return False
    return True
def posicao(string):
    # alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    maiusculo = string.lower()
    coluna = alfabeto.index(maiusculo[0])
    linha = int(maiusculo[1:])-1 #já que começa no 0
    return coluna, linha
def cria_mapa(numb):
    saida = []
    partes = []
    pas = ""
    linhas = numb
    colunas = numb
    for i in range(colunas):
        for k in range(linhas):
            partes.append(pas)
        saida.append(partes)
        partes = []
    return saida
# print(cria_mapa(4))
def posicao_suporta(mapa, numero_de_blocos, linha, coluna, orientacao):
    if mapa[linha][coluna] == 'N':
        return False
    for espaco in range(0,numero_de_blocos):
        if orientacao == 'v':
            if linha + espaco >= len(mapa):
                return False
            if mapa[linha+espaco][coluna] == 'N':
                return False
        elif orientacao == 'h':
            if coluna+espaco >= len(mapa):
                return False
            if mapa[linha][coluna+espaco] == 'N':
                return False
        else:
            return 'Direção inválida'
    return True
# print(posicao_suporta([
#     [' ', ' ', ' ', 'N', ' '],
#     [' ', ' ', ' ', 'N', ' '],
#     ['N', 'N', ' ', 'N', ' '],
#     [' ', ' ', ' ', ' ', ' '],
#     ['N', 'N', 'N', ' ', ' ']
# ], 2, 3, 4, 'h'))