from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
if jogador != 0 and jogador != 1 and jogador !=2:
    print('OPÇÃO INVÁLIDA')
else:
    print('JO', end='')
    sleep(0.5)
    print('KEN', end='')
    sleep(0.5)
    print('POOO!!!')
    sleep(0.5)
    print('Computador jogou {}'.format(itens[computador]))
    sleep(0.65)
    print('E você jogou {}'.format(itens[jogador]))
    sleep(1)
    print('-=-' * 5)
    if computador == 0:
        if jogador == 0:
            print('Você \033[34mEMPATOU\033[m!!!')
        elif jogador == 1:
            print('Você \033[32mGANHOU\033[m!!!')
        elif jogador == 2:
            print('Você \033[31mPERDEU\033[m!!!')    
    elif computador == 1:
        if jogador == 0:
            print('Você \033[31mPERDEU\033[m!!!')
        elif jogador == 1:
            print('Você \033[34mEMPATOU\033[m!!!')
        elif jogador == 2:
            print('Você \033[32mGANHOU!\033[m!!')
    elif computador == 2:
        if jogador == 0:
            print('Você \033[32mGANHOU\033[m!!!')
        elif jogador == 1:
            print('Você \033[31mPERDEU\033[m!!!')
        elif jogador == 2:
            print('Você \033[34mEMPATOU\033[m!!!')
print('-=-' * 5)
