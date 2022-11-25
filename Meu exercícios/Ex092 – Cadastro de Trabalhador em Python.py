from datetime import date
cadastro = dict()
cadastro['Nome'] = str(input('Nome: ')).strip().lower().capitalize()
cadastro['Idade'] = date.today().year - int(input('Ano: ')) 
cadastro['CTPS'] = int(input('Carteira de trabalho: '))
if cadastro['CTPS'] == 0:
    print('-=' * 30)
    for keys, values in cadastro.items():
        print(f'{keys} = {values}')