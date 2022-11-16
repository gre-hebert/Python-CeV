lista = list()
while True:
    novo_número = int(input('Digite um valor: '))
    if novo_número in lista:
        print('Valor duplicado não pode ser adicionado')
    else:
        lista.append(novo_número)
    pergunta = str(input('Quer continuar: [Digite "N" para PARAR] ')).lower().strip()
    if pergunta == 'n':
        break
print(f'Os valores digitado foram {sorted(lista)}')
