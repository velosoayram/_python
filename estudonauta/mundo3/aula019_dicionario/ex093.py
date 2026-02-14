# Exercício Python 093: Crie um programa que gerencie o aproveitamento
# de um jogador de futebol. O programa vai ler o nome do jogador e quantas
# partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado num dicionário, incluindo o total de gols
# feitos durante o campeonato.

jogador = {'NOME': str(input('NOME: ')).strip().title()}
x = int(input(f'Quantas partidas {jogador['NOME']} jogou? '))
gol = [int(input(f'Gols feitos na partida {i+1}: ')) for i in range(x)]
y = sum(gol)
jogador['GOLS'] = gol[:]
jogador['TOTAL'] = y
print()
print(jogador)
print()
for j, k in jogador.items():
    print(f'{j} | {k}')
print()
print(f'O jogador {jogador["NOME"]} fez {jogador["TOTAL"]} gols.')
for l, m in enumerate(jogador['GOLS']):
    print(f'Na partida {l+1} -> {m}')
