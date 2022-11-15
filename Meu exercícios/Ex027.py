nome = str(input('Digite seu nome: ')).strip()
nomes = nome.split()
print('Olá, prazer em te conhecer.\nSeu primeiro nome é {}.\nSeu último nome é {}.'.format(nomes[0], nomes[len(nomes) -1]))