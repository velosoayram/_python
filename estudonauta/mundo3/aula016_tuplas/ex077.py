# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

pal = ('Inefavel', 'Proton', 'Nebulosa', 'Catarse', 'Sinfonia',
            'Paradoxo', 'Alento', 'Vertice', 'Impeto', 'Mantra', 'Zefiro',
            'Solsticio', 'Amago', 'Caleidoscopio')
print('CATADOR DE VOGAIS')
for p in range(len(pal)):
    print(f'Na palavra {pal[p]:.<15} temos: ', end='')
    for p0 in pal[p]:
        if p0 in 'AEIOUaeiou':
            print(f'\033[33m{p0.lower()}\033[m', end=' ')
    print()
