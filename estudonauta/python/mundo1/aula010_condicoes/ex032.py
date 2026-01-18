# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = int(input('Digite um ano para saber se ele é bissexto: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano {ano} é bissexto!')
elif ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto.')
