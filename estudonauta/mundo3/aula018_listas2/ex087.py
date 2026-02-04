# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

"""
matriz = [[], [], []]
soma1 = soma2 = maior = 0
for linha in range(3):
    for coluna in range(3):
        num = int(input(f'VALOR [{linha}, {coluna}]: '))
        matriz[linha].append(num)
        if num % 2 == 0:
            soma1 += num
        if coluna == 2:
            soma2 += num
        if linha == 1:
            if num > maior:
                maior = num
for a in matriz:
    print(a)
print(f'SOMA DOS PARES: {soma1}\n'
      f'SOMA DA TERCEIRA COLUNA: {soma2}\n'
      f'MAIOR VALOR DA SEGUNDA LINHA: {maior}')
"""

# guanabara way:

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pa = c3 = maior = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'DIGITE O VALOR [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            pa += matriz[l][c]
        if matriz[l][2]:
            c3 += matriz[l][2]
        maior = matriz[1][0]
        if matriz[1][c] > maior:
            maior = matriz[1][c]
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^9}]', end='')
    print()
print(f'SOMA DOS PARES: {pa}\n'
      f'SOMA DA TERCEIRA COLUNA: {c3}\n'
      f'MAIOR VALOR DA SEGUNDA LINHA: {maior}')
