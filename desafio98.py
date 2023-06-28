from time import sleep
def contador(inicio, fim, passo):
    if passo < 0 :
        passo *= -1
    if passo == 0:
        passo = 10
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(.5)
            cont -= passo
        print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início:'))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
