temp = []
C, V = map(int, input().split())
for c in range(C):
    t = str(input()).split()
    soma = 0
    for t in t:
        soma += int(t)
    temp.append([(c+1), soma])

temp.sort(key=lambda item: item[1]) # tira o bubblesort

for podio in range(3):
    print(temp[podio][0])

"""for t in range(len(temp)):
    for u in range(len(temp) - 1 - t):
        if temp[u][-1] > temp[u+1][-1]:
            (temp[u][0], temp[u][-1]), (temp[u+1][0], temp[u+1][-1]) = (temp[u+1][0], temp[u+1][-1]), (temp[u][0], temp[u][-1])"""