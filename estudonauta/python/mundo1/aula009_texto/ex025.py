# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite seu nome: ')).strip().upper()
if 'SILVA' in nome:
    print('Que nome genérico...')
else:
    print(f'Prazer, {nome.title()}.')
