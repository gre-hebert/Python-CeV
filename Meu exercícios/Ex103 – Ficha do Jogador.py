def jogador(nome='<desconhecido>', gols=0):
    pergunta_nome = str(input('Nome do jogador: ')).strip().lower().capitalize()
    if len(pergunta_nome) > 0:
        nome = pergunta_nome
    pergunta_gols = str(input('Quantos gols: ')).strip()
    if pergunta_gols.isnumeric():
        gols = int(pergunta_gols)
    if gols > 1:
        print(f'O jogador {nome} fez {gols} gols.')
    elif gols == 1:
        print(f'O jogador {nome} fez 1 gol.')
    else:
        print(f'O jogador {nome} não fez gol.')

jogador()