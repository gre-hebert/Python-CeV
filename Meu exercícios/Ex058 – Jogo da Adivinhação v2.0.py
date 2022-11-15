from random import randint
comp = randint(1, 10)
tentativas = 0
print('''Olá, o sou o seu computador
Eu acabei de pensar em um jogo de 1 a 10.''')
p1 = int(input('Gostaria de tentar advinhar? Dê o seu palpite: '))
tentativas += 1
while p1 != comp:
    if p1 < comp:
        p1 = int(input('Um pouco mais! Tente novamente: '))
        tentativas += 1
    else:
        p1 = int(input('Um pouco menos! Tente novamente: '))
        tentativas += 1
if tentativas == 1:
    print('WOW!!! Você muito bom!!! Parabéns conseguiu de primeira.')
else:
    print('Você coseguiu. Parabéns! Precisou de {} tentativas.'.format(tentativas))
