# Faça um programa que leia o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura WHILE.

primeiroT = int(input('Digite um número: '))
razão = int(input('Razão: '))
termo = primeiroT
cont = 1
while cont <= 10:
    print('{} - '.format(termo),end='')
    termo += razão
    cont += 1
print('FIM')
