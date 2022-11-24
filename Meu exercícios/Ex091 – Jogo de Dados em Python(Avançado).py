from random import randint
from time import sleep
print('~' * 50)
print(f'{"SUPER MEGA ULTRA BLASTER JOGO DE DADO":^50}')
print('~' * 50)
sleep(3)
print('     Cada jogador vai jogar 2d6, ou seja, 2 dados de 6 lados')
sleep(3)
print('BOA SORTE!!!')
sleep(1)
print('Que o primeiro jogaador comece!!!')
sleep(2)
Jogadores = dict()
for repetição in range (0, 4):
    Jogadores[f'{repetição + 1}p'] = {'1d6': randint(1,6), '2d6': randint(1 , 6)}
    Jogadores[f'{repetição + 1}p']['soma'] = Jogadores[f'{repetição + 1}p']['1d6'] + Jogadores[f'{repetição + 1}p']['2d6']
for P, dados in Jogadores.items():
    print(f'O {P} jogou o primeiro dado.')
    sleep(1)
    print(f'Caiu {dados["1d6"]}')
    sleep(1)
    print('Jogou o segundo dado.')
    sleep(1)
    print(f'Caiu {dados["2d6"]}')
    sleep(1)
    print(f'Total: {dados["soma"]}')
    sleep(1)
    if Jogadores[P]['soma'] == 12:
        print('INCRÍVEL!!!')
    elif Jogadores[P]['soma'] == 11:
        print('Muito bom!')
    elif Jogadores[P]['soma'] == 2:
        print('QUE JOGADA HORRÍVEL!!!')
    print('-' * 27)
    sleep(2)
rank = sorted(Jogadores.items(), key=lambda item:item[1]['soma'], reverse=True)
print('~' * 50)
print(f'{"RANKING DOS MELHORES MAIS BEM COLOCADOS":^50}')
print('~' * 50)
sleep(3)
for colocação, dado in enumerate(rank):
    print(f'{colocação + 1}º LUGAR: {dado[0]} com {dado[1]["soma"]}pts')
    sleep(1)