import random
import time
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numfabeto ='10112131415161718192021223242526'
def foi_derrotado_jogador(matriz):
    for p in matriz:
        for k in p:
            if k == N:
                return False
    return True
def foi_derrotado_robo(matriz):
    for p in matriz:
        for k in p:
            if k == T:
                return False
    return True
# def posicao(string):
#     maiusculo = string.upper()
#     coluna = alfabeto.index(maiusculo[0])
#     linha = int(maiusculo[1:])-1 #já que começa no 0
#     return coluna, linha
def frotas(pais_j, pais_c):
    pais_jogador = []
    for n,q in paises[pais_j].items():
        if q > 1:
            for i in range(q):
                pais_jogador.append(n)
        else: pais_jogador.append(n)
    pais_computador = []
    for n,q in paises[pais_c].items():
        if q > 1:
            for i in range(q):
                pais_computador.append(n)
        else: pais_computador.append(n)
    frota_pais = [pais_jogador, pais_computador]
    return frota_pais  
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

def cria_mapa(N):
    final = []
    for _ in range(N):
        Linha = [W]*(N)
        final.append(Linha)
    return final


def formatador(robo, humano):

    espaconum = 0
    espaco =''
    AbcCalculo = alfabeto[:size]
    AbcPrint = '    '
    for i in AbcCalculo:
        AbcPrint += i + '  '
        espaconum += 3
    espaconum -= 12
    espaconum = espaconum//2
    for i in range(espaconum):
        espaco += ' '
    print('  ',espaco,'COMPUTADOR  ',espaco,'                            ',espaco,'JOGADOR')
    print(AbcPrint,'                        ',AbcPrint)
    #A proxima linha de codigo esconde a posição dos robos
    for linha in range(len(robo)):
        for ponto in range(len(robo)):
            if robo[linha][ponto] == ' N ':
                robo[linha][ponto] = T
            if humano[linha][ponto] == ' N ':
                humano[linha][ponto] = N

    for i in range(len(robo)):
        pos_reverso = i +1
        pos = i + 1
        pos = str(pos)
        if int(pos) < 10:
            pos_reverso =  pos + ' '
            pos = ' ' + pos
        


        RoboPrint = ''
        HumanoPrint = ''
        for ponto in range(size):
            if robo[i][ponto] == C:
                RoboPrint += C
            elif robo[i][ponto] == X:
                RoboPrint += X
            else: RoboPrint += f'{B}'
            HumanoPrint += humano[i][ponto]
        

        #print(robo[i])
        print(pos,RoboPrint,'\u001b[0m',pos_reverso,'                     ',pos,HumanoPrint,'\u001b[0m',i+1)

    print(AbcPrint,'                        ',AbcPrint)

    debug = 0
    for i in robo:
        for ii in i:
            if ii == T:
                debug += 1
    print('Precisamos destruir ',debug, 'locais do inimigo')



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

def letra_valida(letra):
    if (letra not in alfabeto and letra not in alfabeto.lower()) or len(letra) > 1 or alfabeto.index(letra.upper()) >= size:
        return False
    return True

def numero_valido(numero):
    if numero not in numfabeto:
        return False
    numero = int(numero)
    if numero > size or numero == 0:
        return False
    return True

size = int(input())

cores = {'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'}

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
    }, 'Aústralia': {
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

W = '\u001b[34m███'
X = '\u001b[31m███'
N = '\u001b[32m███'
T = '\u001b[33m███' 
C = '\u001b[36m███'
B = '\u001b[30m███'