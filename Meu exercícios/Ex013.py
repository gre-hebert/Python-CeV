sal = float(input('Qual é o salario do funcionário? R$'))
novo = sal + (sal * 15 / 100)
print('O salário que antes era de R${:.2f}, com o aumento de 15% vai para R${:.2f}.'.format(sal, novo))
