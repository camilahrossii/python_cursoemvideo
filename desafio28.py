# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule e peça o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Informe a distância da sua viagem em Km: '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}.'.format(preço))