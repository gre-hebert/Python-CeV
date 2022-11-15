while True:
    num = int(input('Digite um número para ver a sua tabuada: '))
    if num < 0:
        break
    for mult in range(1, 11):
        print(f'{num} x {mult:2} = {num * mult:2}')
print('Programa finalizado')
