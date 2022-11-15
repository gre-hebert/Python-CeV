km = float(input('Qual a distância em km da viagem: '))
if km < 200:
    print('O valor da viagem é R${:.2f}.'.format(km * 0.5))
else:
    print('o valor da viagem é de R${:.2f}.'.format(km * 0.45) )
