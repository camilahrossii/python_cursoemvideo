# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preço = float(input('Digite o preço do produto: R$'))
desc = preço * 0.05
vlFinal = preço - desc
print('O produto custa R${:.2f}, o valor do desconto será de R${:.2f}. \nO valor final é R${:.2f}.'.format(preço, desc ,vlFinal))

# O cálculo também pode ser feito assim: 10*5/100
# desc = preço - (preço * 5 / 100)
