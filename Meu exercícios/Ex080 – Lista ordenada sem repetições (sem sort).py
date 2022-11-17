lista = []
for pergunta in range (0,5):
    valor = int(input('Digite um valor: '))
    if pergunta == 0:
        lista.append(valor)
        print('O primeiro valor foi inserido')
    else: 
        for posição, valor_lista in enumerate(lista):
            if valor < valor_lista:
                lista.insert(posição, valor)
                print(f'Ele foi inserido na posição {posição}.')
                break
        else:
            lista.append(valor)
            print('Ele foi inserido na ultima posição.')
print('-=' * 30)
print(f'Os números inseridos foram: {lista}')
