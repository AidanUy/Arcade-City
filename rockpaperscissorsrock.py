import pygame, os, sys
pygame.init()
from buttonclass import button

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
bright_red = (255, 0, 0)

green = (0, 200, 0)
bright_green = (0, 255, 0)

blue = (0, 0, 200)
bright_blue = (0, 0, 255)

class rockPaperScissorsRock:

    def __init__(self):
        size = [800, 600]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Arcade City")


        clock = pygame.time.Clock()

        from random import randint

        #create a list of play options
        t = ["Rock", "Paper", "Scissors"]

        #assign a random play to the computer
        computer = t[randint(0,2)]


        clock = pygame.time.Clock()

        screen.fill(black)



        subText = pygame.font.SysFont('Showcard Gothic', 50)
        smallText = pygame.font.SysFont('Showcard Gothic', 20)
        midText = pygame.font.SysFont('Showcard Gothic', 30)


        player = "Rock"
        if computer == "Rock":
            cs = midText.render("Tie!", True, white)
        if computer == "Paper":
            cs = midText.render("You lose! Paper covers rock.", True, white)
        if computer == "Scissors":
            cs = midText.render("You win! Rock smashes scissors.", True, white)

        screen.blit(cs, [165, 260])

        nextButton = button(screen, green, bright_green, 343, 411, 150, 50)

        pygame.display.update()

        clock.tick(60)

