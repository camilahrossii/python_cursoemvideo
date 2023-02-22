#Faça um ṕrograma que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o último nome separadamente
# Ex: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

nome = str(input('Informe o seu nome completo: ')).strip().split()
print('O primeiro nome é {}.'.format(nome[0]))
print('O último nome é {}.'.format(nome[len(nome)-1]))
