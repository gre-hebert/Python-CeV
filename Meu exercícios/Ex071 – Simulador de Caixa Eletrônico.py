while True:
    valor = int(input('Qual o valor deseja sacar: '))
    print(f'{valor // 50} notas de 50')
    print(f'{(valor % 50) // 20} notas de 20')
    print(f'{((valor % 50) % 20) // 10} notas de 10')
    print(f'{(((valor % 50) % 20) % 10) // 1} notas de 1')
    sacar_mais = str(input('Deseja sacar mais: [S/N]:')).strip().lower()
    if sacar_mais == 'n':
        break
    