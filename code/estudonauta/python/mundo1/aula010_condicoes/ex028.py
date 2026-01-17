# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu. 

from random import randint

cont = 0
num = randint(0, 5)
print('Hey, eu pensei num número de 0 a 5, tente adivinhar qual!')
while True:
    resp = int(input('Chute: '))
    cont += 1
    if resp != num:
        print('Tente novamente.')
    elif resp == num and cont == 1:
        print('Parabéns! Você acertou de primeira!')
    elif resp == num:
        print(f'Acertou, mas precisou de {cont} tentativas.')
