from math import hypot
co = float(input('Qual o tamanho do cateto oposto? '))
ca = float(input('Qual o tamnaho do cateto adjacente? '))
hip = hypot(co, ca)
print('O valor dda hipotenusa é {:.2f}'.format(hip))  