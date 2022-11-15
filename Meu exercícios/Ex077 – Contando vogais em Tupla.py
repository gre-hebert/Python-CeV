tupla = ('aprender', 'programar', 'linguaguem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for n in tupla:
    print(f'\nAs vogais da palavra {n.upper()} são: ', end='')
    for vogal in n:
        if vogal in 'aeiou':
            print(vogal, end=' ')
