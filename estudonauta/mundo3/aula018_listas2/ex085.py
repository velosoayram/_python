# Exercício Python 085: Crie um programa onde o usuário possa digitar
# sete valores numéricos e cadastre-os numa lista única que mantenha
# separados os valores pares e ímpares. Mostre os valores pares e ímpares
# em ordem crescente.

# SOL 1: list comprehension
val = [int(input(f'Digite o {i+1}o valor: ')) for i in range(7)]
lista = [[p for p in val if p % 2 == 0], [i for i in val if i % 2 != 0]]
print(f'PARES: {sorted(lista[0])}')
print(f'IMPARES: {sorted(lista[1])}')

# SOL 2: basic form
x = [[], []]
while True:
    if len(x[0] + x[1]) >= 7:
        break
    else:
        r = int(input())
        if r % 2 == 0:
            x[0].append(r)
        else:
            x[1].append(r)
print(f'PARES: {sorted(x[0])}')
print(f'IMPARES: {sorted(x[1])}')
