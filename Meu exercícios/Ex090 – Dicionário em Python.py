aluno = {'Nome': str(input('Nome: ')).strip().lower().capitalize(), 'Nota': float(input('Nota: '))}
if aluno['Nota'] >= 7:
    aluno['Situação'] = '\033[34mAPROVADO\033[m'
else:
    aluno['Situação'] = '\033[31mREPROVADO\033[m'
print(f'Nome do aluno é {aluno["Nome"]}.\nEle tirou {aluno["Nota"]}.\nEle está {aluno["Situação"]}')
