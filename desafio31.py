# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual é o valor do salário do funcionário? R$'))
if salario > 1250:
    calc = (salario * 0.10) + salario
else:
    calc = (salario * 0.15) + salario
print('Quem ganhava R${:.2f} passa a ganhar \033[36;40mR${:.2f}\033[m agora.'.format(salario, calc))