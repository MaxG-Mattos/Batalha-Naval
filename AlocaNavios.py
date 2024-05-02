import random
def aloca_navios(mapa,listablocos):
    n = len(mapa)
    for blocos in listablocos:
        while True:
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(['h', 'v'])
            if posicao_suporta(mapa, blocos, linha, coluna, orientacao) == False:
                continue
            else:

                if orientacao == 'h':
                    for i in range(blocos):
                        mapa[linha][coluna] = 'N'
                        coluna += 1
                    break

                if orientacao == 'v':
                    for i in range(blocos):
                        mapa[linha][coluna] = 'N'
                        linha += 1
                    break
    return mapa
