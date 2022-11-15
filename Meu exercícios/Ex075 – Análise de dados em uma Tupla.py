números = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')), int(input('Digite o terceiro número: ')), int(input('Digite o último número: ')))
print(f'Os números que você digitou foi: ', end='')
for n in números:
    print(n, end=' ')
if números.count(9) == 0:
    print('\nO \033[1;34m9\033[m não aparece \033[1;31mnenhuma vez\033[m')
elif números.count(9) == 1:
    print('\nO \033[1;34m9\033[m aparece \033[1;33m1 vez\033[m')
else:
    print(f'\nO \033[1;34m9\033[m aparece \033[1;33m{números.count(9)} vezes\033[m')
if 3 in números:
    print(f'O \033[1;34m3\033[m aparece pela \033[1;33m1ª vez\033[m na \033[1;32m{números.index(3) + 1}ª posição\033[m')
else:
    print('O numero \033[1;34m3\033[m \033[1;31mnão foi digitado\033[m')
cont = 0
for n in números:
    if n % 2 == 0 and n != 0:
        cont += 1
if cont == 0:
    print('\033[1;31mNenhum\033[m número par foi digitado')
else:
    print('Os numeros pares são ', end='')
    for n in números:
        if n % 2 == 0 and n != 0:
            print(n, end=' ')
    