# Exercício Python 094: Crie um programa que leia nome, sexo e idade
# de várias pessoas, guardando os dados de cada pessoa num dicionário
# e todos os dicionários numa lista. No final, mostre:

# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

soma = 0
mulh = []
idad = []
todos = []
qtd = int(input('QTD DE PESSOAS A CADASTRAR: '))
for p in range(qtd):
    pess = {'nome': str(input('NOME: ').upper().strip()),
            'sexo': str((input('SEXO [M/F]: ')).upper().strip()),
            'idade': int(input('IDADE: '))}
    if pess['sexo'] == 'F':
        mulh.append(pess['nome'])
    soma += pess['idade']
    todos.append(pess.copy())
media = (soma/qtd)
for a in todos:
    if a['idade'] > media:
        idad.append([a['nome'], a['idade']])
print(f'PESSOAS CADASTRADAS  | {qtd}\n'
      f'MEDIA DA IDADE       | {media:.2f}\n'
      f'MULHERES CADASTRADAS | {mulh}\n'
      f'ACIMA DA MEDIA       | {idad}')
