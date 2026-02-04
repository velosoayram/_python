# Exercício Python 084: Faça um programa que leia nome e peso
# de várias pessoas, guardando tudo numa lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

listan = list()
listap = list()
pmaior = list()
pmenor = list()
while True:
    listan.append(str(input('NOME: ')))
    listap.append(float(input('PESO: ')))
    r = input('CONTINUA [S/N]: ').upper()
    while r != 'S' and r != 'N':
        r = input('ERRO - [S/N]: ').upper()
    if r == 'N':
        break
maior = menor = listap[0]
for a in listap:
    if a > maior:
        maior = a
    if a < menor:
        menor = a
for cont in range(len(listap)):
    if listap[cont] == maior:
        pmaior.append(listan[cont])
    if listap[cont] == menor:
        pmenor.append(listan[cont])
print(f'{len(listan):.0f} PESSOA(S) CADASTRADA(S).\n'
      f'O maior peso foi {maior:.2f}KG / {pmaior}\n'
      f'O menor peso foi {menor:.2f}KG / {pmenor}')
