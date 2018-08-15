import pygame
import time


BGCOLOR = (0, 0, 0)
SCREENSIZE = (800, 600)
FONTSIZE = SCREENSIZE[0]//20
FONTCOLOR = (255, 255, 255)

CENTER = 0
NEWLINECENTER = 1
BOTTOM = 3
TOP = 6


def get_position(screen, text_surface, where):
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()
    width = screen.get_width()
    height = screen.get_height()
    if where == CENTER:
        return width/2-text_width/2, height/2-text_height/2
    elif where == NEWLINECENTER:
        return width/2-text_width/2, 5.0/8*height
    elif where == BOTTOM:
        return width/2-text_width/2, height-1.5*text_height
    elif where == TOP:
        return width/2-text_width/2, 1.0/10*height


def main():
    pygame.init()
    screen=pygame.display.set_mode(SCREENSIZE)

    screen.fill(BGCOLOR) #erase texts before
    font = pygame.font.Font(None, FONTSIZE)
    text_surface = font.render("Hello, World!", True, FONTCOLOR, BGCOLOR) #text, antialias, color, background
    posx, posy = get_position(screen, text_surface, TOP)
    screen.blit(text_surface, dest=(posx, posy))
    pygame.display.flip()

    time.sleep(5)


if __name__ == "__main__":
    main()