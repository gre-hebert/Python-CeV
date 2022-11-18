teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste) # ['Gustavo', 40]
galera = list()
galera.append(teste)
print(galera) # [['Gustavo', 40]]
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera) # [['Maria', 22], ['Maria', 22]]
