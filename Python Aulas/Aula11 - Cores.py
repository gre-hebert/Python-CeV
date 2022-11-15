from distutils import core


print('\n')
print('STYLE')
print('-' * 5)
print('\033[0mNone\033[m')
print('\033[1mBold\033[m')
print('\033[4mSublinhado\033[m')
print('\033[7mIvertido\033[m')
print('-' * 5)
print('\n')

print('TEXT')
print('-' * 5)
print('\033[30mCinza\033[m \033[31mVermelho\033[m \033[32mVerde\033[m \033[33mAmarelo\033[m')
print('\033[34mAzul\033[m \033[35mRoxo\033[m \033[36mCiano\033[m \033[37mBranco\033[m')
print('-' * 5)
print('\n')

print('BACK')
print('-' * 5)
print('\033[40mPreto\033[m \033[41mVermelho\033[m \033[42mVerde\033[m \033[43mAmarelo\033[m')
print('\033[44mAzul\033[m \033[45mRoxo\033[m \033[46mCiano\033[m \033[47mBranco\033[m')
print('-' * 5)
print('\n')

print('\033[1;31;43mOlá, mundo!\033[m')

a = 3
b = 5
print('O valores são \033[32m{}\033[m e \033[33m{}\033[m!!!'.format(a, b))

nome = 'Grégão'
print('Olá, prazer em te conhecer {}{}{}.'.format('\033[31m', nome,'\033[m' ))

local = 'Casa'
hora = '7pm'
dia = 'Segunda'
cores = {'limpa':'\033[m', 
    'azul':'\033[34m', 
    'amarelo':'\033[33m', 
    'pretoebranco':'\033[7m'}
print('Hoje {}{}{} eu cheguei em {}{}{} as {}{}{}!!!'.format(cores['pretoebranco'], dia, cores['limpa'], cores['azul'], local, cores['limpa'], cores['amarelo'], hora, cores['limpa']))
print('\n')
