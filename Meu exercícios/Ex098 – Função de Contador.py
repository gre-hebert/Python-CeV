from time import sleep
def contagem(inicio, fim, passo):
    print('-=' * 20)
    if passo < 0:
        passo -= passo * 2
    print(f'Contagem de {inicio} até {fim} em {passo} em {passo}')
    if passo == 0:
        passo = 1
    if inicio > fim and passo > 0:
        passo = -passo
        for repitir in range(inicio, fim - 1, passo):
            print(repitir, end=' ')
            sleep(0.38)
    else:
        for repitir in range(inicio, fim + 1, passo):
            print(repitir, end=' ')
            sleep(0.38)
    print('FIM!')


contagem(1, 10, 1)
contagem(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
contagem(int(input('Início: ')), int(input('FIM: ')), int(input('Passo: ')))