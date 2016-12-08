import pygame, os, sys
from buttonclass import button
from startscreen import startScreen
from instructions import instructionScreen
from gamescreen import gameScreen
from rockpaperscissors import rockPaperScissors
from rockpaperscissorsrock import rockPaperScissorsRock
from rockpaperscissorspaper import rockPaperScissorsPaper
from rockpaperscissorsscissors import rockPaperScissorsScissors
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
    var1 = True
    var2 = True
    done = False
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()

                if 500 > mouse[0] > 350 and 450 > mouse[1] > 400 and var1:
                    var1 = False
                    instructionScreen()

                elif 475 > mouse[0] > 325 and 550 > mouse[1] > 500 and not var1:
                    var1 = False
                    gameScreen()

                elif 210 > mouse[0] > 100 and 455 > mouse[1] > 205:
                    var2 = False
                    rockPaperScissors()

                elif 280 > mouse[0] > 130 and 500 > mouse[1] > 450 and not var2:
                    var2 = False
                    rockPaperScissorsRock()
                    
                elif 480 > mouse[0] > 330 and 500 > mouse[1] > 450 and not var2:
                    var = False
                    rockPaperScissorsPaper()

                elif 680 > mouse[0] > 530 and 500 > mouse[1] > 450 and not var2:
                    var = False
                    rockPaperScissorsScissors()
main()
