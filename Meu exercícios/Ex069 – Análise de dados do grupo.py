texto = '-Cadastro no Banco de Dados-'
idade_mais18 = 0
homens  = 0
mulheres_menos20 = 0
print('~' * len(texto))
print(texto)
print('~' * len(texto))
while True:
    idade = int(input('IDADE: '))
    if idade > 18:
        idade_mais18 += 1
    while True:
        sexo = str(input('SEXO [M/F]: ')).strip().lower()
        if sexo == 'm' or sexo == 'masculino' or sexo == 'masc' or sexo == 'male':
            homens += 1
            break
        elif sexo == 'f' or sexo == 'fem' or sexo == 'feminino' or sexo == 'female':
            if idade < 20:
                mulheres_menos20 += 1
            break
        else:
            print('Por favor, digite o sexo corretamente.')
        
    print('-' * 23)
    pergunta = str(input('Quer continuar [S/N]: ')).strip().lower()
    print('-' * 23)
    if pergunta == 'n':
        break
if idade_mais18 == 0:
    print('Ninguém é maior de 18 anos.')
elif idade_mais18 == 1:
    print('Uma pessoa é maior de 18 anos ')
else:
    print(f'{idade_mais18} pessoas é maior de 18 anos')
if homens == 0:
    print('Nenhum homem cadstrado')
elif homens == 1:
    print('1 homem cadastrado.')
else:
    print(f'{homens} homens cadastrados.')
if mulheres_menos20 == 0:
    print('Nenhuma mulher com menos de 20 anos cadastrada.')
elif mulheres_menos20 == 1:
    print('Somente uma mulher com menos de 20 anos cadastrada.')
else:
    print(f'{mulheres_menos20} menos de 20 anos cadastrada.')
