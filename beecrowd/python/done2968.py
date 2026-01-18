from math import ceil
voltas, placas = map(int, input().split())
total = voltas * placas
progresso = []
for i in range(1, 10):
    progresso.append(f'{ceil((total * i/10))}')
print(' '.join(progresso))
