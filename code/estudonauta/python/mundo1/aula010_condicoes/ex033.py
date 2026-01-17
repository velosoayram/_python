# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
lista = [n1, n2, n3]
print(f'O maior número é: {max(lista)}\n'
      f'O menor número é: {min(lista)}')
