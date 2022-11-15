num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
num3 = int(input('Digite um terceiro valor: '))
maior = num1
menor = num2

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

if num1 < num2 and num1 < num3:
    menor = num1
if num3 < num1 and num3 < num2:
    menor = num3

print('O número menor é {}\nE o número maior é {}'.format(menor, maior))
