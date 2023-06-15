listagem = ('Lápis', 1.75,
             'Borracha', 2,
             'Caderno', 27.90,
             'Mochila', 129.90,
             'Estojo', 8,
             'Compasso', 9.99,
             'Canetas', 22.30,
             'Fichário', 35,
             'Transferidor', 4.20)
print('-'*40)
print(f'{"LISTA DE PRODUTOS":^37}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')
print('-'*40)