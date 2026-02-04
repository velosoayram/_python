# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

barato = ''
cont = total = m1000 = menor = 0
while True:
    prodt = str(input('PRODUTO: '))
    preco = float(input('PREÇO: '))
    total += preco
    if preco > 1000:
        m1000 += 1
    if cont == 0:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            barato = prodt
    cont += 1
    r = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if r == 'N':
        break
print(f'O total gasto foi R$ {total:.2f} | A quantidade de produtos que custam mais de R$ 1.000 é {m1000} | O produto mais barato é {barato.upper()}.')
