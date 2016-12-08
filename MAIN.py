import pygame, os, sys
from buttonclass import button
from startscreen import startScreen
from instructions import instructionScreen
from gamescreen import gameScreen
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
bright_red = (255, 0, 0)

green = (0, 200, 0)
bright_green = (0, 255, 0)

blue = (0, 0, 200)
bright_blue = (0, 0, 255)

def main():
    size = [800, 600]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Arcade City")

    start = startScreen()
    var = True
    done = False
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse1 = pygame.mouse.get_pos()

                if 500 > mouse1[0] > 350 and 450 > mouse1[1] > 400 and var:
                    var = False
                    instructionScreen()

                elif 475 > mouse1[0] > 325 and 550 > mouse1[1] > 500 and not var:
                    var = False
                    gameScreen()

main()
