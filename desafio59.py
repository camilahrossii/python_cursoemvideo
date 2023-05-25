# Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
#
# [ 2 ] multiplicar
#
# [ 3 ] maior
#
# [ 4 ] novos números
#
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
opção = 0
while opção != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do Programa''')
    opção = int(input('>>>>> Digite a sua opção: '))
    if opção == 1:
        soma = n1 + n2
        print('A soma de {} + {} é {}.'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('{} x {} é igual a {}.'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            print('Entre {} e {}, o maior número é {}.'.format(n1, n2, n1))
        else:
            print('Entre {} e {} o maior número é {}.'.format(n1, n2, n2))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Informe o primeiro valor: '))
        n2 = int(input('Informe o segundo valor:'))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção INVÁLIDA. Tente novamente.')
    print('=*' * 15)
    sleep(2)
print('Fim do Programa. Volte Sempre!!')