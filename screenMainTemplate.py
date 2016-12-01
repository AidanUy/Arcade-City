import pygame, os, sys
pygame.init()

def main():
    size = [800, 600]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Arcade City")

    black = (0, 0, 0)
    white = (255, 255, 255)

    red = (200, 0, 0)
    bright_red = (255, 0, 0)

    green = (0, 200, 0)
    bright_green = (0, 255, 0)

    blue = (0, 0, 200)
    bright_blue = (0, 0, 255)

    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True

        # ---------CODE GOES HERE---------

        pygame.display.update()

        clock.tick(60)
