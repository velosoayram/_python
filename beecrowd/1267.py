resp = []
while True:
    linha = input().split()
    if not linha:
        break
    N, D = map(int, linha)
    part = []
    if N == D == 0:
        break
    for _ in range(D):
        part.append(input().split())
    encontrou_aluno = False
    for alumni_index in range(N):
        participou_de_todos = True
        for jantar_participacao in part:
            if jantar_participacao[alumni_index] == '0':
                participou_de_todos = False
                break
        if participou_de_todos == True:
            encontrou_aluno = True
            break
    if encontrou_aluno == True:
        resp.append('yes')
    else:
        resp.append('no')
for resultado in resp:
    print(resultado)


"""
resp = []
while True:
    val = True
    aluno, jantar = map(int, input().split())
    part = []
    if aluno == jantar == 0:
        break
    for a in range(aluno):
        x = str(input())
        part.append(x)
    for b in range(jantar):
        temp = []
        for c in range(len(part)):
            temp.append(part[c][b])
        if '0' not in temp:
            answer = 'yes'
            resp.append(answer)
            val =  True

            break
        else:
            val = False
    if not val:
        answer = 'no'
        resp.append(answer)
for i in resp:
    print(i)
"""