from datetime import date
ano = int(input('Qual ano você nasceu? '))
ano_atual = date.today().year

if ano == ano_atual - 18:
    print('Você deve se alistar esse ano!')
elif ano < ano_atual - 18:
    print('O seu alistamento foi há {} anos atrás.\nSe não alistou, procure uma unidade militar.'.format((ano_atual - 18) - ano))

elif ano == ano_atual - 17:
    print('Falta 1 ano para você se alistar.')
else:
    print('Faltam {} anos para você se alistar.'.format(18 - (ano_atual - ano)))
