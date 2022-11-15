Zelda = ('The Legend of Zelda', 'The Adventure of Link ', 'A Link to the Past', "Link's Awakening", 'Ocarina of Time', "Majora's Mask",
'Oracle of Ages', 'Oracle of Seasons', 'Four Swords', 'The Wind Waker', 'Four Swords Adventures', 'The Minish Cap', 'Twilight Princess',
'Phantom Hourglass', 'Spirit Tracks', 'Skyward Sword', 'A Link Between', 'Tri Force Heroes', 'Breath of the Wild', 'Tears of the Kingdom')
print('Os primeiros jogos da franquia \33[32mThe Legend of Zelda\33[m foram:')
for cont in range(0, 5):
    if Zelda[cont] == 'The Legend of Zelda':
        print(f'{cont + 1}º {Zelda[cont]}')
    else:
        print(f'{cont + 1}º The Legend of Zelda: {Zelda[cont]}.')
print(f'\nOs ultimos 4 jogos lançados foram:')
for cont in range (-4, 0):
    print(f'The Legend of Zelda: {Zelda[cont]}')
print('\nOs jogos em ordem alfabética ficam:')
for cont in range(0, len(Zelda)):
    if sorted(Zelda)[cont][0] == sorted(Zelda)[cont - 1][0]:
        print(f'   {sorted(Zelda)[cont]}')
    else:
        print(f'{sorted(Zelda)[cont][0]}: {sorted(Zelda)[cont]}')
print('\nThe Legend of Zelda: Ocarina of Time foi o {}º jogo a ser lançado'.format(Zelda.index('Ocarina of Time') + 1))
