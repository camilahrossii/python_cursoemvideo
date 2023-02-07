# 5+3*2 == 11
# 5**2 == 125
# 19//2 == 2
# 19/2 == 9,5
# 365**522 == numero gigante (py nao tem limites)
# 18%2 = 0

# ao cubo
# 4**3 == 64
# pow(4,3) == 64 << perde a ordem de precedência

#raíz quadrada
# 81**(1/2) == 9,0

# raíz cúbica
# 127**(1/3) == 5.026525695313479

# automatização de repetição de escrita
# 'texto '*5 ==
# 'texto texto texto texto texto '

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))
# sem alinhamento {:20}
#alinhamento para a direita {:>20}
# alinamento no meio {:^20}
# alinhado por espaços {:=^20}

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, \n o produto é {} \n e a divisão é {:.3f}'.format(s, m, d), end=' >>>')
print('Divisão inteira {} e potência {}'.format(di, e))
# {:.3f} == 3 casas decimais
# , end='') == conteúdo na mesma linha
# \n == quebra de linha