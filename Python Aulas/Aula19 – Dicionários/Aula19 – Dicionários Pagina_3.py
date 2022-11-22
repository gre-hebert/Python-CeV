estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print(brasil) # [{'UF': 'Minas Gerais', 'Sigla': 'MG'}, {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}, {'UF': 'São Paulo', 'Sigla': 'SP'}]
for est in brasil:
    print(est)
    '''
    {'UF': 'Minas Gerais', 'Sigla': 'MG'}
    {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
    {'UF': 'São Paulo', 'Sigla': 'SP'}
    '''
for est in brasil:
    for keys, values in est.items():
        print(f'O campo {keys} tem o valor {values}.')
        '''
        O campo UF tem o valor Minas Gerais.
        O campo Sigla tem o valor MG.
        O campo UF tem o valor São Paulo.
        O campo Sigla tem o valor SP.
        O campo UF tem o valor Rio de Janeiro.
        O campo Sigla tem o valor RJ.
        '''
for est in brasil:
    for values in est.values():
        print(values, end=' ')
    print()
    '''
    Minas Gerais MG 
    São Paulo SP 
    Rio de Janeiro RJ 
    '''