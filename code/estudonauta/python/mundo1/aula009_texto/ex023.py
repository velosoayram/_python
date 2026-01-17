# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Digite um número de 0 a 9999: '))
print(f'Unidade: {num//1%10}\n'
      f'Dezena: {num//10%10}\n'
      f'Centena: {num//100%10}\n'
      f'Milhar: {num//1000%10}')
