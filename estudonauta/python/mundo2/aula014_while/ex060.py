# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

n = int(input('Digite um número para obter seu fatorial: '))
x = 0
cont = n-1
fat = n * cont
while x != 1:
    cont += -1
    if cont > 0:
        fat *= cont
    else:
        x = 1
print(f'O resultado do fatorial é {fat}')
