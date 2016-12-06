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

class instructionScreen:

    def __init__(self):
        size = [800, 600]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Arcade City")

        clock = pygame.time.Clock()

        background = pygame.image.load("background.png").convert()
        screen.blit(background, [0, 0])
        caption = pygame.image.load("caption.png").convert()
        oak = pygame.image.load("oak.png").convert()
        oak.set_colorkey(black)
        screen.blit(oak, [570, 130])

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    done = True

            titleText = pygame.font.SysFont('Showcard Gothic', 60)
            subText = pygame.font.SysFont('Showcard Gothic', 25)

            text = titleText.render("Instructions", True, white)
            captionText = subText.render("Hey! Welcome to Arcade City! Start by walking up", True, black)
            captionText2 = subText.render("to and playing Higher or Lower and racking up", True, black)
            captionText3 = subText.render("tickets. Then, when you get enough tickets,", True, black)
            captionText4 = subText.render("different games will be unlocked. Have fun!", True, black)

            screen.blit(text, [200, 80])

            playButton = button(screen, green, bright_green, 325, 500, 150, 50)
            playPos = playButton.mouse

            buttonText = pygame.font.SysFont('Showcard Gothic', 30)

            screen.blit(caption, [3, 300])
            pygame.draw.rect(screen, white, (45, 320, 670, 110))

            screen.blit(captionText, [45, 325])
            screen.blit(captionText2, [45, 350])
            screen.blit(captionText3, [45, 375])
            screen.blit(captionText4, [45, 400])

            play = buttonText.render("Play!", True, white)
            screen.blit(play, [357, 515])

            if 480 > playPos[0] > 325 and 550 > playPos[1] > 500:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    from gamescreen.py import gamescreen

            pygame.display.update()

            clock.tick(60)
