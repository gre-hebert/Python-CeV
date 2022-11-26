# Enumerate
lista = [1, 2, 3, 4, 5]
print(' Índices | Valores ')
for índice, valor in enumerate(lista):
    print(f'{índice:^9}|{valor:^9}')

# Usar dicionário dentro de lista
lista = [{'nome': 'Gnomo Gay', 'poder': 6, 'defesa': 4}, {'nome': 'Galinha Gorda', 'poder': 3, 'defesa': 7}, {'nome': 'Gnomo Hétero', 'poder': 4, 'defesa': 6}]
for x in lista:
    for a, b in x.items():
        print(a, b)
