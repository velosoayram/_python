# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

ang = float(input('Digite o ângulo: '))
print(f'Do ângulo {ang:.0f}°\n'
      f'Sen: {sin(radians(ang)):.2f}\n'
      f'Cos: {cos(radians(ang)):.2f}\n'
      f'Tan: {tan(radians(ang)):.2f}')
