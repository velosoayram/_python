# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

n1 = int(input('Digite o n1: '))
n2 = int(input('Digite o n2: '))
if n1 > n2:
    print('O \033[31mprimeiro\033[m valor é maior.')
elif n2 > n1:
    print('O \033[31msegundo\033[m valor é maior.')
elif n1 == n2:
    print('Ambos valores são iguais.')
