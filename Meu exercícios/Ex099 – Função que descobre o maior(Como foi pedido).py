import time
def função(* números):
    print('=-' * 20)
    print('Analisando os valores passados...')
    for  valor in números:
        print(valor, end=' ')
        time.sleep(.5)
    print(f'Foram informados {len(números)} valores ao todo.')
    if len(números) > 0:
        print(f'O maior valor informado foi {max(números)}')
        

função(2,9,4,5,7,1)
função(4,7,0)
função(1,2)
função(6)
função()