# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 'Bahia', 'São Paulo', 'Grêmio', 'RB Bragantino', 'Atlético-MG', 'Santos', 'Corinthians', 'Vasco', 'Vitória', 'Internacional', 'Ceará', 'Fortaleza', 'Juventude', 'Sport')

print(f'OS CINCO PRIMEIROS: {times[:6]}\n'
      f'OS 4 ULTIMOS: {times[-4:]}\n'
      f'EM ORDEM ALFABETICA: {sorted(times)}\n'
      f'CORINTHIANS: {times.index('Corinthians')}')
