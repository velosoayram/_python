# Exercício Python 085: Crie um programa onde o usuário possa digitar
# sete valores numéricos e cadastre-os numa lista única que mantenha
# separados os valores pares e ímpares. Mostre os valores pares e ímpares
# em ordem crescente.

def bubble_sort(l):
    n = len(l)
    for x in range(n):
        for y in range(n - x - 1):
            if l[y] > l[y + 1]:
                l[y], l[y + 1] = l[y + 1], l[y]
lista = list()
par = list()
impar = list()
for a in range(7):
    lista.append(int(input(f'DIGITE O {a + 1} VALOR: ')))
bubble_sort(lista)
for p in lista:
    if p % 2 == 0:
        par.append(p)
    else:
        impar.append(p)
print(f'OS PARES: {par}\n'
      f'OS IMPARES: {impar}')
