# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3
# e preencha com valores lidos pelo teclado. Mostre a matriz na tela.

"""
linha1 = list()
linha2 = list()
linha3 = list()
while True:
    for a in range(3):
        linha1.append(int(input(f'DIGITE O VALOR [0, {a}]: ')))
    for b in range(3):
        linha2.append(int(input(f'DIGITE O VALOR [1, {b}]: ')))
    for c in range(3):
        linha3.append(int(input(f'DIGITE O VALOR [2, {c}]: ')))
    break
print(linha1)
print(linha2)
print(linha3)
"""

# guanabara way:

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input())
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^9}]', end='')
    print()

