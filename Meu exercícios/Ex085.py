lista = []
pares = []
impares = []
lista.append(pares)
lista.append(impares)
for repetidor in range(0, 7):
    valor = int(input(f'Digite o {repetidor + 1}º valor: '))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(f'Os valores pares foram {sorted(pares)} e o valores ímpares {sorted(impares)}')