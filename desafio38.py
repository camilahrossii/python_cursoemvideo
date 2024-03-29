# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date
hoje = date.today().year
nasc = int(input('Informe o ano de nascimento do atleta: '))
idade = hoje - nasc
if idade <= 9:
    print('O atleta tem {} anos e a sua categoria é MIRIM.'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e a sua categoria é INFANTIL.'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e a sua categoria é JUNIOR.'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos e a sua categoria é SÊNIOR.'.format(idade))
else:
    print('O atleta tem {} anos e a sua categoria é MASTER.'.format(idade))
