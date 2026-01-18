# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

pt = int(input('Digite o primeiro termo da sua PA: '))
rz = int(input('Digite a razão da sua PA: '))
for i in range(pt, pt+(10*rz), rz):
    print(i, end = ' -> ')
print('FIM')
