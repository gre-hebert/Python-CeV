mae_lista = []
maior_peso = []
menor_peso = []
while True:
    pessoas = []
    pessoas.append(str(input('Nome: ')).strip().lower().capitalize())
    pessoas.append(float(input('Peso: ')))
    mae_lista.append(pessoas)
    if len(mae_lista) == 1:
        maior_peso.append(pessoas)
        menor_peso.append(pessoas)
    elif pessoas[1] > maior_peso[0][1]:
        maior_peso.clear()
        maior_peso.append(pessoas)
    elif pessoas[1] == maior_peso[0][1]:
        maior_peso.append(pessoas)
    elif pessoas[1] < menor_peso[0][1]:
        menor_peso.clear()
        menor_peso.append(pessoas)
    elif pessoas[1] == menor_peso[0][1]:
        menor_peso.append(pessoas)
    while True:
        resposta = str(input('Quer continuar: [S/N] ')).lower().strip()
        if resposta != 'n' and resposta != 's':
            print('\033[31mResposta inválida\033[m')
        else:
            break
    if resposta == 'n':
        break
print(f'{len(mae_lista)} pessoas foram cadastradas.')
print(f'O maior peso foi {maior_peso[0][1]} de',end=' ')
for cont in range(0, len(maior_peso)):
    print(f'{maior_peso[cont][0]}', end='... ')
print(f'\nO menor peso foi {menor_peso[0][1]} de',end=' ')
for cont in range(0, len(menor_peso)):
    print(f'{menor_peso[cont][0]}', end='... ')
