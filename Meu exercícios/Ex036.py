print('\033[7m-=-\033[m' *20)
valor = float(input('Qual é o valor da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
prestação = int(input('Em quantas prestações você desejar pagar a casa? R$'))

if valor / prestação <= sal * 30/100:
    print('Seu empréstimo foi \033[34mAPROVADO\033[m, você pagará R${:.2f} por mês'.format(valor / prestação))
else:
    print('\033[31mEmprétimo reprovado\033[m.')
print('\n')
print('Valor da prestação R${:.2f}.\n30% do salario R${:.2f}'.format(valor / prestação, sal * 30/100))
print('\033[7m-=-\033[m' *20)
