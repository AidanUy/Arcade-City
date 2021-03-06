import pygame, os, sys
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

class rockPaperScissorsScissors:

    def __init__(self):
        size = [800, 600]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Arcade City")

        clock = pygame.time.Clock()

        background = pygame.image.load("rockpaperscissorsbg.png").convert()
        screen.blit(background, [0, 0])

        from random import randint

        t = ["Rock", "Paper", "Scissors"]

        computer = t[randint(0,2)]

        subText = pygame.font.SysFont('Showcard Gothic', 50)
        smallText = pygame.font.SysFont('Showcard Gothic', 20)
        midText = pygame.font.SysFont('Showcard Gothic', 30)

        player = "Scissors"
        if computer == "Scissors":
            cs = midText.render("Tie!", True, blue)
            screen.blit(cs, [385, 260])
        if computer == "Rock":
            cs = midText.render("You lose! Rock smashes scissors.", True, blue)
            screen.blit(cs, [165, 260])
            tickLose = -10
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
        if computer == "Paper":
            cs = midText.render("You win! Scissors cuts paper.", True, blue)
            screen.blit(cs, [165, 260])
            tickWin = 30
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

        backButton = button(screen, green, 343, 411, 150, 50)
        backText = midText.render("Back", True, white)
        screen.blit(backText, [380, 426])

        pygame.display.update()

        clock.tick(60)
