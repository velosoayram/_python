# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%. 

sal = float(input('Digite o valo do seu salário: R$ '))
aumento = 0
if sal <= 1250:
    print(f'Seu salário irá receber um aumento de 15%, agora valendo R$ {sal + (sal*15/100):.2f}')
else:
    print(f'Seu salário irá receber um aumento de 10%, agora valendo R$ {sal + (sal*10/100):.2f}')
    