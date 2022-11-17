lista = list()
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    while True:
        pergunta = str(input('Quer continuar? [S/N] ')).lower().strip()
        if pergunta != 's' and pergunta != 'n':
            print('Opcão invalida')
        else:
            break
    if pergunta == 'n':
        break
if len(lista) > 1:
    print(f'Você digitou {len(lista)} elementos.')
    lista.sort(reverse=True)
    print(f'Os valores em ordem decrecescente são: {lista}')
    if lista.count(5) > 0:
        print('O valor 5 faz parte da lista!')
    else:
        print('O valor 5 não aparece na lista!')

else:
    print('Você digitou apenas um elemento.')
    print(f'O valor digitado foi {lista[0]}')