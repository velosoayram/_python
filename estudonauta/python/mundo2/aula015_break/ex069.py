# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior = homem = mulher = 0
while True:
    idad = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
    if idad < 20 and sexo == 'F':
        mulher += 1
    if idad > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    r = str(input('Deseja continuar? | [S/N]: ')).strip().upper()
    while r not in ['S', 'N']:
        r = str(input('Inválido | [S/N]: ')).strip().upper()
    if r == 'N':
        break
print(f'\nA quantidade de homens cadastrados é {homem}.\nA quantidade de mulheres menores de 20 anos é {mulher}.\nAgora {maior} pessoa(s) são maior(es) de idade.')
