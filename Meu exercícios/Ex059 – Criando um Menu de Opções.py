from time import sleep
número_1 = int(input('Digite o primeiro número: '))
número_2 = int(input('Digite o segundo número: '))
escolha = ''

while escolha != 5:
    print('''
>>>>Escolha uma das oções:
    [1] Somar
    [2] Multiplicar
    [3] Exibir o Maior
    [4] Novos números
    [5] Sair''')
    escolha = int(input('>>>>Qual a sua escolha: '))
    if escolha < 1 or escolha > 5:
        resp = 'Opção inválida, tente novamente'
        print('')
        print('-' * len(resp))
        print(resp)
        print('-' * len(resp))
        sleep(1)
    elif escolha == 1:
        resp = 'A soma de {} e {} é {}.'.format(número_1, número_2, número_1 + número_2)
        print('')
        print('-' * len(resp))
        print(resp)
        print('-' * len(resp))
        sleep(1)
    elif escolha == 2:
        resp = 'A multiplicação de {} e {} é {}.'.format(número_1, número_2, número_1 * número_2)
        print('')
        print('-' * len(resp))
        print(resp)
        print('-' * len(resp))
        sleep(1)
    elif escolha == 3:
        if número_1 == número_2:
            resp = 'Não há número maior, os dois número são iguais.'
            print('')
            print('-' * len(resp))
            print(resp)
            print('-' * len(resp))
            sleep(1)
        elif número_1 > número_2:
            resp = '{} é maior que o {}, portanto {} é o número maior'.format(número_1, número_2, número_1)
            print('')
            print('-' * len(resp))
            print(resp)
            print('-' * len(resp))
            sleep(1)
        else:
            resp = '{} é maior que o {}, portanto {} é o número maior'.format(número_2, número_1, número_2)
            print('')
            print('-' * len(resp))
            print(resp)
            print('-' * len(resp))
            sleep(1)
    elif escolha == 4:
        resp = 'Ok, digite os numeros novamente!'
        print('')
        print('-' * len(resp))
        print(resp)
        número_1 = int(input('Digite o primeiro número: '))
        número_2 = int(input('Digite o segundo número: '))
        sleep(1)
print('Finalizando, por favor, aguarde', end='')
sleep(0.5)
for ponto in range (1,4):
    print('.', end='')
    sleep(0.5)
print('Finalizado!!! Volte sempre.')