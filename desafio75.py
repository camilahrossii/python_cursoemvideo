pares = 0
numeros = ( int(input('Digite um número: ')), int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')), int(input('Agora o último número: ')) )
print(f'Você digitou os números: {numeros}')
if 9 in numeros:
    print(f'O número 9 aparece { numeros.count(9) } vezes.')
else:
    print('O número 9 não aparece em nenhuma posição.')
if 3 in numeros:
    print(f'O valor 3 apareceu na { numeros.index(3)+1 }ª posição')
else:
    print('O número 3 não aparece em nenhuma posição.')
print(f'Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f' {n} ', end='')