# Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

item = input('Digite algo: ')
print(f'O tipo primitivo desses caracteres é: {type(item)}')

print(f'Número: {item.isnumeric()}\n'
      f'Alfabético: {item.isalpha()}\n'
      f'Alfanumérico: {item.isalnum()}\n'
      f'Caixa alta: {item.isupper()}\n'
      f'Caixa baixa: {item.islower()}\n'
      f'Capitalizado: {item.istitle()}\n'
      f'Espaço: {item.isspace()}')
