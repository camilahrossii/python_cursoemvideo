# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Informa a velocidade atual do carro: '))
if velocidade > 80:
    print('VOCÊ FOI MULTADO!')
    multa = (velocidade - 80) * 7
    print('A multa será de R${:.2f}.'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')