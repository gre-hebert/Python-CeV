sexo = str(input('Digite seu sexo [M/F]: ')).strip().lower()
if sexo == 'm' or sexo == 'masc' or sexo == 'masculino' or sexo == 'male':
    sexo = 'masculino'
elif sexo == 'f' or sexo == 'fem' or sexo == 'feminino' or sexo == 'female':
    sexo = 'feminino'
else:
    sexo = 'erro'
while sexo == 'erro':
    sexo = str(input('ERRO\nDigite seu sexo corretamente, M para masculino e F para feminino: ')).strip().lower()
    if sexo == 'm' or sexo == 'masc' or sexo == 'massculino' or sexo == 'male':
        sexo = 'masculino'
    elif sexo == 'f' or sexo == 'fem' or sexo == 'feminino' or sexo == 'female':
        sexo = 'feminino'
    else:
        sexo = 'erro'
print('Sexo cadastrado como {}.'.format(sexo))
