matriz= []
linhas = []
colunas = []
L, C = map(int, input().split())
for l in range(L): # matriz
    num = str(input()).split()
    temp = []
    soma_li = 0
    for li in num: # soma das linhas
        temp.append(int(li))
        soma_li += int(li)
    matriz.append(temp)
    linhas.append([(soma_li), temp])
for co in range(C): # soma das colunas
    temp = []
    soma_co = 0
    for li in range(len(matriz)):
        temp.append(matriz[li][co])
        soma_co += matriz[li][co]
    colunas.append([(soma_co), temp])
linhas.sort(key=lambda item: item[0], reverse=True)
colunas.sort(key=lambda item: item[0], reverse=True)
if linhas[0][0] > colunas[0][0]:
    print(linhas[0][0])
else:
    print(colunas[0][0])
