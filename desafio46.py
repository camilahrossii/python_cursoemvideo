# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Tabuada do número: '))
for c in range (1, 11):
    print('{} x {} = {}'.format(num, c, num * c))
