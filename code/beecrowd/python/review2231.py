result = []
while True:
    Q, J = map(int, input().split())
    if Q == J == 0:
        break
    else:
        temp = []
        for q in range(Q): # registra as temperaturas
            temp.append(int(input()))
        soma = 0
        for j in range(J): # itera sobre o primeiro intervalo
            soma += temp[j]
        media = (soma/J)
        maior = menor = media
        for a in range(1, Q - J + 1): # itera sobre os demais intervalos
            ultimo = temp[a - 1]
            proximo = temp[a + J - 1]
            soma = soma - ultimo + proximo
            media = soma / J
            if media > maior:
                maior = media
            if media < menor:
                menor = media
        medias = [menor, maior]
        result.append(medias)
for m in range(len(result)):
    print(f'Teste {m+1}\n'
          f'{int(result[m][0])} {int(result[m][-1])}')
    print()



# WRONG ANSWER 20%:
"""cont1 = soma = 0
result = list()
media = list()
ultimo = list()
while True:
    N, D = map(int, input().split())
    if N == D == 0:
        break
    else:
        temperaturas = []
        for qtd in range(N):
            tem = int(input())
            temperaturas.append(tem)
            if N % 2 != 0:
                ultimo.append(tem)
        for t in temperaturas:
            soma += t
            cont1 += 1
            if cont1 == D:
                result.append(f'{int(soma/D)}')
                soma = 0
                cont1 = 0
                if N % 2 != 0 and len(ultimo) == N:
                    for u in reversed(ultimo):
                        soma += u
                        cont1 += 1
                        if cont1 == D:
                            result.append(f'{int(soma/D)}')
                            ultimo = []
                            break
        media.append(result)
        result = []
for test in range(len(media)):
    print(f'Teste {test + 1}')
    for num in media[test]:
        print(num, end=' ')
    print('\n')
"""