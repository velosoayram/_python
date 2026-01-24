# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.


cont = 1
while True:
    n = int(input('Deseja a tabuada de qual número? '))
    if n < 0:
        print('Fim do programa.')
        break
    else:
        while cont < 11:
            print(f'{n} * {cont} = {n*cont}')
            cont += 1
    cont = 1
