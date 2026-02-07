# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

maior = soma1 = soma2 = 0
matriz = [[0 for x in range(3)] for x in range(3)]
for l in range(len(matriz)):
    for c in range(len(matriz[0])):
        r = int(input(f'VALOR [{l}, {c}]: '))
        if r % 2 == 0:
            soma1 += r
        if c == 2:
            soma2 += r
        if l == 1:
            if r > maior:
                maior = r
        matriz[l][c] = r
for l in range(len(matriz)):
    print('-'.join([f'[{matriz[l][c]:^5}]' for c in range(len(matriz))]))
print(f'SOMA DOS PARES: {soma1}')
print(f'SOMA DA TERCEIRA COLUNA: {soma2}')
print(f'MAIOR DA SEGUNDA LINHA: {maior}')
