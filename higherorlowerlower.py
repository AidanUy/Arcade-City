import pygame, os, sys, random
from buttonclass import button
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
bright_red = (255, 0, 0)

green = (0, 200, 0)
bright_green = (0, 255, 0)

blue = (0, 0, 200)
bright_blue = (0, 0, 255)

class higherOrLowerLower:

    def __init__(self, currentNum):
        size = [800, 600]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Arcade City")

        clock = pygame.time.Clock()

        background = pygame.image.load("bggamescreen.png").convert()
        screen.blit(background, [0, 0])
        caption = pygame.image.load("caption.png").convert()
        instructgirlimg = pygame.image.load("instructgirl.png").convert()
        instructgirl = pygame.transform.scale(instructgirlimg, (200, 200))
        instructgirl.set_colorkey(black)
        screen.blit(instructgirl, [70, 90])

        newNum = random.randrange(30)

        titleText = pygame.font.SysFont('Showcard Gothic', 60)
        subText = pygame.font.SysFont('Showcard Gothic', 25)
        buttonText = pygame.font.SysFont('Showcard Gothic', 30)

        text = titleText.render("Higher or Lower", True, white)
        screen.blit(text, [140, 50])

        screen.blit(caption, [3, 280])
        pygame.draw.rect(screen, white, (45, 300, 670, 110))

        backButton = button(screen, blue, 330, 475, 150, 50)

        backText = buttonText.render("Back", True, white)
        screen.blit(backText, [365, 485])

        winText = subText.render(("Correct!  The number was " + str(newNum) + ".  Here are your tickets."),True, black)
        loseText = subText.render(("You lost.  The number was " + str(newNum) + ". Try again later!"), True, black)

        if newNum <= currentNum:
            screen.blit(winText, [50, 300])
            tickWin = 10
            ticketFile = open("tickets.txt", "r")
            tickets = ticketFile.read()
            tickets = int(tickets) + tickWin
            if tickets <= 0:
                tickets = 0
            elif tickets >= 1000:
                tickets = 1000
            ticketFile.close()
            ticketUpdate = open("tickets.txt", "w")
            ticketUpdate.write(str(tickets))
            ticketUpdate.close()
        elif newNum > currentNum:
            screen.blit(loseText, [50, 300])
            tickLose = -5
            ticketFile = open("tickets.txt", "r")
            tickets = ticketFile.read()
            tickets = int(tickets) + tickLose
            if tickets <= 0:
                tickets = 0
            elif tickets >= 1000:
                tickets = 1000
            ticketFile.close()
            ticketUpdate = open("tickets.txt", "w")
            ticketUpdate.write(str(tickets))
            ticketUpdate.close()

        pygame.display.update()

        clock.tick(60)
