# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite a sua frase: ')).strip().upper()
frase = ''.join(frase.split())
print(frase)
palin = ''
for i in range(len(frase) -1, -1, -1):
    palin += frase[i]
print(palin)
if palin == frase:
    print(f'"{frase}" / é um palíndromo.')
else:
    print(f'"{frase}" / não é um palíndromo.')
