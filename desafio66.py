soma = cont = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Você digitou {cont} números e', end='')
print(f' a soma dos números informado é {soma}')