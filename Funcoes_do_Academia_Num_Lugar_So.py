import numpy as np
import random
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
def aloca_navios (mapa, lista_numero_de_blocos):
    linhas_possiveis = list(range(0, len(mapa)))
    colunas_possiveis = list(range(0, len(mapa)))
    ocupados = []
    for line in mapa:
        cod = []
        c = 0
        for place in line:
            if place == 'N':
                cod.append(mapa.index(line))
                cod.append(c)
                ocupados.append(cod)
                cod = []
            c+=1
            if c >= len(line):
                c = 0
    for b in lista_numero_de_blocos:
        linha = random.choice(linhas_possiveis); coluna = random.choice(colunas_possiveis); orientacao = random.choice(['v','h'])
        continua = posicao_suporta(mapa, b, linha, coluna, orientacao)
        pos_igual = [linha, coluna] in ocupados
        if continua == False or pos_igual == True:
            while continua == False or pos_igual == True:
                linha = random.choice(linhas_possiveis); coluna = random.choice(colunas_possiveis); orientacao = random.choice(['v','h'])
                continua = posicao_suporta(mapa, b, linha, coluna, orientacao)
                pos_igual = [linha,coluna] in ocupados
            if orientacao == 'v':
                for i in range(0, b):
                    mapa[linha+i][coluna] = 'N'
                # return mapa
            if orientacao == 'h':
                for i in range(0, b):
                    mapa[linha][coluna+i] = 'N'
                # return mapa
        elif orientacao == 'v':
            for i in range(0, b):
                mapa[linha+i][coluna] = 'N'
            # return mapa
        elif orientacao == 'h':
            for i in range(0, b):
                mapa[linha][coluna+i] = 'N'
    return mapa  
print(aloca_navios([
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ']
], [3, 2]))
            

