# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = [int(input(f'Digite o {i+1}o valor: ')) for i in range(5)]
for j in range(len(lista)):
    for k in range(len(lista) - j - 1):
        if lista[k] > lista[k + 1]:
            lista[k], lista[k + 1] = lista[k + 1], lista[k]
print(lista)
