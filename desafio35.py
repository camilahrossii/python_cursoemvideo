# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('O primeiro valor \33[34m{}\33[m é maior que o segundo valor \33[34m{}\33[m.'.format(num1, num2))
elif num2 > num1:
    print('O segundo valor \33[36m{}\33[m é maior que o primeiro valor \33[36m{}\33[m.'.format(num2, num1))
else:
    print('Não existe valor maior, \33[35mos dois são iguais!')
