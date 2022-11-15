num = int(input('Digite um número: '))
razão = int(input('Qual a razão da PA: '))
contador = 0
while contador < 10:
    print(num, end=' -> ')
    num += razão
    contador += 1
print('FIM')
