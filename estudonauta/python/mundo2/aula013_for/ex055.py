# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesos = []
for i in range(5):
    p = float(input(f'PESO {i+1}°: (KG) '))
    pesos.append(p)
print(f'O maior peso lido foi {max(pesos):.2f} KG')
print(f'O menor peso lido foi {min(pesos):.2f} KG')
