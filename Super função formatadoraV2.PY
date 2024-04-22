import random
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
escolha = input('Você quer escolher o país do computador? S/N') #aqui o jogador diz se ele quer escolher o país do computador ou não
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

robo = cria_mapa(10)
humano = cria_mapa2(10)
# agora que a gente tem nossas matrizes, estaq na hora de rodar o nossa SUPPPPPPERR função formatadora.
#IMPORtANTE: Esse negocio só funciona se o tabuleiro for 10x10. Não achei em nenhum lugar falando que o tabuleiro podia ter outras dimenções. Então fiz só para 10x10 mesmo.


def formatador(robo, humano):
    #primeiro, A SUPPPPERRRR função imprime qual lado é o computador e qual é o Humano. 
    #Depois Ela imprime o ABCDEFGHIJ.
    #importante: Cada quadradinho na função é 3x1. Ou seja, um espaço vazio são 3 espaços, e um lugar cheio são 3 █

    print('                 COMPUUTADOR                                                           JOGADOR')
    print('    A   B   C   D   E   F   G   H   I   J','                         ','    A   B   C   D   E   F   G   H   I   J')
    #Agora vem a parte dificl. Não da para imprimir direro porque ficqa tudo cagado. tem que fazer linha a linha.  

    #menti, a parte dificil não é agora. 

    #O codigo Abaixo só serve para alinhar as coisas. Aparentemente o numero 10 é mais largo que os outros. Então precisa colocar uns espaços aleatorios para fazer os outros numeros ficarem com a mesma largura que o 10.
    for i in range(len(robo)):
        pos_reverso = i +1
        pos = i + 1
        pos = str(pos)
        if pos != '10':
            pos_reverso =  pos + ' '
            pos = ' ' + pos

        #agora sim é a parte dificil
        #Como eu ja disse, tem que fazer as coisas linha a linha, A primeira vista, seria só fazer print( numero linha[i], numero, espaço, numero linha[i], numero ). só que isso da errado, o negocio imprime tudo cagado tipo 
        #[' A ', ' A ', ' A ', ' A ', ' A ', ' A ', ' A ', ' A ', ' A ', ' A '], sendo que a gente quer
        #A   A   A   A   A   A   A   A   A   A
        #Para corrigir, por sorte pra caramba, eu descobri como acessar um valor de uma matriz em uma linha
        #nos exercicios de matriz , eu tentei fazer isso de todas as formas e falhei, só que agora por sorte eu consegui.
        #é só fazer assim: Matriz[linha][coluna]
        #é tao facil que me deixa com raiva. como que eu nao descobri isso antes??
        #acho que voce ja entendeu como que a proxima linha de codigo vai ser né? 
        #se voce nao entendeu, vou te explicar. Ela imprime o numero da coluna, e ai imprime 10 vezes o valor da coluna em uma linha. 
        


        #print(robo[i])
        print(pos,robo[i][0],robo[i][1],robo[i][2],robo[i][3],robo[i][4],robo[i][5],robo[i][6],robo[i][7],robo[i][8],robo[i][9],pos_reverso,'                     ',pos,humano[i][0],humano[i][1],humano[i][2],humano[i][3],humano[i][4],humano[i][5],humano[i][6],humano[i][7],humano[i][8],humano[i][9],i+1)
    #agora olha só que legal, é o alfabeto denovo.
    print('    A   B   C   D   E   F   G   H   I   J','                         ','    A   B   C   D   E   F   G   H   I   J')

#Eu não sabia que sava para usar função sem return até hoje. Que util. 
formatador(robo, humano)

#Como usar essa função? 
#depois de que todos os cauculos forem feitos, é só colocar a matriz atual do robo e do humano na função e ela vai imprimir direitinho.



