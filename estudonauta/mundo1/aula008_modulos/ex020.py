# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
lista = []
x = int(input('Quantos alunos serão sorteados? Escreva: '))
print('Agora, diga seus nomes: ')
for a in range(x):
    lista.append(str(input(f'Aluno {a+1}: ')))
shuffle(lista)
print(f'A ordem dos sorteados foi: {lista}')
