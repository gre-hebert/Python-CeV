matriz = [[],[],[]]
for repetidor in range(0, 9):
    if repetidor < 3:
        valor = int(input(f'Digite o {repetidor + 1}º valor da primeira linha: '))
        matriz[0].append(valor)
    elif repetidor < 6:
        valor = int(input(f'Digite o {repetidor - 2}º valor da segunda linha: '))
        matriz[1].append(valor)
    else:
        valor = int(input(f'Digite o {repetidor - 5}º valor da terceira linha: '))
        matriz[2].append(valor)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
