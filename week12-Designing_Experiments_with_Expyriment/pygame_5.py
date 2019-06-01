import pygame
import time
import random


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


def wait_any_key():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                else:
                    return event.key  #returns key numbers
            elif event.type == pygame.QUIT:
                return False


def wait_key(which):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == which:
                    return True
            elif event.type == pygame.QUIT:
                return False


def main():
    pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
    pygame.init()
    screen=pygame.display.set_mode(SCREENSIZE)

    screen.fill(BGCOLOR)
    font = pygame.font.Font(None, FONTSIZE)
    smallfont = pygame.font.Font(None, FONTSIZE*3//4)

    intro_text = font.render("Press <left> for even numbers, and <right> else!", True, FONTCOLOR, BGCOLOR)
    posx, posy = get_position(screen, intro_text, CENTER)
    screen.blit(intro_text, (posx, posy))
    other_text = smallfont.render("Space to continue", True, FONTCOLOR, BGCOLOR)
    posx, posy = get_position(screen, other_text, NEWLINECENTER)
    screen.blit(other_text, (posx, posy))
    pygame.display.flip()

    if not wait_key(pygame.K_SPACE):
        return

    effect = pygame.mixer.Sound('beep.wav')
    num = None
    for i in range(4):
        pre_num = num
        while pre_num == num:
            num = random.randint(1, 9)
        screen.fill(BGCOLOR)
        number = font.render(str(num), True, FONTCOLOR, BGCOLOR)
        posx, posy = get_position(screen, number, CENTER)
        screen.blit(number, (posx, posy))
        pygame.display.flip()
        key = wait_any_key()
        if not key:
            return
        elif (key == pygame.K_LEFT and num % 2 != 0) or (key == pygame.K_RIGHT and num % 2 == 0):
            effect.play()


if __name__ == "__main__":
    main()
