# Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação num dicionário. No final, mostre o conteúdo
# da estrutura na tela.


aluno = dict()
aluno['nome'] = str(input('NOME: ')).strip().title()
aluno['media'] = float(input('MEDIA: '))
if aluno['media'] >= 6:
    aluno['situacao'] = 'APROVADO(A)'
elif 4 < aluno['media'] < 6:
    aluno['situacao'] = 'RECUPERACAO'
else:
    aluno['situacao'] = 'REPROVADO'
for k, v in aluno.items():
    print(f'{k} = {v}')
