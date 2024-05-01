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
def mostrado (mapa):
    lim = alfabeto[:10]
    letras = []
    for l in lim:
        letras.append(f'{l}')
    letras = '   '.join(letras)
    print(f'    {letras}')
    for m in range(len(mapa)):
        print(f'{m+1}  {mapa[m]}')
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
bloco_por_navio = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}
# quantidade de tipos de návio por país
paises = {'França':{
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    }, 'Brasil':{
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    }, 'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    }, 'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }}
# esse embaixo provavelmente vai facilitar na hora de escolher os jogadores
numero_pais = {0: 'Brasil',1 : 'França', 2 : 'Aústralia', 3 : 'Rússia', 4 : 'Japão' }
print('0 = Brasil\n1 = França\n2 = Aústralia\n3 = Rússia\n4 = Japão')
jogador_num = int(input('qual o numero do pais que tu queres jogar? ')) #o jogador diz o número do país q ele quer jogar
jogador = numero_pais[jogador_num] #pega o país do dicionario usando o número como chave
computador = None #aqui vai ficar o país do computador
aleatorio_computador = True #se isso for verdade o país do computador vai ser escolhido aleatoriamente
escolha = input('Caso queira escolher o país do computador digite "S", caso não digite qualquer outro caractere: ') #aqui o jogador diz se ele quer escolher o país do computador ou não
if escolha == 'S' or escolha == 's': #se o jogador quiser escolher o aleatorio computador vai ser falso e ele pula pro else
    aleatorio_computador = False
if aleatorio_computador: #se aleatorio_computador for verdade ele cai aqui e escolhe aleatoriamente
    computador = random.choice(list(numero_pais.values())) #pega um país aleatório
    if computador == jogador: #se o país for igual ao do jogador ele cai no while até pegar um diferente
        while computador == jogador:
            computador = random.choice(list(numero_pais.values())) #voce tem que transformar os valores em lista se n o random n funciona nessa situação
else:
    print('0 = Brasil\n1 = França\n2 = Aústralia\n3 = Rússia\n4 = Japão')
    computador_num = int(input('qual o numero do pais que tu queres jogar contra? '))
    if computador_num == jogador_num:
        while computador_num == jogador_num:
            computador_num = int(input('esse país já está sendo usado, digite outro: '))
        computador = numero_pais[computador_num]
    computador = numero_pais[computador_num]
print(f'você está jogando como {jogador}, seu oponente está jogando como {computador}')
mapa = cria_mapa(10)
mostrado(mapa)
