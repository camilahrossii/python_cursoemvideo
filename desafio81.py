valores = list()
while True:
    valores.append(int(input('Digite um número: ')))
    print('Valor adicionado com sucesso...')
    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp == 'N':
        break
valores.sort(reverse=True)
print(f'Foram digitados {len(valores)} números')
print(f'Números informados: {valores}')
if 5 in valores:
    print('O valor 5 foi informado')
else:
    print('O valor 5 NÃO consta na lista')
