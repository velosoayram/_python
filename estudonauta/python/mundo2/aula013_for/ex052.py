# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

cont = 0
n = int(input('Digite um inteiro: '))
print()
for i in range(1, n+1):
    if n % i == 0:
        cont += 1
        print(f'\033[32m{i}\033[m', end = ' ')
    else:
        print(f'\033[31m{i}\033[m', end = ' ')
print('\n')
if cont != 2:
    print(f'O número {n} \033[33mnão é primo\033[m.')
else:
    print(f'O número {n} \033[33mé primo\033[m.')
