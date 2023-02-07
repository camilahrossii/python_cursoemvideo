# Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

salario = float(input('Salário: R$'))
novoSal = salario + (salario * 15 / 100)
print('O salário atual é de R${:.2f}. \nCom o aumento de 15% passará a ser R${:.2f}.'.format(salario, novoSal))