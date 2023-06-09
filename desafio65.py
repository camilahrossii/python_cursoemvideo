 # Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
 # e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a sigitar valores.

resp = 'S'
soma = qtd = média = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    qtd += 1
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / qtd
print('Você digitou {} números e a média foi {:.2f}.'.format(qtd, média))
print('O MAIOR valor foi {} e o MENOR foi {}.'.format(maior, menor))