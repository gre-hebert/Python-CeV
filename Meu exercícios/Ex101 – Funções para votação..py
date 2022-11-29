def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return print('Não pode votar')
        
    


data = int(input('Em que ano você nasceu: '))
voto(data)