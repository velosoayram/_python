# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

n = int(input('Digite quantos produtos serão cadastrados: '))
prod = tuple((input(f'Nome do {i+1}º produto: '), float(input('Preço: R$ '))) for i in range(n))
for i in range(len(prod)):
    print(f'PDT: {prod[i][0]:.<30}R$ {prod[i][1]:.2f}')
