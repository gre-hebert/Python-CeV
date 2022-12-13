from time import sleep
c = ('\033[m',        # 0 - sem cortes
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[0;30;41m', # 6 - branco
    );

def ajuda(com):
    título(f'Acessando o manual do comando ')