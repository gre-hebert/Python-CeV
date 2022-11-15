total_pessoas = int(input('Quantas pessoas serão analisadas? ')) + 1
soma_das_idades = 0
idade_homem_mais_velho = 0
homen_mais_velho = ''
mulheres_menos_20 = 0
for pessoas in range(1, total_pessoas):
    print('----- {}ª pessoa -----'.format(pessoas))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).lower().strip()
    soma_das_idades += idade
    if sexo == 'm' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        homen_mais_velho = nome
    if sexo == 'f' and idade < 20:
        mulheres_menos_20 += 1
print('A média de idade do grupo é {}.'.format(soma_das_idades / pessoas))
print('{} é o homem mais velho.'.format(homen_mais_velho))
if mulheres_menos_20 == 1:
    print('{} mulher tem menos de 20 anos.'.format(mulheres_menos_20))
else:
    print('{} mulheres tem menos de vinte anos.'.format(mulheres_menos_20))
