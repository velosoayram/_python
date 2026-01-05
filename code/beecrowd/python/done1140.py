tautog = []
while True:
    frase = str(input()).title().split() # .title() 'iguala P = p' | .split() deve ser fora dos ().
    n = len(frase)
    valido = True
    if '*' in frase:
        break
    else:
        for a in range(n - 1):
            if frase[a][0] != frase[a + 1][0]:
                valido = False
                break # otimiza o código
        if valido:
            tautog.append('Y')
        if not valido:
            tautog.append('N')
        frase = []
for d in tautog:
    print(d)
