from time import sleep
from random import randint
def sorteio(valores):
    print('Analisando os valores passados...')
    sleep(1)
    for indices, números in enumerate(valores):
        print(números, end=" ")
        sleep(.5)
    print(f'Foram informados {len(valores)} valores ao todo.\nO maior valor informado foi {max(valores)}')
    print('-=' * 30)

while True:
    lista = list()
    for repetição in range(0, randint(1, 10)):
        lista.append(randint(0, 9))
    sorteio(lista)
    while True:
        pergunta = str(input('Quer continuar: [S/N] ')).strip().lower()
        if pergunta == 's' or pergunta == 'n':
            break
        print('Digite "S" para SIM e "N" para NÃO')
    if pergunta == 'n':
        break
print('\n  <<  FINALIZADO  >>')