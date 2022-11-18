galera = (['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45])
print(galera[2][1]) # 13
for p in galera:
    print(p)
    '''
    ['João', 19]
    ['Ana', 33]
    ['Joaquim', 13]
    ['Maria', 45]   
    '''
for p in galera:
    print(p[0])
    '''
    João
    Ana
    Joaquim
    Maria
    '''
for p in galera:
    print(p[1])
    '''
    19
    33
    13
    45
    '''
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
    '''
    João tem 19 anos de idade.
    Ana tem 33 anos de idade.
    Joaquim tem 13 anos de idade.
    Maria tem 45 anos de idade.
    '''
