lista = list()
while True:
    h = maior = int(input())
    if h == 0:
        break
    else:
        while True:
            if h == 1:
                lista.append(maior)
                break
            if h % 2 == 0:
                h = h/2
            else:
                h = (h*3) + 1
                if h > maior:
                    maior = h
for m in lista:
    print(int(m))