distância = float(input('Qual a distância da sua viagem? '))
print('Você está preste a começar uma viagem de {}km.'.format(distância))
preço = distância * 0.5 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será R${:.2f}'.format(preço))
