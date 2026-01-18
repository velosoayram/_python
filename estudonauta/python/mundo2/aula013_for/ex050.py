# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

lista = []
soma = 0
for i in range(6):
    lista.append(int(input(f'Digite o {i+1}° valor: ')))
for j in lista:
    if j % 2 == 0:
        soma += j
print(f'A soma dos seu números, que são pares, é {soma}.')
