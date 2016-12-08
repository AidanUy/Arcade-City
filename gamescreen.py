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

class gameScreen:

    def __init__(self):
        size = [800, 600]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Arcade City")

        clock = pygame.time.Clock()

        background = pygame.image.load("gamescreenbg.png").convert()
        screen.blit(background, [0, 0])

        tickets = open("tickets.txt", "r")
        tickets = tickets.read()

        titleText = pygame.font.SysFont('Showcard Gothic', 30)

        ticks = titleText.render(tickets, True, white)
        ticklabel = titleText.render("Tickets", True, white)

        pygame.draw.line(screen, red, [660, 0], [660, 93], 7)
        pygame.draw.line(screen, red, [660, 90], [800, 90], 7)

        screen.blit(ticks, [710, 50])
        screen.blit(ticklabel, [670, 10])

        building1img = pygame.image.load("buildingrps.png").convert()
        building1 = pygame.transform.scale(building1img, (110, 250))

        building2img = pygame.image.load("buildinghl.png").convert()
        building2 = pygame.transform.scale(building2img, (110, 250))

        screen.blit(building1, [100, 205])
        screen.blit(building2, [250, 205])

        pygame.display.update()

        clock.tick(60)
