import pygame, os, sys
pygame.init()

class instructionScreen:

    def __init__(self):
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

        background = pygame.image.load("background.png").convert()
        screen.blit(background, [0, 0])
        caption = pygame.image.load("caption.png").convert()
        oak = pygame.image.load("oak.png").convert()
        oak.set_colorkey(black)
        screen.blit(oak, [570, 130])

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    done = True

            titleText = pygame.font.SysFont('Showcard Gothic', 60)

            text = titleText.render("Instructions", True, white)

            screen.blit(text, [200, 80])

            mouse = pygame.mouse.get_pos()

            if 480 > mouse[0] > 325 and 550 > mouse[1] > 500:
                pygame.draw.rect(screen, bright_green, (325, 500, 150, 50))
            else:
                pygame.draw.rect(screen, green, (325, 500, 150, 50))

            buttonText = pygame.font.SysFont('Showcard Gothic', 30)

            screen.blit(caption, [3, 300])
            pygame.draw.rect(screen, white, (45, 320, 670, 110))

            play = buttonText.render("Play!", True, white)
            screen.blit(play, [357, 515])

            if 480 > mouse[0] > 325 and 550 > mouse[1] > 500:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    from gamescreen.py import gamescreen

            pygame.display.update()

            clock.tick(60)

def main():
    instructionScreen()

main()
