# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media = 0
velho = ''
vinte = 0
for i in range(4):
    if i == 0:
        x = 0
    nome = str(input(f'{i+1}° NOME: ')).strip().upper()
    idad = int(input(f'{i+1}° IDADE: '))
    media += idad
    sexo = str(input(f'{i+1}° SEXO: ')).strip().upper()
    if idad < 20 and sexo == 'F':
        vinte += 1
    elif sexo == 'M' and idad > x:
        velho = nome
        x = idad
print(f'A média da idade do grupo é {media/4:.0f} anos')
print(f'O nome do homem mais velho é {velho.capitalize()}')
print(f'{vinte} mulher(es) tem menos de 20 anos')
