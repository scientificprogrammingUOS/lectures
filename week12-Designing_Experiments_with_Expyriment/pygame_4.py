# %load pygame_4.py
import pygame
import time

killevent = lambda event: event.type == pygame.QUIT or (event.type is pygame.KEYDOWN and event.key == pygame.K_ESCAPE)

def main():

    pygame.init()

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((800, 600))

    image = pygame.image.load("smiley.jpg")
    image.set_colorkey((255,255,255)) #this color is now transparent

    xpos = 50
    ypos = 50
    step_x = 10
    step_y = 10


    while True:
        if xpos > screen.get_width()-image.get_width() or xpos <= 0: step_x *= -1
        if ypos > screen.get_height()-image.get_height() or ypos <= 0: step_y *= -1
        xpos += step_x 
        ypos += step_y
        screen.fill((0,0,0))
        screen.blit(image, (xpos, ypos))
        pygame.display.flip()
        time.sleep(0.01)
        if any(killevent(event) for event in pygame.event.get()):
            break
            
    pygame.quit()


if __name__ == "__main__":
    main()
