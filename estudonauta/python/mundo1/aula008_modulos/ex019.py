# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import randint
list = ('Carlos', 'Eduardo', 'Heitor', 'Fabrício')
x = randint(0, 3)
print(f'A pessoa sorteada foi {list[x]}!')
