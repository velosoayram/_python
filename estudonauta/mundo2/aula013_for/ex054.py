# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

cont1 = cont2 = 0
idades = []
for i in range(7):
    nasc = int(input(f'ANO DE NASCIMENTO ({i+1}° PESSOA): '))
    idade = date.today().year - nasc
    idades.append(idade)
for j in idades:
    if j >= 18:
        cont1 += 1
    else:
        cont2 += 1
print(f'{cont1} pessoas atingiram a maioridade.')
print(f'E {cont2} ainda não.')
