dicionário = dict()
dicionário['nome'] = str(input('Nome: ')).strip().lower().capitalize()
gols = list()
for jogos in range(0, int(input(f'Quantos jogos {dicionário["nome"]} jogou? '))):
    gols.append(int(input(f'     Quantos gols na partda {jogos}? ')))
dicionário['gols'] = gols
dicionário['total'] = sum(gols)
print('-=' * 30)
print(dicionário)
print('-=' * 30)
for keys, values in dicionário.items():
    print(f'O campo {keys} tem o valor {values}')
print('-=' * 30)
print(f'O jogador {dicionário["nome"]} jogou {len(gols)} partidas')
for partida, gol in enumerate(gols):
    print(f'    => Na partida {partida}, fez {gol} gols.')
print(f'Foi um total de {dicionário["total"]} gols')
