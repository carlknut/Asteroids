# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    
    # Prints game announcement
    print("Starting Asteroids!")
    print("Screen width: 1280: " + str(SCREEN_WIDTH) )
    print("Screen height: 720" + str(SCREEN_HEIGHT) )

    # Initializing game assests
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    

    # Groups
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updateables,drawables)

    Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    # Infinite game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateables.update(dt)

        screen.fill( (0,0,0) )
        
        for d in drawables:
            d.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) /1000

if __name__ == "__main__":
    main()