# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

a = float(input('Digite a medida da reta A: '))
b = float(input('Digite a medida da reta B: '))
c = float(input('Digite a medida da reta C: '))
if a + b > c and a + c > b and c + b > a:
    print('É possível formar um triângulo!')
    if a == b == c:
        print('Ele será EQUILÁTERO.')
    elif a != b != c:
        print('Ele será ESCALENO.')
    else:
        print('Ele será ISÓSCELES.')
else:
    print('Não dá para formar um triângulo!')
