# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(b, h):
    a = b * h
    print(f'A área de um terreno {b} x {h} é de {a:.2f} m2')


base = float(input('VALOR DA BASE: '))
height = float(input('VALOR DA ALTURA: '))
area(base, height)
