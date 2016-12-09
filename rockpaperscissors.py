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

class rockPaperScissors:

    def __init__(self):
        size = [800, 600]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Arcade City")

        clock = pygame.time.Clock()

        subText = pygame.font.SysFont('Showcard Gothic', 50)
        smallText = pygame.font.SysFont('Showcard Gothic', 20)
        midText = pygame.font.SysFont('Showcard Gothic', 30)

        names = subText.render("Rock, Paper, or Scissors?", True, white)
        screen.blit(names, [80, 100])

        rockButton = button(screen, green, 130, 450, 150, 50)
        paperButton = button(screen, green, 330, 450, 150, 50)
        scissorsButton = button(screen, green, 530, 450, 150, 50)
        backButton = button(screen, bright_red, 330, 525, 150, 50)

        rock = smallText.render("Rock", True, white)
        screen.blit(rock, [180, 465])

        paper = smallText.render("Paper", True, white)
        screen.blit(paper, [373, 465])

        scissors = smallText.render("Scissors", True, white)
        screen.blit(scissors, [563, 465])

        back = smallText.render("Back", True, white)
        screen.blit(back, [380, 540])

        pygame.display.update()

        clock.tick(60)
