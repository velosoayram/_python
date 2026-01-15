# Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
if n > 0:
    print(f'O antecessor de {n} é {n - 1}\n'
        f'O sucessor de {n} é {n + 1}\n')
elif n == 0:
    print(f'Não há antecessor para {n}\n'
        f'O sucessor de {n} é {n + 1}\n')
else:
    print(f'Não trabalhamos com números negativos')
