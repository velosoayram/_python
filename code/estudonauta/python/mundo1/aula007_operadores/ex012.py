# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço: R$ '))
desconto = preco - (preco * 5/100)
print(f'Com o desconto de 5% o valor é R$ {desconto:.2f}')
