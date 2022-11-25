lista = list()
média = list()
while True:
    cadastro = {'nome': str(input('Nome: ')).strip().lower().capitalize()}
    while True:
        cadastro['sexo'] = str(input('Sexo: [M/F] ')).strip().lower()
        if cadastro['sexo'] != 'm' and cadastro['sexo'] != 'f':
            print('Erro, digite apenas M ou F.')
        else:
            break
    cadastro['idade'] = int(input('Idade: '))
    lista.append(cadastro)
    média.append(cadastro['idade'])
    while True:
        pergunta = str(input('Quer continuar? [S/N] ').strip().lower())
        if pergunta != 's' and pergunta != 'n':
            print('Erro, digite apenass "S" ou "N" ')
        else:
            break
    if pergunta == 'n':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastrada.')
print(f'B) A média de idade é de {sum(média) / len(média)} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for índice, dicionário in enumerate(lista):
    if dicionário['sexo'] == 'f':
        print(dicionário['nome'], end=', ')
print()
print(f'D) Listas das pessoas que estão acima da média: ')
for d in lista:
        if d['idade'] > sum(média) / len(média):
            print(f'    => {d["nome"]}, com {d["idade"]} anos.')
