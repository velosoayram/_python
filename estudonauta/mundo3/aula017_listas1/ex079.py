# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
flag = True
while flag:
    x = int(input('Digite um valor numérico (negativos interrompem): '))
    if x in lista:
        pass
    elif x < 0:
        break
    else:
        lista.append(x)
print(sorted(lista))
