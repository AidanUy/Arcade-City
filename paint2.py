import pygame
from pygame.locals import *
from gamescreen import gameScreen
from buttonclass import button
import sys, os
import time

pygame.init()
pygame.display.set_caption('Paint City')

mouse = pygame.mouse
fpsClock = pygame.time.Clock()

width = 800
height = 600

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
ORANGE = (255,165,0)
YELLOW = (255,255,0)
GREEN = (0,128,0)
BLUE = (0,0,205)
PURPLE = (148,0,211)
PINK = (225,182,193)

class paint:
    def __init__(self):
        pygame.display.set_caption('Paint City')

        mouse = pygame.mouse
        fpsClock = pygame.time.Clock()
        

        width = 800
        height = 600
        size = [800,600]
        screen = pygame.display.set_mode(size)
        
        colors = [BLACK, RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK]
        i = 0
        window = pygame.display.set_mode((width,height))
        canvas = window.copy()
        canvas.fill(WHITE)
        color = colors[i]
        size = 5
        buttonText = pygame.font.SysFont('Showcard Gothic', 30)

        backButton = button(screen, PINK, PURPLE, 20, 20, 20, 100)
        bText = buttonText.render("Back", True, BLACK)
        screen.blit(bText, [25,60])
        while True:
            left_pressed = mouse.get_pressed()
            middle_pressed = mouse.get_pressed()
            c_pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if (event.type == QUIT):
                    pygame.quit()
                    sys.exit()
                elif (left_pressed):
                    pygame.draw.circle(canvas, color, (pygame.mouse.get_pos()), size)
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_c):
                        i += 1
                        if (i >= len(colors)):
                            i = 0
                        color = colors[i]
                    if (event.key == pygame.K_LEFT):
                        size -= 1
                        if (size <= 1):
                            size = 1
                    if (event.key == pygame.K_RIGHT):
                        size += 1

            window.fill(WHITE)
            window.blit(canvas, (0,0))
            pygame.display.update()

