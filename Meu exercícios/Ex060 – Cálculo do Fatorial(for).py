num = int(input('Digite um número para ver o seu fatorial: '))
print('{}! = {}'.format(num, num), end=' x ')
for fatorial in range(num -1, 1, -1):
    print('{}'.format(fatorial), end=' x ')
    num *= fatorial
print('1 = {}'.format(num))
    