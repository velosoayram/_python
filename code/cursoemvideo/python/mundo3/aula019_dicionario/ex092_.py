# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e
# carteira de trabalho e cadastre-o (com idade) num dicionário. Se por acaso
# a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação
# e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai
# se aposentar.

ano = 2025

ficha = dict()
ficha['nome'] = str(input('NOME: '))
x = int(input('DATA DE NASC: '))
ficha['ctps'] = int(input('CTPS: '))
ficha['idade'] = ano - x
if ficha['ctps'] != 0:
    ficha['contratacao'] = int(input('ANO DE CONTRATAÇÃO: '))
    ficha['salário'] = int(input('SALÁRIO: '))
    ficha['aposentadoria'] =  (35 - (ano - ficha['contratacao'])) + ficha['idade']
print('-'*20)
for k, v in ficha.items():
    print(f'{k} -> {v}')
print('-'*20)