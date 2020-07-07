import pygame
import time

def main():

    pygame.init()

    # load and set the logo
    logo = pygame.image.load("logo32x32.jpg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((240,180))

    image = pygame.image.load("image.jpg")
    screen.blit(image, dest=(50,50))
    pygame.display.flip()
    
    time.sleep(5)
    pygame.quit() 


if __name__ == "__main__":
    main()