# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal 
# 3x ou mais no cartão: 20% de juros

val = float(input('Informe o valor do produto: R$ '))
print('- TABELA -\n 1 - À VISTA (DINHEIRO/CHEQUE)\n 2 - À VISTA (CARTÃO)\n 3 - ATÉ 2x (CARTÃO)\n 4 - 3x ou mais (CARTÃO)')
res = int(input('Informe a forma de pagamento pelo número da tabela: '))
if res == 1:
    print(f'Você irá receber 10% de desconto, o preço final é de: R$ {val - (val*10/100):.2f}')
elif res == 2:
    print(f'Você irá receber 5% de desconto, o preço final é de: R$ {val - (val*5/100):.2f}')
elif res == 3:
    print(f'São duas parcelas de R$ {val/2:.2f}')
elif res == 4:
    x = int(input('Deseja pagar em quantas vezes? '))
    print(f'Ao escolher {x} parcelas, você deverá pagar R$ {(val + (val * 20/100))/x:.2f} ao mês.')
