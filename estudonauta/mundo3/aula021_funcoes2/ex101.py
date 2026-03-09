# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import datetime

def voto(x):
    idade = datetime.now().year - x
    if idade < 16:
        return '\033[32mNEGADO\033[m'
    elif 16 < idade < 18:
        return '\033[33mOPCIONAL\033[m'
    else:
        return '\033[31mOBRIGATÓRIO\033[m'


nasc = int(input('EM QUE ANO NASCEU? '))
sit = voto(nasc)
print(f'SUA SITUAÇÃO: VOTO {sit} PARA AS ELEIÇÕES')
