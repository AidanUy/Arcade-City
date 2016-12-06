import random
import pygame
import os
import sys
from buttonclass import button
pygame.init()

#correct = False
#tickets = 0

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
bright_red = (255, 0, 0)

green = (0, 200, 0)
bright_green = (0, 255, 0)

blue = (0, 0, 200)
bright_blue = (0, 0, 255)

class higherOrLower:
    #def getRandNum():
        #num = random.randrange(20)
        #return(num)

    def __init__(self): #and tickets
        size = [800, 600]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Arcade City")

        clock = pygame.time.Clock()

        currentNum = random.randrange(20)

        wins = 0
        tickets = 0

        background = pygame.image.load("background.png").convert()
        screen.blit(background, [0,0])
        caption = pygame.image.load("caption.png").convert()
        oak = pygame.image.load("oak.png").convert()
        oak.set_colorkey(black)
        screen.blit(oak, [570, 130])

        done = False
        while (wins < 3 and wins > -1 or done == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    done = True

            titleText = pygame.font.SysFont('Showcard Gothic', 60)
            subText = pygame.font.SysFont('Showcard Gothic', 25)

            text = titleText.render("Higher or Lower", True, white)
            p1 = subText.render("My number is " + str(currentNum), True, black)
            p2 = subText.render("Will my next number be higher or lower?", True, black)
            p3 = subText.render("Correct!",True, black)
            p4 = subText.render("Game over", True, black)
            pWin = subText.render("You win! Here is your ticket!", True, black)
            pLose = subText.render("You lose. Try again later!", True, black)

            screen.blit(text, [200, 80])

            higherButton = button(screen, green, bright_green, 325, 500, 150, 50)
            higherPos = higherButton.mouse

            buttonText = pygame.font.SysFont('Showcard Gothic', 30)

            screen.blit(caption, [3, 300])
            pygame.draw.rect(screen, white, (45, 320, 670, 110))

            print("My number is " + str(currentNum)) #p1
            newNum = random.randrange(20)
            print("For debuging num is" + str(newNum))
            hOrL = input("Will my next number be higher or lower? (\"h\" or \"l\")")#p2

            if (not(newNum == currentNum)):
                if (hOrL == "h" or hOrL == "H"):
                    if(newNum >= currentNum):
                        print("Correct!")#p3
                        wins += 1
                        currentNum = newNum
                    else:
                        print("Game Over")#p4
                        wins = -1
                elif (hOrL == "l" or hOrL == "L"):
                    if(newNum <= currentNum):
                        print("Correct!")#p3
                        wins += 1
                        currentNum = newNum
                    else:
                        print("Game Over")#p4
                        wins = -1
                else:
                    print("Invalid response.")
            if(wins == 3):
                print("You win! Here is your ticket!")
                tickets += 1
                return(tickets)
            elif(wins == -1):
                print("You lose. Try again later!")
                return(tickets)

            pygame.display.update()

            clock.tick(60)

def main():
    print("Welcome to Higher or Lower!")
    print("I will tell you a number.")
    print("You will then need to guess if the next number is higher or lower.")
    print("If you guess correctly 3 times in a row, you win a ticket!")
    tickets = higherOrLower()
    print("You now have " + str(tickets) + " tickets.")

main()
