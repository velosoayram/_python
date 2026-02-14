# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*n):
    m = 0
    for num in range(len(n)):
        if num == 0:
            m = n[num]
        else:
            if n[num] > m:
                m = n[num]
    print(m)


maior(2, 9, 4, 5, 7, 1)
