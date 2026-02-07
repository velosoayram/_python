# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    x = int(input('Adicione números | (Flag: negativos): '))
    if x < 0:
        break
    else:
        lista.append(x)
print(f'{len(lista)} números adicionados.\n'
      f'Lista de valores decrescentes: {sorted(lista, reverse=True)}')
print(f'O valor cinco \033[35mestá\033[m na lista.' if 5 in lista else 'O valor cinco \033[31mnao está\033[m na lista.')
