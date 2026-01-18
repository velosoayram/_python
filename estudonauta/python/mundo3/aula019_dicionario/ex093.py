# Exercício Python 093: Crie um programa que gerencie o aproveitamento
# de um jogador de futebol. O programa vai ler o nome do jogador e quantas
# partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado num dicionário, incluindo o total de gols
# feitos durante o campeonato.


t = 0
gols = []
jogador = dict()
jogador['nome'] = str(input('NOME: '))
jogador['partidas'] = int(input('PARTIDAS: '))
qtd = jogador['partidas']
for a in range(qtd):
    t = int(input(f'{a + 1}o. PARTIDA | GOLS: '))
    gols.append(t)
    t += t
    print('-' * 20)
for k, v in jogador.items():
    print(f'{k} = {v}')
jogador['gols'] = gols[:]
jogador['golstot'] = t
print('-'*20)
print(jogador)
print('-'*20)