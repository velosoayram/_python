# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Você deseja a tabuada de qual número? Digite-o: '))
for i in range(10):
    print(f'{n} * {i+1} = {n*(i+1)}')
