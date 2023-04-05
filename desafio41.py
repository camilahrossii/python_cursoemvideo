# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
print('{:~^40}'.format(' Simulador de Loja '))
produto = float(input('Valor do produto: R$'))
print('''FORMAS DE PAGAMENTO
- à vista dinheiro/cheque: DIGITE 1
- à vista no cartão: DIGITE 2
- em até 2x no cartão: DIGITE 3
- 3x ou mais no cartão: DIGITE 4''')
pagamento = int(input('Qual será a forma de pagamento? '))
if pagamento == 1:
    total = produto - (produto * 10 / 100)
elif pagamento == 2:
    total = produto - (produto * 5 / 100)
elif pagamento == 3:
    total = produto
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(parcela))
elif pagamento == 4:
    total = produto + (produto * 20 / 100)
    totalParcelas = int(input('Quantas parcelas? '))
    parcela = total / totalParcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(totalParcelas, parcela))
else:
    total = produto
    print('OPÇÃO DE PAGAMENTO INVÁLIDA. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(produto,total))
