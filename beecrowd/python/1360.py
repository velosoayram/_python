# H < C < D < S (Copas, Paus, Ouros, Espadas)
# 1 < 2 < ... < 9 < T < J < Q < K











































"""
cont = 1
seq = []
fix = []
result = []
qtd = int(input())
for i in range(qtd):
    c1, c2, c3, c4 = map(str, input().split())
    result.append(c1[-1])
    seq.append(c2 and c3 and c4)
    for j in range(len(seq) - cont):
        cont += 1
        if seq[j][0] == seq[j + 1][0] == seq[j + 2][0]:
            fix.append(seq[j][0])
        elif seq[j][0] == seq[j + 1][0]:
            fix.append(seq[j][0])
        elif seq[j][0] == seq[j + 2][0]:
            fix.append(seq[j][0])
        elif seq[j + 1][0] == seq[j + 2][0]:
            fix.append(seq[j + 1][0])
    fix.sort()
    if c1 < c2 < c3:
        result.insert(fix[0] + 1)
    if c1 < c3 < c2:
        result.insert(fix[0] + 2)
    if c2 < c1 < c3:
        result.insert(fix[0] + 3)
    if c2 < c3 < c1:
        result.insert(fix[0] + 4)
    if c3 < c1 < c2:
        result.insert(fix[0] + 5)
    if c3 < c2 < c1:
        result.insert(fix[0] + 6)
    print(result[0])
    result = []
"""
