import random


def posicao_suporta(mapa, numero_de_blocos, linha, coluna, orientacao):
    if mapa[linha][coluna] == ' N ' or mapa[linha][coluna] == N or mapa[linha][coluna] == T:
        return False
    for espaco in range(0,numero_de_blocos):
        if orientacao == 'v':
            if linha + espaco >= len(mapa):
                return False
            if mapa[linha+espaco][coluna] == ' N ' or mapa[linha+espaco][coluna] == N or mapa[linha+espaco][coluna] == T:
                return False
        elif orientacao == 'h':
            if coluna+espaco >= len(mapa):
                return False
            if mapa[linha][coluna+espaco] == ' N ' or mapa[linha][coluna+espaco] == N or mapa[linha][coluna+espaco] == T:
                return False
        else:
            print('AAAAAAAAAAAAAAAAAAAAAAA')
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
            if place == 'N' or place == T:
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
        if continua == False or pos_igual == True or continua == 'Direção inválida':
            while continua == False or pos_igual == True or continua == 'Direção inválida':
                linha = random.choice(linhas_possiveis); coluna = random.choice(colunas_possiveis); orientacao = random.choice(['v','h'])
                continua = posicao_suporta(mapa, b, linha, coluna, orientacao)
                pos_igual = [linha, coluna] in ocupados
                if continua == False or continua == 'Direção inválida':
                    continue
            if orientacao == 'v':
                for i in range(0, b):
                    mapa[linha+i][coluna] = ' N '
                    ocupados.append([linha+i, coluna])
            if orientacao == 'h':
                for i in range(0, b):
                    mapa[linha][coluna+i] = ' N '
                    ocupados.append([linha, coluna+i])
        elif orientacao == 'v':
            for i in range(0, b):
                mapa[linha+i][coluna] = ' N '
                ocupados.append([linha+i, coluna])
        elif orientacao == 'h':
            for i in range(0, b):
                mapa[linha][coluna+i] = ' N '
                ocupados.append([linha, coluna+i])
    return mapa  

def aloca_navios_jogador (mapa, numero_de_blocos, linha, coluna, orientacao):
    # numero_de_blocos = [numero_de_blocos]
    ocupados = []
    for line in mapa:
        cod = []
        c = 0
        for place in line:
            if place == ' N ':
                cod.append(mapa.index(line))
                cod.append(c)
                ocupados.append(cod)
                cod = []
            c+=1
            if c >= len(line):
                c = 0
    linha = linha; coluna = coluna; orientacao = orientacao
    pos_igual = [linha, coluna] in ocupados
    if pos_igual == True or posicao_suporta(mapa, numero_de_blocos, linha, coluna, orientacao) == False:
        return False
    elif orientacao == 'v':
        for i in range(0, numero_de_blocos):
            mapa[linha+i][coluna] = ' N '
    elif orientacao == 'h':
        for i in range(0, numero_de_blocos):
            mapa[linha][coluna+i] = ' N '
    return mapa  

W = '\u001b[34m███'
X = '\u001b[31m███'
N = '\u001b[32m███'
T = '\u001b[33m███' 
C = '\u001b[36m███'
B = '\u001b[30m███'