from random import randint
valores = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f'Os valores sorteados foram: {valores}')
maior = 0
for contador in range(0, 5):
    if valores[contador] > maior:
        maior = valores[contador]
print(f'O maior valor sorteado foi {maior}')
menor = valores[0]
for contador in range(0, 5):
    if valores[contador] < menor:
        menor = valores[contador]
print(f'O menor valor sorteado é {menor}')
