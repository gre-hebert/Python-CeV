print('-=-' * 3, 'Tabuada', '-=-' * 3)
num = int(input('Digite um número para ver a tabuada dele: '))
for n in range(1, 11):
    print('{} x {:2} = {:2}'.format(num, n, num * n))
