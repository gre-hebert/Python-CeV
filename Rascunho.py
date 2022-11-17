lista = []
for perguntar in range(0, 5):
    valor = int(input('Insira um valor: '))
    if perguntar == 0:
        list.append(valor)
        print('Primeiro valor adicionado')
    else:
        
        if valor < list[0]:
            lista.insert(0, valor)
        else:
            lista.append(valor)
            print('O valor foi adicionado na última posição.')