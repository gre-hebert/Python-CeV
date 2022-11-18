lista = []
par_lista = list()
impar_lista = []
while True:
    número = int(input('Digite um número: '))
    lista.append(número)
    if número % 2 == 0:
        par_lista.append(número)
    else:
        impar_lista.append(número)
    while True:
        resposta = str(input('Quer continuar: [S/N] ')).lower().strip()
        if resposta != 's' and resposta != 'n':
            print('Opção inválida! Digite "\033[32mS\033[m" para \033[32mSim\033[m e "\033[31mN\033[m" para \033[31mNão\033[m.')
        else:
            break
    if resposta == 'n':
        break
print(f'O números foram: {lista}\nOs números pares foram: {par_lista}\nOs números impar foram{impar_lista}')
