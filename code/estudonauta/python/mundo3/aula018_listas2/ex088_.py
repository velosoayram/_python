# Exercício Python 088: Faça um programa que ajude um jogador da "MEGA-SENA" a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
# para cada jogo, cadastrando tudo numa lista composta.

"""
from random import randint
from time import sleep
jogo = list()
randint(1, 60)
v = int(input('QUANTOS PALPITES DESEJA? '))
for a in range(v):
    for b in range(6):
        if b == 0:
            num = randint(1, 60)
            jogo.append(num)
        else:
            num = randint(1, 60)
            if num in jogo:
                while num in jogo:
                    num = randint(1, 60)
            if num not in jogo:
                jogo.append(num)
    for c1 in range(len(jogo)):
        for c2 in range(len(jogo) - 1 - c1):
            if jogo[c2] > jogo[c2 + 1]:
                jogo[c2], jogo[c2 + 1] = jogo[c2 + 1], jogo[c2]
    print(f'JOGO {a + 1}: {jogo}')
    sleep(1)
    jogo = []
    """

# guanabara way:

def bubble(l):
    qtd = len(l)
    for a in range(qtd):
        for b in range(qtd - a - 1):
            if l[b] > l[b + 1]:
                l[b], l[b + 1] = l[b + 1], l[b]

from random import randint
lista = []
jogos = []
count = 0
vezes = int(input('QUANTOS PALPITES? '))
for times in range(vezes):
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            count += 1
        if count == 6:
            bubble(lista)
            jogos.append(lista[:])
            lista = []
            count = 0
            break
for i, l in enumerate(jogos):
    print(f'JOGO {i + 1}: {l}')
