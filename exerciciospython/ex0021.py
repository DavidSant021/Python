import pygame
pygame.mixer.init()
pygame.mixer.music.load('21.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue
    pygame.quit()
