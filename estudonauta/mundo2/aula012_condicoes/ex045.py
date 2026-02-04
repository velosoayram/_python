# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

lista = ['PEDRA', 'PAPEL', 'TESOURA']
pc = randint(0, 2)
print('VAMOS JOGAR JO-KEN-PO!')
print('TABELA\n'
    ' 0 - PEDRA\n' 
    ' 1 - PAPEL\n' 
    ' 2 - TESOURA')
jg = int(input('Escolha sua jogada! Número: '))
if jg == pc:
    print(f'O PC escolheu, {lista[pc]} e você {lista[jg]}. \033[33mÉ empate\033[m!')
elif jg == 0 and pc == 1 or jg == 1 and pc == 2 or jg == 2 and pc == 0:
    print(f'O PC escolheu, {lista[pc]} e você {lista[jg]}. Você \033[31mperdeu\033[m!')
else:
    print(f'O PC escolheu, {lista[pc]} e você {lista[jg]}. Você \033[32mganhou\033[m!')
