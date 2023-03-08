# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário descobrir
# qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usúario venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
print('Você disse {} e eu pensei no {}.'.format(jogador,computador))
if computador == jogador:
    print('PARABÈNS! Você venceu!!')
else:
    print('Você ERROU e eu GANHEI!'.format(computador))
