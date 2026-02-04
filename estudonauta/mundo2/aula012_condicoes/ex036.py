# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Digite o valor da casa: R$ '))
sal = float(input('Digite o valor do salário: R$ '))
anos = int(input('Digite em quantos anos irá pagar: '))
prest = casa/(anos*12)
if prest <= (sal * 30/100):
    print(f'Seu empréstimo foi concedido em {anos*12} parcelas de R$ {prest:.2f}')
else:
    print(f'Seu empréstimo foi negado, pois as parcelas de R$ {prest:.2f} excedem 30% do seu salário.')
