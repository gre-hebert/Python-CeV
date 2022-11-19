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