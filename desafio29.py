# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date
ano = int(input('Que ano você quer analisar?  Coloque 0 para analisar o ano atual. '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é \033[34mBISSEXTO\033[m!'.format(ano))
else:
    print('O ano {} \033[30;41mNÃO\033[m é BISSEXTO!'.format(ano))
