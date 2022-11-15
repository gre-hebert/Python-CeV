preco = float(input('Digite o preço do produto: R$'))
desc = (preco*5)/100
novo_preco = preco - desc

print('Preço: R${:.2f}\nDesconto(5%): R${:.2f}\nPreço com desconto: R${:.2f}'.format(preco, desc, novo_preco))