# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número: '))
print('TABELA DE CONVERSÃO\n'
      '| 1 - BINÁRIO\n| 2 - OCTAL\n| 3 - HEXADECIMAL')
s = int(input('Digite um número: '))
if s == 1:
    print(bin(n)[2:])
elif s == 2:
    print(oct(n)[2:])
elif s == 3:
    print(hex(n)[2:])
else:
    print('Número fora da tabela, tente novamente.')
