from random import randint  
from time import sleep
jogos = int(input('Quantos jogos você deseja? '))
print('-=' * 30)
for quantidade in range(0, jogos):
    mega_sena = []
    while True:
        número = randint(1, 60)
        if número not in mega_sena:
            mega_sena.append(número)
        if len(mega_sena) == 6:
            print(f'{quantidade + 1}º jogo para MEGA SENA: {mega_sena}')
            sleep(0.5)
            break
