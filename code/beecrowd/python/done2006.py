cont = 0
tipo = int(input())
A, B, C, D, E = map(int, input().split())
chutes = [A, B, C, D, E]
for i in chutes:
    if i == tipo:
        cont += 1
print(cont)