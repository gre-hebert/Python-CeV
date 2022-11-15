from random import randint
from time import sleep
vitórias = 0
while True:
    while True:
        impar_ou_par = str(input('Você quer impar ou par? ')).strip().lower()
        if impar_ou_par == 'impar' or impar_ou_par == 'par':
            if impar_ou_par == 'impar':
                escolha_player = 'impar'
                escolha_comp = 'par'
            else:
                escolha_player = 'par'
                escolha_comp = 'impar'
            print(f'Ok, então fica com {escolha_player.upper()} e o computador com {escolha_comp.upper()}.')
            break
        else:
            print('Por favor. Digite corretamente para processegui.')
    print('Pronto?!')
    sleep(1.25)
    print('IM', end='')
    sleep(1)
    print('PAR, ', end='')
    sleep(1)
    print('PAR!!!')
    num = int(input('Qual número você joga? '))
    comp = randint(1, 10)
    if (num + comp) % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'impar'
    if resultado == escolha_player:
        print(f'Você jogou {num} e o computador jogou {comp}, deu {num + comp}, {num + comp} é {resultado}. VOCÊ GANHOU!!!')
        vitórias +=  1
    else:
        print(f'Você jogou {num} e o computador jogou {comp}, deu {num + comp}, {num + comp} é {resultado}. VOCÊ PERDEU!!!')
        break
if vitórias == 0:
    print('Você não conceguiu ganhar nenhuma vez. Mais sorte na próxima.')
elif vitórias == 1:
    print('Você ganhou 1 vez. Parabéns')
elif vitórias > 1:
    print(f'Você ganhou {vitórias} vezes. PARABÉNS!!!')
    