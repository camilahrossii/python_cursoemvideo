# Faça um programa que leia o comprimento do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
# hi = (co ** 2 + ca ** 2) ** (1/2) - fórmula matemática
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
