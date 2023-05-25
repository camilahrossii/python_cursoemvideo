'''Faça um prgrama que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'
Caso esteja errado, peça a digitação novamente até ter um valor correto'''

sexo = str(input('Por favor, informe seu sexo [ F / M ] :')).strip().upper()[0]
while sexo not in 'FmMm':
    sexo = str(input('Dados inválidos. Por favor, tente novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))