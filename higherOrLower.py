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

class higherOrLower:

    def __init__(self, currentNum):
        size = [800, 600]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Arcade City")

        clock = pygame.time.Clock()

        background = pygame.image.load("background.png").convert()
        screen.blit(background, [0,0])
        caption = pygame.image.load("caption.png").convert()
        oak = pygame.image.load("oak.png").convert()
        oak.set_colorkey(black)
        screen.blit(oak, [570, 110])

        titleText = pygame.font.SysFont('Showcard Gothic', 60)
        subText = pygame.font.SysFont('Showcard Gothic', 25)
        buttonText = pygame.font.SysFont('Showcard Gothic', 30)

        text = titleText.render("Higher or Lower", True, white)
        screen.blit(text, [140, 50])

        screen.blit(caption, [3, 280])
        pygame.draw.rect(screen, white, (45, 300, 670, 110))

        higherButton = button(screen, blue, bright_blue, 150, 450, 150, 50)
        lowerButton = button(screen, blue, bright_blue, 515, 450, 150, 50)
        backButton = button(screen, red, bright_blue, 330, 525, 150, 50)

        line1 = subText.render(("My number is " + str(currentNum) + "."), True, black)
        line2 = subText.render("Will my next number be higher or lower?", True, black)
        screen.blit(line1, [50, 300])
        screen.blit(line2, [50, 330])

        higherText = buttonText.render("Higher", True, white)
        lowerText = buttonText.render("Lower", True, white)
        backText = buttonText.render("Back", True, white)
        screen.blit(higherText, [166, 460])
        screen.blit(lowerText, [535, 460])
        screen.blit(backText, [365, 535])

        pygame.display.update()

        clock.tick(60)
