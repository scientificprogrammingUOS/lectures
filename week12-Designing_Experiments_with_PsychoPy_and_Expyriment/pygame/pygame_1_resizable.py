import os
import pygame
from pygame.locals import *

killevent = lambda event: event.type == pygame.QUIT or (event.type is pygame.KEYDOWN and event.key == pygame.K_ESCAPE)

pygame.init()
screen = pygame.display.set_mode((500, 500), HWSURFACE | DOUBLEBUF | RESIZABLE)

while True:
    pygame.event.pump()
    event = pygame.event.wait()
    if killevent(event):
        pygame.quit()
        break
    elif event.type == VIDEORESIZE:
        screen = pygame.display.set_mode(
            event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
        screen.blit(pygame.transform.scale(pic, event.dict['size']), (0, 0))
        pygame.display.flip()