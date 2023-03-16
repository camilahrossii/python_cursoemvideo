# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('A média tirada pelo aluno foi {}.'.format(média))
if média < 5:
    print('O aluno está REPROVADO')
# elif média >= 5 and média < 7>:
elif 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO')
else:
    print('O aluno está APROVADO')