#Operation 3067
#A game that involves exploration, building, and attack.
#Written by vanquished
#Licenced under the GPL v3 licence.

VERSION = "0.1"

try:
    import pygame, sys
    from pygame.locals import *
except ImportError, err:
    print "Could not load module. {0}".format(err)

def main():
    #Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 540))
    pygame.display.set_caption("Operation 3067 version "+ VERSION)
    
    #Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((1, 136, 186))
    # Rest of code down here
    screen.blit(background, (0,0))
    pygame.display.flip()
    #The main loop
    while True:
        #events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        #state
        #draw on screen
        
if __name__ == "__main__":
    main()
