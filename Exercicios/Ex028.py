from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador pensar em um número de 0 a 5.
print('-=-' *20)
print('Vou pensar em um número entre 0  e 5. Tente advinhar...')
print('-=-' *20)
jogador = int(input('Em que número eu pensei? ')) # O jogador tentar advinhar o número
print('PROCESSANDO...')
sleep(1.5)
if jogador == computador:
    print('Parabéns! Você coseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
