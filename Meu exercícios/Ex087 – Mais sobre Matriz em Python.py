matriz = [[],[],[]]
soma_pares = soma_3_linha = maior_2_linha = 0
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
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        if coluna == 2:
            soma_3_linha += matriz[linha][coluna]
        if linha == 1 and matriz[linha][coluna] > maior_2_linha:
            maior_2_linha = matriz[linha][coluna]
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print(f'\nOs valores pares são {soma_pares}')
print(f'A soma da terceira coluna é {soma_3_linha}')
print(f'O maior valor da segunda linha foi {maior_2_linha}')