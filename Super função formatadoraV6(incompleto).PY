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
                    mapa[linha+i][coluna] = ' N '
                # return mapa
            if orientacao == 'h':
                for i in range(0, b):
                    mapa[linha][coluna+i] = ' N '
                # return mapa
        elif orientacao == 'v':
            for i in range(0, b):
                mapa[linha+i][coluna] = ' N '
            # return mapa
        elif orientacao == 'h':
            for i in range(0, b):
                mapa[linha][coluna+i] = ' N '
    return mapa  

def cria_mapa(N):
    final = []
    for _ in range(N):
        Linha = [W]*(N)
        final.append(Linha)
    return final


def formatador(robo, humano):
    robo_P = robo
    humano_P = humano

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
    print(AbcPrint,'                       ',AbcPrint)
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
    
            RoboPrint += robo[i][ponto]
            HumanoPrint += humano[i][ponto]
        

        #print(robo[i])
        print(pos,RoboPrint,'\u001b[0m',pos_reverso,'                     ',pos,HumanoPrint,'\u001b[0m',i+1)

    print(AbcPrint,'                        ',AbcPrint)



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
# selecionando tamanho do mapa
tamanho_mapa_aleatorio = False
size = None
escolha_de_dimensao = input('Você quer escolher a dimensão do seu mapa?  S/N ')
escolha_de_dimensao = escolha_de_dimensao.upper()
if escolha_de_dimensao == 'N' or escolha_de_dimensao == 'n':
    tamanho_mapa_aleatorio = True
if tamanho_mapa_aleatorio:
    size = random.randrange(5, 13) #dps do 13 não tem mais como deixar o gráfico formatado, ele não cabe no terminal
else:
    size = int(input('\nO mapa é quadrado, portanto o tamanho de linhas é igual ao de colunas\nescolha um número entre 5 e 13: '))
    if size > 13 or size < 5:
        while size > 13 or size < 5:
            size = int(input('por favor escolha outra dimensão: '))

print(f'\nVocê está jogando como {jogador}. O Computador está jogando como {computador}')

robo = cria_mapa(size)
humano = cria_mapa(size)
navios = frotas(jogador, computador)
navios_computador = navios[1] 
navios_jogador = navios[0]
bloco_navio_pc = []
for n in navios_computador:
    bloco_navio_pc.append(bloco_por_navio[n])
robo = aloca_navios(robo, bloco_navio_pc)
formatador(robo, humano)

print('Hora de alocar suas tropas!\n')
while len(navios_jogador) > 0:
    print(f'Seus navios disponiveis são: {navios_jogador}')
    print(f'Você agora está alocando {navios_jogador[0]}\nEle possui {bloco_por_navio[navios_jogador[0]]} blocos')
    
    linha = (input('Em que linha você quer posicionar?')); 
    while numero_valido(linha) == False:
        linha = input('Por favor, selecione uma linha valida')

    linha = int(linha); linha = linha -1


    coluna = input('Em que coluna queres posicionar? ')
    while letra_valida(coluna) == False:
        coluna = input('Por favor, selecione uma coluna valida')

    coluna = coluna.upper(); coluna = alfabeto.index(coluna)

    orientacao = input('Horizontal ou Vertical? | v/h |')
    while orientacao != 'h' and orientacao != 'v' and orientacao != 'V' and orientacao != 'H':
        orientacao  = input('Por favor selecione uma orientação valida')

    orientacao = orientacao.lower()
    pode_colocar = posicao_suporta(humano, bloco_por_navio[navios_jogador[0]], linha, coluna, orientacao)
    mapa = aloca_navios_jogador(humano, bloco_por_navio[navios_jogador[0]], linha, coluna, orientacao)
    if pode_colocar == False or mapa == False:
        while pode_colocar == False and mapa == False:
            print('Posição inválida, tente outra: ')
            linha = int(input('Em que linha você quer posicionar?')); linha = linha -1
            coluna = input('Em que coluna queres posicionar? ')
            coluna = coluna.upper(); coluna = alfabeto.index(coluna)
            
            orientacao = input('Horizontal ou Vertical? | v/h |')
            while orientacao != 'h' and orientacao != 'v' and orientacao != 'V' and orientacao != 'H':
                orientacao  = input('Por favor selecione uma orientação valida')

            print(print(f'Seu návio atual possui {bloco_por_navio[navios_jogador[0]]} blocos'))
            orientacao = orientacao.lower()
            pode_colocar = posicao_suporta(humano, bloco_por_navio[navios_jogador[0]], linha, coluna, orientacao)
            mapa = aloca_navios_jogador(humano, bloco_por_navio[navios_jogador[0]], linha, coluna, orientacao)
        humano = mapa
        formatador(robo, humano)
        del navios_jogador[0]
    else:
        humano = mapa
        formatador(robo, humano)
        del navios_jogador[0]

print('INICIANDO A BATALHA NAVAL!')
time.sleep(1)
print('5')
time.sleep(1)
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')


while True:
    #sim humberto, eu sei do isdigit(), mas nao vou usar.

    linha = (input('Em que linha você quer atacar?'))
    if linha not in numfabeto:
        print('Isso não é uma linha valida')
        continue
    linha = int(linha) ; linha = linha -1
    if linha > size:
        print('Isso esta fora do mapa chefinho')
        continue
    coluna = input('Em que coluna queres atacar? ')
    if coluna not in alfabeto and coluna not in alfabeto.lower():
        print('Isso não é uma linha valida')
        continue

    coluna = coluna.upper()

    if (alfabeto.index(coluna)) > size - 1:
        print('Isso esta fora do mapa chefinho')
        continue
    coluna = alfabeto.index(coluna)

    if robo[linha][coluna] == W:
        print('ERRRRRRRROUUUUUUUUUUUUUUUUU')
        robo[linha][coluna] = C
    elif robo[linha][coluna] == T:
        print('KABBBBBBBBBBBOOOOOOOOOOOOOOOOOOOMMMMMMMM!!!!!!')
        robo[linha][coluna] = X
    elif robo[linha][coluna] == C or robo[linha][coluna] == X:
        resposta = input('Esse lugar ja foi atingido Chefinho, tem certeza que quer atacar ai?  [S/N]')
        resposta = resposta.upper()
        if resposta == 'N':
            continue
        else:
            print(print('ERRRRRRRROUUUUUUUUUUUUUUUUU'))

    formatador(robo, humano)
    print('O computador esta calculando a sua proxima jogada...')
    time.sleep(2)


    linha = random.randrange(size)
    coluna = random.randrange(size)
    if humano[linha][coluna] == C or humano[linha][coluna] == X:
        while humano[linha][coluna] == C or humano[linha][coluna] == X:
            linha = random.randrange(size)
            coluna = random.randrange(size)
    if humano[linha][coluna] == W:
        print('ERRRRRRRROUUUUUUUUUUUUUUUUU')
        humano[linha][coluna] = C
    elif humano[linha][coluna] == N:
        print('KABBBBBBBBBBBOOOOOOOOOOOOOOOOOOOMMMMMMMM!!!!!!')
        humano[linha][coluna] = X
    formatador(robo, humano)
    vencedor_humano = foi_derrotado_robo(robo)
    vencedor_robo = foi_derrotado_jogador(humano)
    if vencedor_humano:
        print('Ganhou!')
        break
    elif vencedor_robo:
        print('Perdeu lindu :) ')
        break
    else: continue
