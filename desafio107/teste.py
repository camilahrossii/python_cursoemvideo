from moeda import metade, dobro, aumentar

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {metade(p)}')
print(f'O dobro de {p} é {dobro(p)}')
print(f'Aumentando 10%, temos {aumentar(p, 10)}')
# print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13)}')
