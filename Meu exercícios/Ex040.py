num1 = float(input('Qual foi a primeira nota: '))
num2 = float(input('Qual foi a segunda nota: '))

# 0 - 4.9 = REPROVADO
# 5 - 6.9 = RECUPERAÇÃO
# 7 - 10 = APROVADO

nota = (num1 + num2) / 2

if nota < 5:
    print('A média das notas é {:.1f}, o aluno está \033[31;1mREPROVADO\033[m.'.format(nota))
elif nota >= 5 and nota < 7:
    print('A média das notas é {:.1f}, o aluno está em \033[34;1mRECUPERAÇÃO\033[m.'.format(nota))
else:
    print('A média das notas é {:.1f}, o alino está \033[32;1mAPROVADO\033[m.'.format(nota))
