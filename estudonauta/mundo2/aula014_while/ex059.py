# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
print('\n[ 1 ] somar\n'
'[ 2 ] multiplicar\n'
'[ 3 ] maior\n'
'[ 4 ] novos números\n'
'[ 5 ] sair do programa\n')
op = int(input('O que deseja fazer? Digite um número: '))
while op != 5:
    if op == 1:
        print(f'O resultado é {v1+v2}')
    elif op == 2:
        print(f'O resultado é {v1*v2}')
    elif op == 3:
        print(v1 if v1>v2 else v2 if v1<v2 else 'Ambos são iguais.')
    elif op == 4:
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    else:
        print('Essa opcão é inválida, tente novamente.')
    op = int(input('O que deseja fazer? Digite um número: '))
print('Fim do programa.')
