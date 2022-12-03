def leiaInt(msg):
    while True:
        número = str(input(msg))
        if número.isnumeric():
            número = int(número)
            return número
        else:
            print('\033[31mERRO! Digite um número corretamente\033[m')
    

número = leiaInt('Digite um número: ')
print(f'\033[32mVocê digitou {número}\033[m')
