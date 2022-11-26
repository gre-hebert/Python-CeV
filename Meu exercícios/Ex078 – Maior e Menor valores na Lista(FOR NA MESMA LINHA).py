lista = [int(input(f'Digite um valor na posição {c}: ')) for c in range (0,5)]
print(f'Os valores digitados foram{lista}')
print(f'O menor valor foi {min(lista)} nas posições', end=' ')
for n in range(0, len(lista)):
    if min(lista) == lista[n]:
        print(lista.index(min(lista), n), end='... ')
print(f'\nO maior valor foi {max(lista)} nas posições', end=' ')
for n in range(0, len(lista)):
    if max(lista) == lista[n]:
        print(lista.index(max(lista), n), end='... ')