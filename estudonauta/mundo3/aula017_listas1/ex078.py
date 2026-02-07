# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = [int(input(f'{i+1}o valor: ')) for i in range(5)]
print(f'O maior valor foi: {max(lista)} | POSIÇÕES: ', end = ' ')
for l in range(len(lista)):
    if lista[l] == max(lista):
        print(l, end = ' ')
print(f'\nO menor valor foi: {min(lista)} | POSIÇÕES: ', end = ' ')
for l in range(len(lista)):
    if lista[l] == min(lista):
        print(l, end = ' ')
