from math import radians
from operator import imod
from random import randint
from time import sleep
comp = randint(1, 3) # O computador vai pensar de 1 até 3
play = int(input('Eu vou pensar em um número, de 1 até 3!\nTente advinhar, qual número eu pensei? ')) # Aqui valor o valor do jogador
print('PROCESSANDO...')
sleep(1.3)
if comp == play:
    print('UAU! você acertou, eu pensei no {}!'.format(comp))
else:
    print('Você errou, eu pensei no {} e não no {}!'.format(comp, play))