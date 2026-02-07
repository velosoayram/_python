# Exercício Python 088: Faça um programa que ajude um jogador da "MEGA-SENA" a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
# para cada jogo, cadastrando tudo numa lista composta.

from random import randint

x = 1
jogos = []
qtd = int(input('Qual a quantidade de jogos? '))
for q in range(qtd): 
    palp = [randint(1, 60) for i in range(6)]
    jogos.append(palp)
for r in jogos:
    print(f'JOGO {x:<3}: ', end='')
    print(' - '.join((f'[{str(s):^4}]') for s in r))
    x += 1
