import pygame

def main():

    pygame.init()

    # load and set the logo
    logo = pygame.image.load("logo32x32.jpg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    modes = pygame.display.list_modes(0, pygame.FULLSCREEN)
    screen=pygame.display.set_mode(modes[0], pygame.FULLSCREEN)
    
    
    # define a variable to control the main loop
    running = True

    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            
            if (event.type is pygame.KEYDOWN and event.key == pygame.K_f):
                if screen.get_flags() & pygame.FULLSCREEN:
                    pygame.display.set_mode(modes[0])
                else:
                    pygame.display.set_mode(modes[0], pygame.FULLSCREEN)
        
            # only do something if the event is of type QUIT (meaning you click the [x] or press ALT-F4)
            if event.type == pygame.QUIT or (event.type is pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                # change the value to False, to exit the main loop
                running = False
                pygame.quit() #only necessary if you run it in Jupyter


if __name__=="__main__":
    main()
