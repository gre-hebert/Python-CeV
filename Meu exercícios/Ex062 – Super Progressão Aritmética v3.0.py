num = int(input('Digite um número: '))
razão = int(input('Informe a razão da PA: '))
continuar = True
termos = 10
contador = 0
while continuar == True:
    print(num, end=' -> ')
    contador += 1
    num += razão
    termos -= 1
    if termos == 0:
        print('FIM')
        perguntar = True
        while perguntar == True:
            pergunta = str(input('Deseja continuar? [S/N]')).lower().strip()
            if pergunta == 's':
                termos = int(input('Mais quantos termos: '))
                perguntar = False
            elif pergunta == 'n':
                continuar = False
                perguntar = False
            else:
                print('Valor inválido, tente novamente.')
print('Um total de {} termos forma exibidos'.format(contador))
