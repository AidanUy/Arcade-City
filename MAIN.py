import pygame, os, sys
from startscreen import startScreen
pygame.init()

def main():
    startScreen()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                pygame.display.quit()
                done = True

main()
