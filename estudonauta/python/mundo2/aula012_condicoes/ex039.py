# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Informe seu ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    print(f'Aguarde, ainda falta(m) {18 - idade} ano(s) para seu alistamento.')
elif idade == 18:
    print('É a hora, aliste-se já.')
elif idade > 18:
    print(f'Você está atrasado {idade - 18} ano(s). Vá à junta militar mais próxima resolver suas pendências.')
