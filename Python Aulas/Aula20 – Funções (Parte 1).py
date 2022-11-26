def soma(a, b):
    s = a + b
    print(s)


# Primeiro Programa
soma(2, 3) # 5
soma(4, 8) # 12
soma(7, 1) # 8

# Segundo Programa
def soma2(x, y):
    print(f'X = {x} e Y = {y}')

    
soma2(1, 2)  # X = 1 e Y = 2
soma2(y = 1, x = 2) # X = 2 e Y = 1

# Terceiro Programa 
def contador(* num):
    print(num)
    for valor in num:
        print(valor, end=' ')
    print()
    print(len(num))


contador(2, 4, 6, 7)
'''
(2, 4, 6, 7)
2 4 6 7 
4
'''

# Quarto Programa
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos += 1
    print(lst)


valores = [1, 3, 5]
dobra(valores) # [2, 6, 10]
dobra(valores) # [4, 12, 20]

# Quinto Programa
def soma3(* valores):
    s = 0
    for num in valores:
        s += num
    print(s)


soma3(7, 3) # 10
soma3(9, 6, 4) # 19
soma3(7, 19, 53, 21) # 100