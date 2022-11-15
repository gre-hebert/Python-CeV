salário = float(input('Qual é o saalário do funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário de ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(salário, novo))
