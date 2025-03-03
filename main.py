# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    
    print("Starting Asteroids!")
    print("Screen width: 1280: " + str(SCREEN_WIDTH) )
    print("Screen height: 720" + str(SCREEN_HEIGHT) )

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(Black)

        display.flip()

if __name__ == "__main__":
    main()