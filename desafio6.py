# Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considerar $1,00 = R$ 3,27
real = float(input('Quanto você tem na carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f} você poderá comprar US${:.2f}.'.format(real, dolar))
