# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius*1.8) + 32
kelvin = celsius + 273.15
print(f'Sua tempertura Celsius {celsius} oC:\n'
      f'Fahrenheit: {fahrenheit} oF\n'
      f'Kelvin: {kelvin} K')
