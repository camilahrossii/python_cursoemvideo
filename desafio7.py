# Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, area))
tinta = area / 2
print('A quantidade de tinta necessária é de {} litros.'.format(tinta))
