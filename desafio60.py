# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

# from math import factorial
# numero = int(input('Fatorial de: '))
# fatorial = factorial(numero)
# print('O fatorial de {} é {}.'.format(numero, fatorial))

numero = int(input('Fatorial de: '))
count = numero
fatorial = 1
print('Calculando {}! = '.format(numero), end='')
# while count > 0:
#     print('{}'.format(count), end='')
#     print(' x ' if count > 1 else ' = ', end='')
#     fatorial *= count
#     count -= 1
# print('{}'.format(fatorial))

for numero in range(count, fatorial):
    print('{}'.format(count), end='')
    print(' x ' if count > 1 else ' = ', end='')
    fatorial *= count
    count -= 1
    print('{}'.format(fatorial))