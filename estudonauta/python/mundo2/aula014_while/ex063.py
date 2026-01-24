# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

# 0 – 1 – 1 – 2 – 3 – 5 – 8

cont = 0
x, y = 0, 1
n = int(input('Digite um número: '))
while cont < n:
    if cont == n - 1:
        print(x, end = '')
        cont += 1
    else:
        print(x, end = ' - ')
        x, y = y, x + y
        cont += 1
