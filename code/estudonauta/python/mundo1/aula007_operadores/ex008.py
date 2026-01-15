# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite uma medida: '))
print(f'{n}m correspondem a {n*100:.0f}cm e a {n*1000:.0f}mm.')
