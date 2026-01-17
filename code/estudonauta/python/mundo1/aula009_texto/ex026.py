# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite qualquer frase: ')).lower().strip()
qtd = frase.count('a')
print(f'Sua frase possui {qtd} "a(s)".\n'
      f'O primeiro "a" aparece na posição {frase.find('a')+1}.\n'
      f'último "a" aparece na posição {frase.rfind('a')+1}.')
