# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.

velho = 0
nova = 0
soma = 0
for c in range(1,5):
    print('{} {}ª PESSOA --{}'.format(('-'*12), c, ('-'*12)))
    nome = input('Nome: ')
    idade = int(input('Idade:'))
    sexo = input('Sexo [F / M]: ')
    soma += idade
    if idade == 1:
        nova = 0
        velho = 0
    else:
        if idade > velho:
            velho = idade
        else :
            nova = idade
    if sexo == M and idade > nova:
        print(nome, idade)
media = soma / 5
print('A média das idade citada é {}'.format(media))
