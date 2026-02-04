# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Digite a medida da reta A: '))
b = float(input('Digite a medida da reta B: '))
c = float(input('Digite a medida da reta C: '))
if a + b > c and a + c > b and c + b > a:
    print('É possível formar um triângulo!')
else:
    print('Não dá para formar um triângulo!')
