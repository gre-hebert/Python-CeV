geral_boletim = list()
while True:
    aluno_boletim = []
    aluno_boletim.append(str(input('Nome: ')).strip().lower().capitalize())
    aluno_boletim.append(float(input('1ª Nota: ')))
    aluno_boletim.append(float(input('2ª Nota: ')))
    geral_boletim.append(aluno_boletim)
    while True:
        resposta = str(input('Quer continuar: [S/N] ')).strip().lower()
        if resposta != 'n' and resposta != 's':
            print('\033[31mOpção Inválida\033[m.')
        else:
            break
    if resposta == 'n':
        break
print('-' * 32)
print('             Alunos               ')
print('-' * 32)
print('Nº | Nome                |Média')
print('-' * 32)
for ordinais in range(0, len(geral_boletim)):
    print(f'{ordinais + 1:2}º- {geral_boletim[ordinais][0]:<20}|{(geral_boletim[ordinais][1] + geral_boletim[ordinais][2]) / 2}pts')
while True:
    escolha = int(input('Qual aluno você que mais detalhe? [Digite "999" para sair] '))
    if escolha > len(geral_boletim) and escolha != 999:
        print('\033[33mOpção incorreta\033[m')
    elif escolha == 999:
        break
    else:
        print(f'{geral_boletim[escolha - 1][0]} tirou {geral_boletim[escolha - 1][1]}pts e {geral_boletim[escolha - 1][2]}pts, média de {(geral_boletim[escolha - 1][1] + geral_boletim[escolha - 1][2]) / 2}pts')