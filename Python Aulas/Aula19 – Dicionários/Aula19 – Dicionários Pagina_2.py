brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1) # {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
print(estado2) # {'UF': 'São Paulo', 'Sigla': 'SP'}
print(brasil) # [{'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}, {'UF': 'São Paulo', 'Sigla': 'SP'}]
print(brasil[0]) # {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
print(brasil[1]) # {'UF': 'São Paulo', 'Sigla': 'SP'}
print(brasil[0]['UF']) # Rio de Janeiro
print(brasil[1]['Sigla']) # SP
