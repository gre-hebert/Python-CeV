palavras = ('aprender', 'programar', 'linguaguem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

vogais = ('a', 'e', 'i', 'o', 'u')

#For para todas as palavras
for contador1 in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[contador1]} temos: ', end='')
    #For para cada letra
    for contador2 in range(0, len(palavras[contador1])):

        for contador3 in range(0, len(vogais)):
            if vogais[contador3] in palavras[contador1][contador2]:
                print(vogais[contador3], end=' ')