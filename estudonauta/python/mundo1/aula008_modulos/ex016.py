# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
num = float(input('Digite um número real: '))
print(f'A parte inteira do seu número é {trunc(num)}')
