# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

hei = float(input('Informe sua altura: (cm) '))
wei = float(input('Informe seu peso: (KG) '))
imc = wei/((hei/100)**2)
if imc < 18.5:
    print(f'SUBNUTRIDO | {imc:.2f}')
elif 18.5 < imc < 25:
    print(f'PESO IDEAL | {imc:.2f}')
elif 25 < imc < 30:
    print(f'SOBREPESO | {imc:.2f}')
elif 30 < imc < 40:
    print(f'OBESIDADE | {imc:.2f}')
else:
    print(f'OBESIDADE MÓRBIDA | {imc:.2f}')
