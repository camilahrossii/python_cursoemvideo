from time import sleep
cor = ( '\033[m',          # 0 - sem cores
        '\033[0;30;41m',   # 1 - vermelho
        '\033[0;30;42m',   # 2 - verde
        '\033[0;30;43m',   # 3 - amarelo
        '\033[0;30;44m',   # 4 - azul
        '\033[0;30;45m',   # 5 - roxo
        '\033[7;30m'       # 6 - branco
         );

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(cor[6], end='')
    help(com)
    print(cor[0], end='')
    sleep(2)


def título(msg, c=0):
    tam = len(msg) + 4
    print(cor[c], end='')
    print('~~' * tam)
    print(msg.center(len(msg)+tam))
    print('~~' * tam)
    print(cor[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
