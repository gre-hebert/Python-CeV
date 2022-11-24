dicionário = {'B': 3, 'A': 2, 'E': 2, 'D': 5, 'C': 1}
ranking = list()
for keys, values in dicionário.items():
    if len(ranking) == 0:
        ranking.append([values, keys])
    else:
        for num in range(0, len(ranking)):
            if  values > ranking[num][0]:
                ranking.append([values, keys])
            else:
                ranking.insert(ranking[num][0])
print(ranking)