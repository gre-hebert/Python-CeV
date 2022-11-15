pri = int(input('Informe o primeiro termo: '))
razão = int(input('Informe a razão da PA: '))
pa = 0
for cont in range(1, 11):
    pa = pri + (cont - 1) * razão
    print('a{} = {}'.format(cont, pa))