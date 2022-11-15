print('CONVERSOR DE TEMPERATURA')
c = float(input('Informe a temperatura em graus °C: '))
f = (c * 9 / 5) + 32
k = c + 273.15
print('Grau Celsius: {}°C\nGrau Fahrenheit: {}°F\nKelvin: {}°K'.format(c, f, k))