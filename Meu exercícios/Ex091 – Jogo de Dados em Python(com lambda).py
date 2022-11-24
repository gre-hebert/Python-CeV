import time
import random
jogadores = dict()
for sequência in range(0, 4):
    jogadores[f'{sequência + 1}º Jogador'] = random.randint(1, 6)
for jogador, dado in jogadores.items():
    print(f'O {jogador} tirou {dado} no dado')
    time.sleep(1)
rank = sorted(jogadores.items(), key=lambda item:item[1], reverse=True)
print('-=' * 30)
print('  == RANKING DE JOGADORES ==')
for colocação, jogador_dado in enumerate(rank):
    print(f'Em {colocação + 1}º LUGAR: {jogador_dado[0]} com {jogador_dado[1]} no dado')
    time.sleep(1)

