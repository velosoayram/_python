par = list()
impar = list()
qtd = int(input())
for n in range(qtd):
    num = int(input())
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
lista = list()
par.sort()
for p in par:
    lista.append(p)
impar.sort(reverse = True)
for i in impar:
    lista.append(i)
for l in lista:
    print(l)