def bubble(mat):
    emparelhadas = []
    matriz = []
    for linha in mat:
        soma = sum(linha)
        emparelhadas.append([soma, linha])
    n = len(emparelhadas)
    for a in range(n):
        for b in range(n - 1 - a):
            if emparelhadas[b][0] < emparelhadas[b + 1][0]:
                emparelhadas[b], emparelhadas[b + 1] = emparelhadas[b + 1], emparelhadas[b]
    for soma, linha in emparelhadas:
        matriz.append(linha)
    return matriz

valor = list()
matrizv1 = list()
linhas = int(input('QUANTIDADE DE LINHAS: '))
colunas = int(input('QUANTIDADE DE COLUNAS: '))
for l in range(linhas):
    for c in range(colunas):
        valor.append(int(input(f'DIGITE O VALOR DE [{l}, {c}]: ')))
    matrizv1.append(valor[:])
    valor = []

print('ORIGINAL')
for m in matrizv1:
    print(m)

matrizv2 = bubble(matrizv1)
print('ORDENADA')
for m in matrizv2:
    print(m)

