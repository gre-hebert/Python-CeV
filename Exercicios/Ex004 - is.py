a = input('Digite algo: ')

print('O tipo primitivo desse valor é:', type(a))

print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É somente espaços?', a.isspace())
print('É minusculo?', a.islower())
print('É maiuscula?', a.isupper())
print('É alfanumérico?', a.isalnum())
print('Está capitalizada?', a.istitle())
