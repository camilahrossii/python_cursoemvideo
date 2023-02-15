# Faça um programa em Python que abra e reproduza o aúdio de arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('desafio18.mp3')
pygame.mixer.music.play()
pygame.event.wait()
