palavras = ('abacate', 'salgado', 'ferramenta', 'analisando',
            'sorvete', 'brinquedo', 'dado', 'jogador', 'piscina')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais:  ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')