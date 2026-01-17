# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = (str(input('Digite o nome da sua cidade: '))).strip().upper()
primeiro = cidade.split()
if 'SANTO' in primeiro[0]:
    print('A cidade é santa!')
else:
    print('Belo nome!')
