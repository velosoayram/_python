# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e
# carteira de trabalho e cadastre-o (com idade) num dicionário. Se por acaso
# a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação
# e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai
# se aposentar.

from datetime import datetime

info = {'NOME': str(input('NOME: ')).strip().upper(), 'NASC': int(input('ANO DE NASC: '))}
ctps = int(input('POSSUI CLT? (0 - NAO  POSSUI): '))
if ctps == 0:
    info['IDADE'] = (datetime.now().year - info['NASC'])
    info['CLT'] = 'INEXISTENTE'
else:
    info['IDADE'] = (datetime.now().year - info['NASC'])
    info['CLT'] = 'EXISTENTE'
    info['CONTRATACAO'] = int(input('ANO DE CONTRATACAO: '))
    info['SALARIO'] = float(input('SALARIO: R$'))
    info['APOSENTADORIA'] = (65 - (datetime.now().year - info['CONTRATACAO']))
for k, v in info.items():
    print(f'{k:.<20} | {v}')
