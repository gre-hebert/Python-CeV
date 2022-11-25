while True:
    print('Olá, mundo!')
    while True:
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if resposta == 'S' or resposta == 'N':
            break
        print('Erro')
    if resposta == 'N':
        break
print('Tchau, mundo!')
