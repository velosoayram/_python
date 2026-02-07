# Exercício Python 084: Faça um programa que leia nome e peso
# de várias pessoas, guardando tudo numa lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

listaG = []
listaP = []
maior = menor = 0
r = int(input('DESEJA CADASTRAR QUANATAS PESSOAS? '))
pessoas = [[(input('NOME: ')), int(input('PESO: '))] for i in range(r)]
for j in range(len(pessoas)):
    if j == 0:
        maior = menor = pessoas[j][-1]
    elif pessoas[j][-1] >= maior:
        maior = pessoas[j][-1]
    elif pessoas[j][-1] <= menor:
        menor = pessoas[j][-1]
for k in pessoas:
    if maior == k[-1]:
        listaG.append(k[0])
    if menor == k[-1]:
        listaP.append(k[0])
print(f'Ao todo, {len(pessoas)} foram pessoas cadastradas.')
print(f'O maior peso: {maior} KG | {listaG}')
print(f'O menor peso: {menor} KG | {listaP}')
