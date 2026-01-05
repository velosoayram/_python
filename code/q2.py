def obtem_oracoes(nome_arq):

    resposta = []
    cont = 0

    with open(nome_arq, 'r', encoding='utf-8') as arquivo:
        x = arquivo.read()
        oracoes = x.split('.')
        for i in oracoes:
            inicio = []
            fim = []
            if i == oracoes[0]:
                inicio.append(0)
                fim.append(len(i[cont]))
                cont += 1
                indice = (inicio, fim)
            else:
                inicio.append(len(i[cont - 1] + 2))
                fim.append(len(i[cont]))
                cont += 1
                indice = (inicio, fim)
            resposta.append([oracoes[cont], indice])
    return resposta