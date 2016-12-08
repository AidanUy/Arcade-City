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

class rockPaperScissorsPaper:

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

        subText = pygame.font.SysFont('Showcard Gothic', 50)
        smallText = pygame.font.SysFont('Showcard Gothic', 20)
        midText = pygame.font.SysFont('Showcard Gothic', 30)

        player = "Paper"
        if computer == "Paper":
            cs = midText.render("Tie!", True, white)
            screen.blit(cs, [385, 260])
        if computer == "Scissors":
            cs = midText.render("You lose! Scissors cuts paper.", True, white)
            screen.blit(cs, [165, 260])
            tickLose = -5
            ticketFile = open("tickets.txt", "r")
            tickets = ticketFile.read()
            tickets = int(tickets) + tickLose
            if tickets <= 0:
                tickets = 0
            ticketFile.close()
            ticketUpdate = open("tickets.txt", "w")
            ticketUpdate.write(str(tickets))
            ticketUpdate.close()
        if computer == "Rock":
            cs = midText.render("You win! Paper covers rock.", True, white)
            screen.blit(cs, [165, 260])
            tickWin = 10
            ticketFile = open("tickets.txt", "r")
            tickets = ticketFile.read()
            tickets = int(tickets) + tickWin
            if tickets <= 0:
                tickets = 0
            ticketFile.close()
            ticketUpdate = open("tickets.txt", "w")
            ticketUpdate.write(str(tickets))
            ticketUpdate.close()

        nextButton = button(screen, green, bright_green, 343, 411, 150, 50)
        nextText = midText.render("Next", True, white)
        screen.blit(nextText, [380, 426])

        pygame.display.update()

        clock.tick(60)
