lista = list()
casos = int(input())
for qtd in range(casos):
    r = str(input()).split()
    r.sort(key=len, reverse = True)
    lista.append(' '.join(r))
for frase in lista:
    print(frase)
