valores = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado, não vou adicionar.')
    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp in 'SN':
        if resp == 'N':
            break
print('=-'*30)
valores.sort()
print(f'Você digitou os valores {valores}')