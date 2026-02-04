# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

pt = int(input('Digite o 1° termo: '))
rz = int(input('Digite a razão da PA: '))
cont = 0
while cont < 10:
    print(pt, end = ' -> ')
    pt += rz
    cont += 1
print('FIM')
