import pygame, os, sys
pygame.init()
from buttonClass import button
from spriteClass import gameSprite

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

    character = gameSprite()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True

        screen.fill(black)

        myButton = button(screen, green, red, 100, 200, 100, 70)

        if myButton.rect.colliderect(character):
            print("COLLISION")

        character.update()
        character.draw(screen)

        pygame.display.update()

        clock.tick(60)

main()
