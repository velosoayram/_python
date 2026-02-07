# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input('N1: ')), int(input('N2: ')),
       int(input('N3: ')), int(input('N4: ')))
print(f'O 9 apareceu {num.count(9)} vez(es).')
if 3 in num:
      print(f'O número 3 apareceu na {num.index(3)+1} posição.')
else:
      print('Não há número 3.')
print(f'Os números pares foram: ', end = '')
par = False   
for n in num:
    if n % 2 == 0:
        print(n, end = ' ')
        par = True
if not par:
     print(f'Não houve números pares.')     
