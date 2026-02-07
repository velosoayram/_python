# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

listaP = []
listaI = []
print('| PARA PARAR, DIGITE -1 |')
while True:
    x = int(input('Valor: '))
    if x == -1:
        break
    elif x % 2 == 0:
        listaP.append(x)
    else:
        listaI.append(x)
print(f'LISTA: {sorted(listaP + listaI)}\n'
      f'PAR: {sorted(listaP)}\n'
      f'IMPAR: {sorted(listaI)}')
