# ex01:
def regressor(n):
    for i in range(n, -1, -1):
        print(i)
regressor(99)

print('-'*15)

# ex02:
def maior_lista(l):
    m = l[0]
    for i in l:
        if i > m:
            m = i
    return m
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(maior_lista(lista))
