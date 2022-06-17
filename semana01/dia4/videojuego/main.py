import pygame
import sys
pantalla = pygame.display.set_mode((648,480))

while True:
    ##Revisar todos los eventos dentro de pygame
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
    
    pygame.display.flip()