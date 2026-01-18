# Exercício Python 089: Crie um programa que leia nome e
# duas notas de vários alunos e guarde tudo numa lista
# composta. No final, mostre um boletim contendo a média
# de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.

"""
lista = list()
qtd = int(input('QUANTOS ALUNOS A SEREM CADASTRADOS: '))
for a in range(qtd):
    temp = list()
    nome = str(input('NOME: '))
    temp.append(nome)
    temp.append(float(input('NOTA 1: ')))
    temp.append(float(input('NOTA 2: ')))
    lista.append(temp)
print('-_'*20)
for b in range(len(lista)):
    print(lista[b], f'MEDIA: {(lista[b][-2] + lista[b][-1])/2}')
print('_-'*20)
nome = input('MOSTRAR NOTAS DE QUAL ALUNO? ')
while True:
    if nome == -1:
        break
    for a in range(len(lista)):
        if lista[a][0] == nome:
            print(lista[a][-2], lista[a][-1])
    break
"""

# guanabara way:

lista = []
while True:
    nome = str(input('NOME: ')).strip().capitalize()
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    r = str(input('DESEJA CONTINUAR [S/N]: '))
    if r in 'Nn':
        break
for i, j in enumerate(lista):
    print(f'No.{i} | {j[0]} | MEDIA: {j[-1]:.1f}')
while True:
    opc = int(input('DESEJA VER A NOTA DE QUAL ALUNO? '))
    if opc == -1:
        break
    if opc <= len(lista) - 1:
        print(f'A NOTA DE \033[31m{lista[opc][0]}\033[m FOI {lista[opc][1]}')






