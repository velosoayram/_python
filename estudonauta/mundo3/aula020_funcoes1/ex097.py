# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(x):
    y = len(x) + 2
    print(f'-'*y)
    print(f' {x}')
    print(f'-'*y)
    
w = str(input('DIGITE UMA FRASE: '))
escreva(w)
