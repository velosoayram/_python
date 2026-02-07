# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

qtd = int(input('CADASTRO | QTD DE PESSOAS: '))
boletim = []
for i in range(qtd):
    nome = str(input('NOME: ')).strip().title()
    n1 = float(input('NOTA 1: '))
    n2 = float(input('NOTA 2: '))
    media = round((n1 + n2)/2, 2)
    temp = [[nome], [n1], [n2], [media]]
    boletim.append(temp)
for j in range(len(boletim)):
    print(f'ALUNO {j} | {boletim[j]}')
while True:
    x = int(input('DESEJA ACESSAR INDIVIDUALMENTE QUAL ALUNO? DIGITE SEU CODIGO: '))
    if x < 0:
        break
    print(boletim[x])
