sal = float(input('Qual o seu salário? R$'))

nsal = sal + (sal * 10 / 100) if sal > 1250 else sal + (sal * 15 / 100)

print('Seu salário era de R${:.2f} e com o aumento de {}%  vai passar a se R${:.2f}'.format(sal, 15 if sal < 1250 else 10, nsal))