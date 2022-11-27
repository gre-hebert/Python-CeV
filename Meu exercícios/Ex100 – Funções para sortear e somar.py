from random import randint
import time
lista = list()
def sorteio():
    for repetição in range (0, 5):
        lista.append(randint(0, 9))
    print('Sorteando 5 valores da lista: ', end='')
    for valores in lista: 
         print(valores, end=' ')
         time.sleep(.3)
    print('PRONTO!')


def soma_par():
    soma = 0
    for valores in lista:
        if valores % 2 == 0:
            soma += valores
    print(f'Somando os valores pares de {lista}, temos {soma}')

sorteio()
soma_par()