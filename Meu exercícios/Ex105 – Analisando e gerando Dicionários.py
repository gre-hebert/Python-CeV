def notas(*notas, situação=False):
    estatisticas = dict()
    estatisticas['Total de Notas:  '] = len(notas)
    estatisticas['Maior nota:      '] = max(notas)
    estatisticas['Menor nota:      '] = min(notas)
    estatisticas['Média da notas:  '] = sum(notas)/len(notas)
    if situação:
        if estatisticas['Média da notas:  '] < 5:
            estatisticas['\033[31mSituação'] = 'RUIM\033[m'
        elif estatisticas['Média da notas:  '] < 7:
            estatisticas['\033[34mSituação'] = 'RAZOÁVEL\033[m'
        else:
            estatisticas['\033[32mSituação'] = 'BOA\033[m'
    for x, y in estatisticas.items():
        print(x, y)
    

notas(2,4,6, situação=True)
notas(5,6,7,8, situação=True)
notas(6,7,8,9,10, situação=True)