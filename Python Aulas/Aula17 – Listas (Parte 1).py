num = [2, 5, 9, 1]
num[2] = 3
print(num) # [2, 5, 3, 1]
num.append(7)
print(num) # [2, 5, 3, 1, 7]
num.sort()
print(num) # [1, 2, 3, 5, 7]
num.sort(reverse=True)
print(num) # [7, 5, 3, 2, 1]
print(f'Essa lista tem {len(num)} elementos') # Essa lista tem 5 elementos
num.insert(2, 0)
print(num) # [7, 5, 0, 3, 2, 1]
num.pop()
print(num) # [7, 5, 0, 3, 2]
num.pop(2)
print(num) # [7, 5, 3, 2]
num.insert(2, 2) 
print(num) # [7, 5, 2, 3, 2]
num.remove(2)
print(num) # [7, 5, 3, 2]
for c, v in enumerate(num):
    print(f'Na posição {c}, encontrei o {v}')
'''
Na posição 0, encontrei o 7
Na posição 1, encontrei o 5
Na posição 2, encontrei o 3
Na posição 3, encontrei o 2
'''
valores = []
for cont in range (0, 5):
    valores.append(int(input('Digite um valore: ')))
print('')
for c, v in enumerate(valores):
    print(f'O {c + 1}º valor que você digitou foi o {v}.')

a = [2, 3, 4, 7]
b = a
b[2] = 8
print(a) # [2, 3, 8, 7]
print(b) # [2, 3, 8, 7]
# Quando usa o '=' criasse um ligação entre as duas variáveis, alteração são feitas nas duas lista.
b = a[:] # IMPORTANTE: Forma correta de passar os elementos de uma variável sem cria um elo entre elas.
b[2] = 4
print(a) # [2, 3, 8, 7]
print(b) # [2, 3, 4, 7] 

