# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
sexo = int(input('''Informe o sexo
Digite 0 para MASCULINO e 1 para FEMININO:
'''))
nasc = int(input('Informe o ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('\33[35mQuem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if sexo == 1:
        print('O alistamento não é obrigatório para mulheres. Mas caso queira se alistar: ')
        print('=*'*20)
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} ano(s) para seu alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} ano(s).'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
