cont = soma = 0
while True:
    valor = int(input('Digite um valor ou 999 para parar: '))
    if valor == 999:
        break
    else:
        cont += 1
        soma += valor
print(f'Você digitou {cont} valores e a soma dos valores são {soma}')