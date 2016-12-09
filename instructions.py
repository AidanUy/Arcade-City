import pygame, sys, os, random
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
        shopkeeper = pygame.image.load("oak.png").convert()
        shopkeeper.set_colorkey(black)
        screen.blit(shopkeeper, [70, 130])

        titleText = pygame.font.SysFont('Showcard Gothic', 60)
        subText = pygame.font.SysFont('Showcard Gothic', 25)

        text = titleText.render("Instructions", True, white)
        captionText = subText.render("Hey! Welcome to Arcade City! Start by clicking the", True, black)
        captionText2 = subText.render("first building to play Rock Paper Scissors and rack up", True, black)
        captionText3 = subText.render("tickets. Then, when you get 300 tickets,", True, black)
        captionText4 = subText.render("the second building is unlocked. Have fun!", True, black)

        screen.blit(text, [200, 80])

        playButton = button(screen, green, bright_green, 325, 500, 150, 50)

        buttonText = pygame.font.SysFont('Showcard Gothic', 30)

        screen.blit(caption, [3, 300])
        pygame.draw.rect(screen, white, (45, 320, 670, 110))

        screen.blit(captionText, [45, 325])
        screen.blit(captionText2, [45, 350])
        screen.blit(captionText3, [45, 375])
        screen.blit(captionText4, [45, 400])

        play = buttonText.render("Play!", True, white)
        screen.blit(play, [357, 515])

        pygame.display.update()

        clock.tick(60)

