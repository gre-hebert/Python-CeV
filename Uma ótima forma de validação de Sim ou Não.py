while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if continuar != 'S' and continuar != 'N':
            print('Opção Inválida!')
        else:
            break