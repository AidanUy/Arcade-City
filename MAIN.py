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
    start_screen = True
    instructions_screen = True
    var1 = True
    var2 = True
    var3 = True
    isRPS = False
    done = False
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()

                if 500 > mouse[0] > 350 and 450 > mouse[1] > 400 and start_screen:
                    start_screen = False
                    instructionScreen()

                elif 475 > mouse[0] > 325 and 550 > mouse[1] > 500 and instructions_screen and not start_screen:
                    instructions_screen = False
                    gameScreen()

                elif 210 > mouse[0] > 100 and 455 > mouse[1] > 205 and not instructions_screen and var2 and not isRPS:
                    var2 = False
                    var3 = True
                    isRPS = True
                    rockPaperScissors()
                    
                elif 480 > mouse[0] > 330 and 575 > mouse[1] > 525 and not var2 and isRPS and var3:
                    var2 = True
                    var3 = False
                    isRPS = False
                    gameScreen()
                    
                elif 280 > mouse[0] > 130 and 500 > mouse[1] > 450 and not var2 and isRPS and var3:
                    var3 = False
                    rockPaperScissorsRock()

                elif 493 > mouse[0] > 343 and 461 > mouse[1] > 411 and not var2 and isRPS:
                    var3 = True
                    rockPaperScissors()
                    
                elif 480 > mouse[0] > 330 and 500 > mouse[1] > 450 and not var2 and isRPS and var3:
                    var3 = False
                    rockPaperScissorsPaper()

                elif 493 > mouse[0] > 343 and 461 > mouse[1] > 411 and not var2 and isRPS:
                    var3 = True
                    rockPaperScissors()

                elif 680 > mouse[0] > 530 and 500 > mouse[1] > 450 and not var2 and isRPS and var3:
                    var3 = False
                    rockPaperScissorsScissors()

                elif 493 > mouse[0] > 343 and 461 > mouse[1] > 411 and not var2 and isRPS:
                    var3 = True
                    rockPaperScissors()


                    
main()
