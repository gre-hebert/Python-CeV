def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return print(f'Com {idade} anos. Não pode votar')
    elif idade < 18 or idade > 65:
        return print(f'Com {idade} anos. Voto facultativo')
    elif idade < 65:
        return print(f'Com {idade} anos. Voto obrigatória') 


data = int(input('Em que ano você nasceu: '))
voto(data)