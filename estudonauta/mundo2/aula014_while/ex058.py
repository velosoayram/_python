# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
cont = 0

print('PC: Hm, olá.')
sleep(0.5)
print('.')
sleep(0.5)
print('.')
sleep(0.5)
print('.')
sleep(0.5)
print('PC: Pensei, em um número de 0 a 10, tente adivinhá-lo.')
pc = randint(0, 10)
resposta = int(input('Digite sua resposta: '))
while resposta != pc:
    cont += 1
    print('PC: Errou, tente novamente.')
    resposta = int(input('Nova tentativa: '))
if resposta == pc:
    print(f"Você acertou. Precisou de {cont} tentativa(s).")
