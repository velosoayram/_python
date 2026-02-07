# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

c1, c2, c3, c4, c5 = randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)
num = (c1, c2, c3, c4, c5)
print(f'Os nums gerados foram: {num}\n'
      f'O menor valor: {min(num)}\n'
      f'O maior valor: {max(num)}')
