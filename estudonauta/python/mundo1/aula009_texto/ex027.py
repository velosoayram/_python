# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome: ')).strip().split()
print(f'Seu primeiro nome é {nome[0]}.\n'
      f'Já o seu último é {nome[-1]}.')
