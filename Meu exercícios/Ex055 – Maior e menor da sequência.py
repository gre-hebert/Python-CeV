maior = 0
menor = 1000
for a in range (1, 6):
    inp = float(input('Digite o peso da {}ª pessoa: '.format(a)))
    if inp > maior:
        maior = inp
    if inp < menor:
        menor = inp
print('''
O maior peso foi {}kg.
E o menor foi {}kg'''.format(maior, menor))
