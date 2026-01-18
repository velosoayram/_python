# Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

a = int(input('Digite um valor: '))
b = int(input('Digite até onde vai sua tabuada: '))
for nums in range(b):
    print(f'{a} * {nums + 1} = {a * (nums + 1)}')
