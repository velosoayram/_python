# Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.mixer.init()
pygame.mixer.music.load('/home/veloso/Documentos/GitHub/rep_meus/coding.py/_media/Find Me.mp3')
pygame.mixer.music.play()
print('Enjoy your music!')
while pygame.mixer.music.get_busy():
    pass
