# Crie um programa que leia um númeo Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite o número: 6.127. O número 6.127 tema  aprte inteira 6.

from math import trunc
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(num, trunc(num)))

