num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número [Digite 999 pra parar]: '))
    if num != 999:
        soma += num
        cont += 1
print('Você digitou {} números e a soma foi {}'.format(cont, soma))
