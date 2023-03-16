# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor do imóvel? R$'))
salário = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos pretende pagar? '))
prestação = casa / (anos * 12)
mínimo  = salário * 30 / 100
print(' Para pagar um casa de R${:.2f} em {} anos.'.format(casa, anos), end='')
print('a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('\33[36mEmpréstimo pode ser CONCEDIDO!')
else:
    print('\33[31mEmpréstimo NEGADO!')
