# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
 
# a) de 1 até 10, de 1 em  1 
# b) de 10 até 0, de 2 em 2 
# c) uma contagem personalizada

def contador(a, b, c):
    dist = a - b
    dist = -(dist-1) if dist < 0 else dist+1
    if a < b:
        for x in range(dist):
            print(a, end = ' ')
            a += c
            if a > b:
                break
    elif a > b:
        for x in range(dist):
            print(a, end = ' ')
            a -= c
            if a < b:
                break
    print()


contador(1, 10, 1)
contador(10, 0, 2)
contador(27, 56, 3)
