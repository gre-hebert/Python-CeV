time = list()
while True:
    jogador = dict()
    jogador['nome'] = str(input('Nome: ')).strip().lower().capitalize()
    gols = list()
    jogos = int(input(f'Quantos jogos {jogador["nome"]} jogou? '))
    for repetir in range(0, jogos):
        gols.append(int(input(f'Quantos gols no {repetir + 1}º jogo: ')))
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    time.append(jogador)
    while True:
        resposta = str(input('Quer continuar: [S/N] ')).strip().lower()
        if resposta == 's' or resposta =='n':
            break
        print('Digite "S" para SIM ou "N" para NÂO')
    if resposta == 'n':
        break
print('-=' * 20)
print(f'Cod {"Nome":<15}{"Gols":<15}TOTAL')
print('-' * 40)
for cod, jog in enumerate(time):
    print(f'{cod:>3} {jog["nome"]:<15}{str(jog["gols"]):<15}{jog["total"]:>5}')
print('-' * 40)
while True:
    detalhe_jogador = int(input('Mostrar dados de qual jogador: (999 para parar) '))
    if detalhe_jogador == 999:
        break
    elif detalhe_jogador >= len(time) or detalhe_jogador < 0:
        print('Codigo de jogador não encontrado')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[detalhe_jogador]["nome"]}')
        for jog, gols_partidas in enumerate(time[detalhe_jogador]['gols']):
            print(f'    No jogo {jog + 1} fez {gols_partidas} gols')
