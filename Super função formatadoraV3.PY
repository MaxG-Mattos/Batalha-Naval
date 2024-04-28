import random
import random
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
        Linha = [' A ']*(N)
        final.append(Linha)
    return final

def cria_mapa2(N):
    final = []
    for _ in range(N):
        Linha = [' █ ']*(N)
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
    print('  ',espaco,'COMPUTADOR  ',espaco,'                           ',espaco,'JOGADOR')
    print(AbcPrint,'                       ',AbcPrint)
 
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
        print(pos,RoboPrint,pos_reverso,'                     ',pos,HumanoPrint,i+1)

    print(AbcPrint,'                       ',AbcPrint)
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
if escolha_de_dimensao == 'N':
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
humano = cria_mapa2(size)
navios = frotas(jogador, computador)
navios_computador = navios[1] 
navios_jogador = navios[0]
bloco_navio_pc = []
for n in navios_computador:
    bloco_navio_pc.append(bloco_por_navio[n])
robo = aloca_navios(robo, bloco_navio_pc)
formatador(robo, humano)