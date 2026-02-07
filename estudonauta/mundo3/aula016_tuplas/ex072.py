# Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    r = int(input('Digite algum número de 0 a 20: '))
    if 0 <= r <= 20:
        break
    else:
        print('Erro, digite novamente ')
print(f'Seu número por extenso: \033[31m{num[r]}\033[m')
