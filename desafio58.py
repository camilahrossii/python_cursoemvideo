# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0,10)
print('Olá, Sou seu computador. Acabei de pensar em um número de 0 a 10.')
print('Será que você consegue acertar? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos... Tente outra vez: ')
        elif jogador < computador:
            print('Mais... Tente outra vez: ')
print('Você acertou com {} tentativas. Parabéns!'.format(palpite))
