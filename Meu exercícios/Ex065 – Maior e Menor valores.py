num = int(input('Digite um numéro: '))
contador = 1
questão = str(input('Quer continuar [S/N]: ')).strip().lower()
soma = num
maior = num
menor = num
while questão == 's':
    num = int(input('Digite um numero: '))
    contador += 1
    soma += num
    questão = str(input('Quer continuar [S/N]: ')).strip().lower()
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print('Você digitou {} número.'.format(contador))
print('A média deles são {}'.format(soma / contador))
print('O menor número foi o {}'.format(menor))
print('E o maior foi o {}'.format(maior))