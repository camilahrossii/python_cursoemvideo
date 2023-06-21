lista = [[], []]
for n in range(1, 8):
    num = int(input(f'Digite o {n}º número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print('=-' * 30)
print(f'Os valores PARES digitados foram: {lista[0]}')
print(f'Os valores ÍMPARES digitados foram: {lista[1]}')