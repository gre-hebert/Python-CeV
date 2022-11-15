valor = float(input('Qual o valor da compra: '))
print('''Qual a forma de pagamento?
[1] À vista no dinheiro.
[2] À vista no cartão.
[3] Em 2x no cartão.
[4] Em 3x ou mais vezes no cartão''')
#1- 10% de desconto
#2- 5% de desconto
#3- Preço normal
#4- 20% de JUROS
forma = int(input('Digite o numero referente a forma de pagamento: '))
if forma == 1:
    print('O cliente ganha 10% de desconto e o valor sai a R${:.2f}.'.format(valor - (valor * 10 / 100)))
elif forma == 2:
    print('O cliente ganha 5% de desconto e o valor sai a R${:.2f}.'.format(valor - (valor * 5 / 100)))
elif forma == 3:
    print('Serão 2x de R${:.2f} e o valor total a ser pago é de R${:.2f}.'.format(valor / 2, valor) )
elif forma == 4:
    parcela = int(input('Em quantas vezes: '))
    print('Serão {}x de R${:.2f} e o valor total a se pago é de R${:.2f} com 20% de JUROS.'.format(parcela, (valor + (valor * 20 / 100))/ parcela, valor + (valor * 20 /100)))
else:
    print('Forma invalida')