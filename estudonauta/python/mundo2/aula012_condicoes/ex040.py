# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

p1 = float(input('1° NOTA: '))
p2 = float(input('2° NOTA: '))
media = (p1+p2)/2
if media < 5:
    print(f'Sua média é {media} | Você está \033[31mreprovado\033[m.')
elif 5 < media < 6.9:
    print(f'Sua média é {media} | Você está em \033[93mrecuperação\033[m.')
else:
    print(f'Sua média é {media} | Você está \033[32maprovado\033[m.')
