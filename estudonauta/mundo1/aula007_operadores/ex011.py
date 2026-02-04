# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

alt = float(input('Digite a altura: '))
lar = float(input('Digite a largura: '))
tinta = (alt*lar)/2
print(f'Será necessário {tinta:.4f}L de tinta para {alt*lar}m2.')
