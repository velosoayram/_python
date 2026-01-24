# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('SEXO(M/F): ')).strip().upper()
while sexo not in ['M', 'F']:
        print('Digite um sexo válido.')
        sexo = str(input('SEXO(M/F): ')).strip().upper()
if sexo == 'M':
    print('Seu sexo é Masculino.')
elif sexo == 'F':
    print('Seu sexo é Feminino.')
