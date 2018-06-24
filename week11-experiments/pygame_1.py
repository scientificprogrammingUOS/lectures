import pygame

def main():

    pygame.init()

    # load and set the logo
    logo = pygame.image.load("logo32x32.jpg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((240,180))

    # define a variable to control the main loop
    running = True

    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


if __name__=="__main__":
    main()
