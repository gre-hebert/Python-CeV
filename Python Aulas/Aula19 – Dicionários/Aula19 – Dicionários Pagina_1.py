pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas) # {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome']) # Gustavo
print(pessoas['idade']) # 22
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') # O Gustavo tem 22 anosO Gustavo tem 22 anos
print(pessoas.keys()) # dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values()) # dict_values(['Gustavo', 'M', 22])
print(pessoas.items()) # dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])
for elementos in pessoas.keys():
    print(elementos)
    '''
    nome
    sexo
    idade
    '''
for elementos in pessoas.values():
    print(elementos)
    '''
    Gustavo
    M
    22
    '''
for elementos in pessoas.items():
    print(elementos)
    '''
    ('nome', 'Gustavo')
    ('sexo', 'M')
    ('idade', 22)
    '''
for keys, values in pessoas.items():
    print(keys, values)
    '''
    nome Gustavo
    sexo M
    idade 22
    '''
del pessoas['sexo']
for keys, values in pessoas.items():
    print(f'{keys}: {values}')
    '''
    nome: Gustavo
    idade: 22
    '''
pessoas['nome'] = 'Leandro'
for keys, values in pessoas.items():
    print(f'{keys}: {values}')
    '''
    nome: Leandro
    idade: 22
    '''
pessoas['peso'] = 98.5
for keys, values in pessoas.items():
    print(f'{keys}: {values}')
    '''
    nome: Leandro
    idade: 22
    peso: 98.5
    '''