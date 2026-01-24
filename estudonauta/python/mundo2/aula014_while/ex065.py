# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

r = ''
soma = cont = maior = menor = 0
while r != 'N':
    n = int(input('Digite um número: '))
    if cont == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont += 1
    soma += n
    r = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while r not in ('S', 'N'):
        r = str(input('Digite uma resposta válida. [S/N]: ')).strip().upper()
print(f'Você digitou {cont} número(s). A média entre eles é {soma/cont:.1f}.\n'
      f'O maior número lido foi {maior}, já o menor foi {menor}.')
