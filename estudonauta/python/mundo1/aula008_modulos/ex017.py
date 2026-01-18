# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
print(f'Sua hipotenusa possui {math.hypot(ca, co):.2f}u')
