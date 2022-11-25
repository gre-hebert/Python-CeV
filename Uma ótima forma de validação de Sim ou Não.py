while True:
    print('Olá, Mundo!')
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if continuar != 'S' and continuar != 'N':
            print('Opção Inválida!')
        else:
            break
    if continuar == 'N':
        break
print('Tchau, mundo!')

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
