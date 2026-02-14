# Exercício Python 095: Aprimore o desafio 93 para que
# ele funcione com vários jogadores, incluindo um sistema
# de visualização de detalhes do aproveitamento de cada jogador.

gols = []
jogadores = []
while True:
    jogador = {'nome': str(input('NOME: ')).strip().title()}
    qtd = int(input('QTD PARTIDAS JOGADAS: '))
    for q in range(qtd):
        gols.append(int(input(f'QUANTOS GOLS NA {q+1}No PARTIDA? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    gols.clear()
    jogadores.append(jogador)
    r = str(input('DESEJA CONTINUAR? [S/N]: ')).strip().upper()
    while r not in 'SN':
        r = str(input('DESEJA CONTINUAR? [S/N]: ')).strip().upper()
    if r == 'N':
        break
for x in jogadores:
    print(f'{jogadores.index(x):<2} | {x['nome']:<15} | {str(x['gols']):<20} | {x['total']}')
while True:
    lev = int(input('DESEJA VER OS DADOS DE QUAL JOGADOR? '))
    if lev < 0:
        break
    if lev > len(jogadores):
        print('JOGADOR INEXISTENTE, REPITA O VALOR CORRETO.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {jogadores[lev]['nome']}')
        for a, b in enumerate(jogadores[lev]['gols']):
            print(f'JOGO {a+1}: {b} gols')
print('FIM DO PROGRAMA')
