lado1 = float(input('Informe o tamanho do primeiro segmento: '))
lado2 = float(input('Informe o tamanho do segundo segmento: '))
lado3 = float(input('Informe o tamnaho do terceiro segmento: '))
if lado1 + lado2 <= lado3 or lado2 + lado3 <= lado1 or lado2 + lado1 <= lado2:
    print('Isso não pode ser um triângulo.')
elif lado1 == lado2 and lado1 == lado3:
    print('Este é um triângulo EQUILÁTERO!')
elif lado1 == lado2 and lado1 != lado3 or lado2 == lado3 and lado2 != lado1 or lado3 == lado1 and lado3 != lado2:
    print('Este é um triângulo ISÓSCELES!')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print('Este é um triângulo ESCALENO!')
else:
    print('Isso poder ser um triângulo.')