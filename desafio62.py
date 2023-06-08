# Melhore o DESAFIO 61, perguntando ao usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0.

primeiro = int(input('Digite um número: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('~ Progressão finalizada com {} termos mostrados.'.format(total))