txt = str(input('Digite uma frase: '))
txtt = txt.strip().replace(' ','').lower()
inverso = txtt[::-1]
if txtt == inverso:
    print('{} é um palíndromo'.format(txt))
else:
    print('{} não é um palíndromo'.format(txt))
