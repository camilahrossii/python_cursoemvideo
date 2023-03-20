# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Informe seu peso (kg): '))
altura = float(input('Informe sua altura (m): '))
IMC = peso / (altura ** 2)
print('O seu IMC é de {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= IMC < 25:
    print('Parabéns, você está na faixa de PESO IDEAL')
elif 25 <= IMC < 30:
    print('Você está em SOBREPESO')
elif 30 <= IMC < 40:
    print('Você está em OBESIDADE, cuidado!!')
elif IMC >= 40:
    print('Cuidado! Você está com OBESIDADE MÓRBIDA!')
