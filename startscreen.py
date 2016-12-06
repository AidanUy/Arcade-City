import pygame
import sys
import os
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

class startScreen:

    def __init__(self):
        size = [800, 600]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Arcade City")

        clock = pygame.time.Clock()

        background = pygame.image.load("background.png").convert()
        screen.blit(background, [0, 0])

        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play(loops = -1)
        pygame.mixer.music.set_volume(0.5)

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    done = True

            titleText = pygame.font.SysFont('Showcard Gothic', 60)
            subText = pygame.font.SysFont('Showcard Gothic', 20)

            text = titleText.render("Arcade City", True, white)
            cs = subText.render("CS110 Final Project", True, white)
            names = subText.render("Aidan Uy, Crystal Low, Danika Gaviola, Dylan Pan", True, white)

            screen.blit(text, [220, 200])
            screen.blit(cs, [310, 265])
            screen.blit(names, [150, 290])

            startButton = button(screen, green, bright_green, 350, 400, 150, 50)
            playPos = startButton.mouse
            buttonText = pygame.font.SysFont('Showcard Gothic', 30)

            start = buttonText.render("Start!", True, white)
            screen.blit(start, [373, 413])

            if 500 > playPos[0] > 350 and 450 > playPos[1] > 400:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    from instructions import instructionScreen

            pygame.display.update()

            clock.tick(60)
