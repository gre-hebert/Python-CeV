from random import choice
n0 = str(input('Primeiro aluno: '))
n1 = str(input('Segundo aluno: '))
n2 = str(input('Terceiro aluno: '))
n3 = str(input('Quarto aluno: '))
lista = [n0, n1, n2, n3]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))