extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    número = int(input('Digite um número de 0 a 20: '))
    if 20 >= número >= 0:
        break
    else:
        print('Tente novamente.', end=' ')
print(f'Você digitou {extenso[número]}')