import pygame, os, sys
from buttonclass import button

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
bright_red = (255, 0, 0)

green = (0, 200, 0)
bright_green = (0, 255, 0)

blue = (0, 0, 200)
bright_blue = (0, 0, 255)

class startScreen:

    def __init__(self):
        size = [800, 600]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Arcade City")

        clock = pygame.time.Clock()

        background = pygame.image.load("mainscreen.png").convert()
        screen.blit(background, [0, 0])

        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play(loops = -1)
        pygame.mixer.music.set_volume(0.5)

        titleText = pygame.font.SysFont('Showcard Gothic', 60)
        subText = pygame.font.SysFont('Showcard Gothic', 20)

        text = titleText.render("Arcade City", True, white)
        cs = subText.render("CS110 Final Project", True, white)
        names = subText.render("Aidan Uy, Crystal Low, Danika Gaviola, Dylan Pan", True, white)

        screen.blit(text, [218, 200])
        screen.blit(cs, [310, 265])
        screen.blit(names, [150, 290])

        startButton = button(screen, green, 330, 400, 150, 50)

        buttonText = pygame.font.SysFont('Showcard Gothic', 30)
        start = buttonText.render("Start!", True, white)
        screen.blit(start, [353, 410])

        ticketReset = open("tickets.txt", "w")
        ticketReset.write("0")
        ticketReset.close()

        pygame.display.update()

        clock.tick(60)
