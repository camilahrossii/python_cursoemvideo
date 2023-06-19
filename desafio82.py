numeros = list()
pares = list()
impares = list()
valor = 0
while True:
    valor = int(input('Digite um número: '))
    numeros.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    print('Valor adicionado com sucesso...')
    resp = str(input('Quer continuar? [S/N]  ')).upper()[0]
    if resp == 'N':
        break
numeros.sort()
pares.sort()
impares.sort()
print(f'Lista Completa: {numeros}')
print(f'Lista de Valores Pares: {pares}')
print(f'Lista de Valores Ímpares: {impares}')