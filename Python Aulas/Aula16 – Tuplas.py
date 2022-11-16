'''
tupla = () #Tuplas são imutáveis!
lista = []
dicionário = {}
'''
lanche = ('Hamburgue', 'Suco', 'Pizza', 'Pudim')
#Uma tupla também pode sser representada sem os ()
print(lanche)
lanche = 'Hamburgue', 'Suco', 'Pizza', 'Pudim'
print(lanche)
#Na hora de exibir ele considera como se fosse uma tupla, com os ()
print(lanche[1]) #Suco
print(lanche[3]) #Pudim
print(lanche[-2]) #Pizza
print(lanche[1:3]) #('Suco', 'Pizza')
print(lanche[2:]) #('Pizza', 'Pudim')
print(lanche[:2]) #('Hamburgue', 'Suco')
print(lanche[-2:]) #('Pizza', 'Pudim')
print(lanche[-3:]) #('Suco', 'Pizza', 'Pudim')
print('-' * 100)
for comida in lanche:
    print(f'Eu comi ou bebi {comida}') 
'''
Eu comi ou bebi Hamburgue
Eu comi ou bebi Suco
Eu comi ou bebi Pizza
Eu comi ou bebi Pudim
'''
print('')
for contador in range(0, len(lanche)):
    print(f'Eu comi ou bebi {lanche[contador]}')
'''
Eu comi ou bebi Hamburgue
Eu comi ou bebi Suco
Eu comi ou bebi Pizza
Eu comi ou bebi Pudim
'''
print('')
for posição, comida in enumerate(lanche):
    print(f'Minha {posição + 1}ª refeição será {comida}')
'''
Minha 1ª refeição será Hamburgue
Minha 2ª refeição será Suco
Minha 3ª refeição será Pizza
Minha 4ª refeição será Pudim
'''
print('-' * 100)
print(len(lanche)) #4
lanche = ('Hamburgue', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
print(len(lanche)) #5
print(sorted(lanche)) #['Batata frita', 'Hamburgue', 'Pizza', 'Pudim', 'Suco'] - Repare que os itens foram exibidos em lista []
print('-' * 100)
a_tupla = (2, 5, 4)
b_tupla = (5, 8, 1, 2)
c = a_tupla + b_tupla
d = b_tupla + a_tupla
print(c) #(2, 5, 4, 5, 8, 1, 2)
print(d) #(5, 8, 1, 2, 2, 5, 4)
print(c.count(5)) #2
print(c.count(4)) #1
print(c.count(9)) #0
print(sorted(c)) #[1, 2, 2, 4, 5, 5, 8]
# Variável.index(termo) vai mostra que posição está o termo.
print(c.index(8)) #4
print(d.index(8)) #1
print(c.index(2)) #0
print(c.index(2, 1)) #6 - Apartir da posição 1, onde tem o termo 2
print('-' * 100)
pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)
print(pessoa)