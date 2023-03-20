# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print('~*'*20)
print('Analisador de Triângulos')
print('~*'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[30;42mPODEM FORMAR\033[m triângulo!!')
    if r1 == r2 == r3:
        print('E formam um \033[30;42mEQUILÁTERO\033[m!!')
    elif r1 != r2 != r3 != r1:
        print('E formam um \033[30;45mESCALENO\033[m!!')
    else:
        print('E formam um \033[31;40mISÓSCELES\033[m!!')
else:
    print('Os segmentos acima \033[31;40mNÃO PODEM FORMAR\033[m triângulo!!')

