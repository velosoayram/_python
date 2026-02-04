# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


n = int(input('Deseja sacar qual valor? R$ '))
c50 = n // 50
resto = n % 50
c20 = resto // 20
resto %= 20
c10 = resto // 10
resto %= 10
c01 = resto // 1
print(f'C50: {c50}\n'
      f'C20: {c20}\n'
      f'C10: {c10}\n'
      f'C01: {c01}')
