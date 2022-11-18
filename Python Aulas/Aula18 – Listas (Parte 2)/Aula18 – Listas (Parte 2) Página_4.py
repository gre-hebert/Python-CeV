galera = list()
dados = list()
totmai = totmen = 0
for c in range(0, 5):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    print('-' * 15)
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')