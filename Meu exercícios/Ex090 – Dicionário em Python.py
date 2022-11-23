aluno = {'Nome': str(input('Nome: ')).strip().lower().capitalize(), 'Nota': float(input('Nota: '))}
print(f'Nome do aluno é {aluno["Nome"]}.\nEle tirou {aluno["Nota"]}')
if aluno['Nota'] >= 7:
    print('Ele está \033[34mAPROVADO\033[m')
else:
    print('Ele está \033[31mREPROVADO\033[m')