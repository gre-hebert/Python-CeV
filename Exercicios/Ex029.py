from email.mime import multipart


velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você eccedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de {:.2f}!'.format(multa))
print('Tenha uma bom dia! Dirija com segurança!')