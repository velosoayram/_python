# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

banco = float(input('Quantos reais você têm? R$: '))
compra = banco/5.39
print(f'Você pode comprar U$ {compra:.2f}')
