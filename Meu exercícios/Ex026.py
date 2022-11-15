frase = str(input('Digite uma frase: ')).upper().strip().replace(' ','')
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A') + frase.count('Á') + frase.count('À') + frase.count('Â') + frase.count('Ã')))
print('A primeira letra "A" apareceu na posição {}.'.format(frase.find('A') + 1))
print('A última letra "A" pareceu na posição {}.'.format(frase.rfind('A') + 1))