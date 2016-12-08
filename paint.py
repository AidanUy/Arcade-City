import pygame
from pygame.locals import *
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


window = pygame.display.set_mode((width,height))
canvas = window.copy()
canvas.fill(WHITE)
while True:
    left_pressed = mouse.get_pressed
    middle_pressed = mouse.get_pressed
    right_pressed = mouse.get_pressed
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif left_pressed:
            pygame.draw.circle(canvas, BLACK, (pygame.mouse.get_pos()), 5)

    window.fill(WHITE)
    window.blit(canvas, (0,0))
    pygame.draw.circle(window, BLACK, (pygame.mouse.get_pos()), 5)
    pygame.display.update()
