soma = inter = cont = 0
result = []
janela = [21, 65, 3, 8, 2, 9, 6, 29]
intervalo = int(input())

for i in range(len(janela) - intervalo + 1):
    for j in range(intervalo):
        ind = i + j
        soma += janela[ind]
    result.append(soma)
    soma = 0
print(result)
