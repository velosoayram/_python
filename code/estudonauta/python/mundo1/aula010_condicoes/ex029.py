# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite. 

vel = int(input('Digite a sua velocidade em Km/H: '))
if vel <= 80:
    print('Ótimo, dentro do limite de velocidade.')
else:
    multa = (vel - 80)*7
    print(f'Você excedeu o limite de velocidade em {multa/7:.0f} Km/H, e deverá pagar R$ {multa:.2f} em multa.')
