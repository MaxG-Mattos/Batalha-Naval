def posicao(string):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    maiusculo = string.upper()
    coluna = alfabeto.index(maiusculo[0])
    linha = int(maiusculo[1:])-1 #já que começa no 0
    return coluna, linha
# provavelmente seria uma boa ideia tacar uma condicional caso a entrada tenha mais de uma letra, tipo 'ab5'