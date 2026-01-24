# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint


cont = 0
while True:
    PC = randint(0, 10)
    n = int(input('Qual numero deseja escolher? [0 a 10]: '))
    opc = str(input('PAR ou ÍMPAR? [P/I]: ')).strip().upper()
    if opc == 'P':
        if (n+PC) % 2 == 0:
            print(f'Você ganhou! O PC escolheu {PC} e você {n}')
            cont += 1
        else:
            print(f'Você perdeu! O PC escolheu {PC} e você {n}')
            break
    elif opc == 'I':
        if (n+PC) % 2 == 0:
            print(f'Você perdeu! O PC escolheu {PC} e você {n}')
            break
        else:
            print(f'Você ganhou! O PC escolheu {PC} e você {n}')
            cont += 1
print(f'Manteve {cont} vitórias consecutiva(s).')
