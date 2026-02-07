# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3
# e preencha com valores lidos pelo teclado. Mostre a matriz na tela.

matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for m in range(len(matriz)):
    for n in range(len(matriz)):
        matriz[m][n] = int(input(f'VALOR [{m},{n}]: '))
for l in range(len(matriz)):
    for c in range(len(matriz[0])):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()
