aluno = {}
aluno['nome'] = str(input('Nome do Aluno: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
situação = ''
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('=-' * 20)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
