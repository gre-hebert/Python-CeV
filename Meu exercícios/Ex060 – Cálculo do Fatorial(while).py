num = int(input('Informe um número: '))
fatorial = num - 1
resultado = num * fatorial
print('{}! = {}'.format(num, num), end=' ')
while fatorial > 1:
    print('x {}'.format(fatorial), end=' ')
    fatorial -= 1
    resultado *= fatorial
print('x 1 = {}'.format(resultado))
