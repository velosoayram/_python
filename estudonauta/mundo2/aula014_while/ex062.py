# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

r = pt = int(input('Digite o 1° termo: '))
rz = int(input('Digite a razão da PA: '))
cont = 0
lim = 10
while r != 0:
    print(pt, end = ' -> ')
    pt += rz
    cont += 1
    if cont == lim:
        r = int(input('\nDeseja ver mais quantos termos? '))
        lim = r
        cont = 0
print('FIM')
