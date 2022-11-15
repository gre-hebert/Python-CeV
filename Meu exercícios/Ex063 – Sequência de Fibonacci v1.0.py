termos = int(input('Quatos termos deseja ver: '))
contador = 0
num0 = 0
num1 = 1
while contador < termos:
    contador += 1
    print(num0, end=' -> ')
    soma = num0 + num1
    num0 = num1
    num1 = soma
print('FIM')
