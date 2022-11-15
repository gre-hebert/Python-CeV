num = 0
for dig in range (0, 6):
    digitado = int(input('Digite um numero: '))
    if digitado % 2 == 0:
        num += digitado
print(num)
