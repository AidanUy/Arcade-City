import pygame, os, sys
from startscreen import startScreen
from instructions import instructionScreen
pygame.init()

def main():
    done = False
    while not done:
        startScreen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True

            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 500 > mouse[0] > 350 and 450 > mouse[1] > 400:
                    return instructionScreen()
                    if 480 > mouse[0] > 325 and 550 > mouse[1] > 500:
                        print("hello")

        pygame.display.update()

main()
