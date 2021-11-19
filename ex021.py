#Faça um programa em python que abra e reproduza um audio de um arquivo mp3.
print()
print('='*25,'DESAFIO 021','='*25)
import pygame
pygame.init()
pygame.mixer.music.load('late.mp3')
pygame.mixer.music.play()
pygame.event.wait()

