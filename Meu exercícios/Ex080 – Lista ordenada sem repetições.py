lista = []
valor = int(input('Adicione um valor: '))
lista.append(valor)
print('Ele foi adicionado ao final da lista.')
valor = int(input('Adicione um valor: '))
if valor > lista[0]:
    lista.append(valor)
    print('Ele foi adicionado ao final da lista')
else:
    lista.insert(0, valor)
    print('Ele foi adicionado na posição 0')
valor = int(input('Adicione um valor: '))
if valor < lista[0]:
    lista.insert(0, valor)
    print('Ele foi adicionado na posição 0')
elif valor > lista[0] and valor < lista[1]:
    lista.insert(1, valor)
    print('Ele foi adicionada a posição 1')
else:
    lista.append(valor)
    print('Ele foi adicionado ao final da lista')
valor = int(input('Adicione um valor: '))
if valor < lista[0]:
    lista.insert(0, valor)
    print('Ele foi adicionado na posição 0')
elif lista[0] < valor < lista[1]:
    lista.insert(1, valor)
    print('Ele foi adicionado na posição 1')
elif lista[1] < valor < lista[2]:
    lista.insert(2, valor)
    print('Ele foi adicionado na posição 2')
else:
    lista.append(valor)
    print('Ele foi adicionado ao final da lista')
valor = int(input('Digite um número: '))
if valor < lista[0]:
    lista.insert(0, valor)
    print('Ele foi adicionado na posição 0')
elif lista[0] < valor < lista[1]:
    lista.insert(1, valor)
    print('Ele foi adicionado na posição 1')
elif lista[1] < valor < lista[2]:
    lista.insert(2, valor)
    print('Ele foi adicionado na posição 2')
elif lista[2] < valor < lista[3]:
    lista.insert(3, valor)
    print('Ele foi adicionado na posição 3')
else:
    lista.append(valor)
    print('Ele foi adicionado ao final da lista')
