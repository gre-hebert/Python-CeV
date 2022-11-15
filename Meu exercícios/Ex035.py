from distutils.command.config import LANG_EXT


lado_a = float(input('Me informe o tamanho de uma dos lados do triângulo: '))
lado_b = float(input('Agora me informe o tamanho de outro lado do triâgnulo: '))
lado_c = float(input('Agora me informe o tamnaho do ultimo lado do triângulo, que ainda não foi me informado: '))

if lado_a + lado_b > lado_c and lado_b + lado_c > lado_a and lado_a + lado_c > lado_b:
    print('TRIÂNGULOOOO!!!')
else:
    print('Isso não pode ser um triângulo')
print(lado_a, lado_b, lado_c)