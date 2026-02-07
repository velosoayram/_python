# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

contA = contB = 0
exp = str(input('Digite uma expressão matemática: '))
for i in exp:
    if i == '(':
        contA += 1
    elif i == ')':
        contB += 1
if contA == contB:
    print(f'Sua expressão {exp} \033[32mestá correta!\033[m')
else:
    print(f'Sua expressão {exp} \033[31mestá incorreta!\033[m')
