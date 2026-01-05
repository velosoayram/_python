# Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação num dicionário. No final, mostre o conteúdo
# da estrutura na tela.


sit = dict()
sit['nome'] = str(input('NOME: ').strip().upper())
sit['media'] = float(input('MÉDIA: '))
if sit['media'] < 6:
    situacao = 'REPROVADO'
else:
    situacao = 'APROVADO'
print(f'NOME: {sit['nome']}\n'
      f'MÉDIA: {sit['media']}\n'
      f'SITUAÇÃO: {situacao}')
