import pygame, os, sys, random
from buttonclass import button
from startscreen import startScreen
from instructions import instructionScreen
from gamescreen import gameScreen
from rockpaperscissors import rockPaperScissors
from rockpaperscissorsrock import rockPaperScissorsRock
from rockpaperscissorspaper import rockPaperScissorsPaper
from rockpaperscissorsscissors import rockPaperScissorsScissors
from higherOrLower import higherOrLower
from higherorlowerhigher import higherOrLowerHigher
from higherorlowerlower import higherOrLowerLower
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

    #variable used to make buttons functional only on the start screen
    start_screen = True
    #variable used to make buttons functional only on the instructions screen
    instructions_screen = True
    #variable used to make buttons functional only on the game screen
    var2 = True
    #variables used to make buttons functional on rock paper scissors and loop
    var3 = True
    #variable used to make the higher lower button functional on the game screen
    var4 = True
    #variable used to make higher and lower buttons loop
    var5 = True
    #variable used to make buttons functional only on higher and lower
    higher_lower = False
    #variable used to make buttons functional when rock paper scissors is running
    isRPS = False

    done = False

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True



            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()

                #Creates a button on the start screen that calls the instructions screen when clicked
                if 500 > mouse[0] > 350 and 450 > mouse[1] > 400 and start_screen:
                    start_screen = False
                    instructionScreen()

                #Creates a button on the instructions screen that calls the game screen when clicked
                elif 475 > mouse[0] > 325 and 550 > mouse[1] > 500 and instructions_screen and not start_screen:
                    instructions_screen = False
                    gameScreen()

                #Creates a clickable area underneath the image of a building that calls the rock paper scissors screen when clicked
                elif 210 > mouse[0] > 100 and 455 > mouse[1] > 205 and not instructions_screen and var2 and not isRPS:
                    var2 = False
                    var3 = True
                    isRPS = True
                    rockPaperScissors()

                #Creates a button that returns you to the game screen when clicked
                elif 480 > mouse[0] > 330 and 575 > mouse[1] > 525 and not var2 and isRPS and var3:
                    var2 = True
                    var3 = False
                    isRPS = False
                    gameScreen()

                #Creates a button that takes you to the outcomes if the player chose rock
                elif 280 > mouse[0] > 130 and 500 > mouse[1] > 450 and not var2 and isRPS and var3:
                    var3 = False
                    rockPaperScissorsRock()

                #Creates a button that takes you to the rock paper scissors screen from the outcome screen of rock
                elif 493 > mouse[0] > 343 and 461 > mouse[1] > 411 and not var2 and isRPS:
                    var3 = True
                    rockPaperScissors()

                #Creates a button that takes you to the outcomes if the player chose paper
                elif 480 > mouse[0] > 330 and 500 > mouse[1] > 450 and not var2 and isRPS and var3:
                    var3 = False
                    rockPaperScissorsPaper()

                #Creates a button that takes you to the rock paper scissors screen from the outcome screen of paper
                elif 493 > mouse[0] > 343 and 461 > mouse[1] > 411 and not var2 and isRPS:
                    var3 = True
                    rockPaperScissors()

                #Creates a button that takes you to the outcomes if the player chose scissors
                elif 680 > mouse[0] > 530 and 500 > mouse[1] > 450 and not var2 and var3 and isRPS:
                    var3 = False
                    rockPaperScissorsScissors()

                #Creates a button that takes you to the rock paper scissors screen from the outcome screen of scissors
                elif 493 > mouse[0] > 343 and 461 > mouse[1] > 411 and not var2 and isRPS:
                    var3 = True
                    rockPaperScissors()

                #Creates a clickable area underneath the image of a building that calls the higher or lower screen
                elif 360 > mouse[0] > 250 and 455 > mouse[1] > 205 and not instructions_screen and var2 and var4 and not isRPS:
                    ticketFile = open("tickets.txt", "r")
                    tickets = ticketFile.read()
                    if int(tickets) >= 30:
                        var2 = False
                        var4 = False
                        var5 = True
                        higher_lower = True
                        currentNum = random.randrange(30)
                        higherOrLower(currentNum)
                    ticketFile.close()

                #Creates a button on the higher or lower screen that takes you back to the gamescreen when clicked
                elif 480 > mouse[0] > 330 and 575 > mouse[1] > 525 and not instructions_screen and not var2 and not var4 and var5 and not isRPS and higher_lower:
                    var2 = True
                    var4 = True
                    var5 = False
                    higher_lower = False
                    gameScreen()

                #Creates a button on the higher or lower screen that takes you to the outcome screen of higher when clicked
                elif 300 > mouse[0] > 150 and 500 > mouse[1] > 450 and not instructions_screen and not var2 and not var4 and var5 and not isRPS and higher_lower:
                    var5 = False
                    higherOrLowerHigher(currentNum)

                #Creates a button on the higher outcome screen that takes you back to the higher or lower screen when clicked
                elif 480 > mouse[0] > 330 and 525 > mouse[1] > 475 and not instructions_screen and not var2 and not var4 and not var5 and not isRPS and higher_lower:
                    var5 = True
                    currentNum = random.randrange(30)
                    higherOrLower(currentNum)

                #Creates a button on the higher or lower screen that takes you to the outcome screen of lower when clicked
                elif 665 > mouse[0] > 515 and 500 > mouse[1] > 450 and not instructions_screen and not var2 and not var4 and var5 and not isRPS and higher_lower:
                    var5 = False
                    currentNum = random.randrange(30)
                    higherOrLowerLower(currentNum)

                #Creates a button on the lower outcome screen that takes you back to the higher or lower screen when clicked
                elif 480 > mouse[0] > 330 and 525 > mouse[1] > 475 and not instructions_screen and not var2 and not var4 and not var5 and not isRPS and higher_lower:
                    var5 = True
                    currentNum = random.randrange(30)
                    higherOrLower(currentNum)


main()
