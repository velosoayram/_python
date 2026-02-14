# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia(l1):
    for i in range(5):
        l1.append(randint(1, 10))
    print(f'OS NÚMEROS SORTEADOS FORAM:\n{l1}')
    
def somaPar(l2):
    soma = 0
    for valor in l2:
        if valor % 2 == 0:
            soma += valor
    print(f'A SOMA DOS VALORES PARES DOS NUMEROS SORTEADOS É: \033[36m{soma}\033[m')
    return l2


lista = list()
sorteia(lista)
somaPar(lista)
