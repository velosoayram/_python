# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado
# e tenham resultados aleatórios. Guarde esses resultados num dicionário
# em Python. No final, coloque esse dicionário em ordem, sabendo que o
# vencedor tirou o maior número no dado.

def bubble(l):
    n = len(l)
    for a in range(n):
        for b in range(n - 1 - a):
            if l[b] > l[b + 1]:
                l[b], l[b + 1] = l[b + 1], l[b]

from random import randint
from time import sleep


players = {'P1': randint(1, 6),
           'P2': randint(1, 6),
           'P3': randint(1, 6),
           'P4': randint(1, 6)}
ranking = {}
for k, v in players.items():
    print(f'  - {k} TIROU {v}')
ranking = sorted(players.items(), )