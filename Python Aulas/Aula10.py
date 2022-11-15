from curses import init_pair


nome = str(input('Digite seu nome: '))
if nome == 'Gustavo':
    print('Que nome bonito, {}.'.format(nome))
print('Prazer em te conhecer!')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2
print('A média da suas notas é {}.'.format(média))
if média >= 7:
    print('APROVADO')
else:
    print('REPROVADO')

vel = float(input('Qual a velocidade? '))
print('MULTADO' if vel > 70 else 'Tudo certo!')