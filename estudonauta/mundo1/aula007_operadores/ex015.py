# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite quantos quilometros foram percorridos: '))
dd = int(input('Digite por quantos dias você o alugou: '))
print(f'Você terá de pagar R$ {((60*dd) + (0.15*km)):.2f}. A soma do preço do KM (R$ {60*dd:.2f}) e dos dias (R${0.15*km:.2f}).')
