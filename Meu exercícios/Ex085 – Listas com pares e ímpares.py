lista = [[],[]]
for repetidor in range(0, 7):
    valor = int(input(f'Digite o {repetidor + 1}º valor: '))
    if valor % 2 == 0: # Par
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(f'Os valores pares digitado são {sorted(lista[0])} \ne os ímpares {sorted(lista[1])}')
