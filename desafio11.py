# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = float(input('Quantos dias de aluguel? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O valor a pagar é de R${:.2f}.'.format(pago))
