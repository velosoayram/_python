# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado
# e tenham resultados aleatórios. Guarde esses resultados num dicionário
# em Python. No final, coloque esse dicionário em ordem, sabendo que o
# vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter

players = {'p1': randint(1, 6), 'p2': randint(1, 6), 'p3': randint(1, 6), 'p4': randint(1, 6)}
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)            # package use
ranking = sorted(players.items(), key=lambda item: item[1], reverse=True)     # lambda function

for k, v in enumerate(ranking):
    print(f'{k+1} | O {v[0]} TIROU {v[1]} NO DADO.')
