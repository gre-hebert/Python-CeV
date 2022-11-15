print('LOCADORA DE VEÍCULOS')
dias = int(input('Quantos dias? '))
km = float(input('Quantos km? '))
pagar = dias * 60 + km * 0.15
print('O total a pagar é R${:.2f}\nDescrição:\nDiárias: R${:.2f}\nKm: R${:.2f}'.format(pagar, (dias*60),(km*0.15)))