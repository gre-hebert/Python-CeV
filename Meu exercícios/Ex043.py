peso = float(input('Qual é o seu peso: '))
altura = float(input('Qual é a sua altura: '))
imc = peso / altura ** 2
print('Seu IMC é de {:.1f}'.format(imc), end='')
if imc < 18.5:
    print(', você está abaixo do peso.')
elif imc < 25:
    print(', você está no peso ideal.')
elif imc < 30:
    print(', você está com sobrepeso.')
elif imc < 40:
    print(', você está com obesidade.')
else:
    print(', Vai morê!!!')