# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('~*'*20)
print('Analisador de Triângulos')
print('~*'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[30;42mPODEM FORMAR\033[m triângulo!!')
else:
    print('Os segmentos acima \033[31;40mNÃO PODEM FORMAR\033[m triângulo!!')