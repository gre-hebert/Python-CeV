preço_total = 0
produtos_mais1000 = 0
produto_mais_barato = 0
nome_do_produto_mais_barato = ''
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Valor do produto: R$'))
    if preço > 1000:
        produtos_mais1000 += 1
    if produto_mais_barato == 0 or preço < produto_mais_barato:
        nome_do_produto_mais_barato = nome
    preço_total += preço
    continuar = str(input('Deseja continuar [S/N]: '))
    if continuar == 'n':
        break
print(f'Valor total: R${preço_total:.2f}')
print(f'{produtos_mais1000} produtos custam mais de R$1000.')
print(f'O produto mais barato foi o {nome_do_produto_mais_barato}.')
