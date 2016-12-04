import pygame, os, sys

pygame.init()
from buttonclass import button
class startScreen:

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

        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play(loops = -1)
        pygame.mixer.music.set_volume(0.5)

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                   
                    done = True

            titleText = pygame.font.SysFont('Showcard Gothic', 60)
            subText = pygame.font.SysFont('Showcard Gothic', 20)

            text = titleText.render("Arcade City", True, white)
            cs = subText.render("CS110 Final Project", True, white)
            names = subText.render("Aidan Uy, Crystal Low, Danika Gaviola, Dylan Pan", True, white)

            screen.blit(text, [220, 200])
            screen.blit(cs, [310, 265])
            screen.blit(names, [150, 290])

            pos = pygame.mouse.get_pos()
            startButton = button(screen, green, red, 350, 400, 150, 50)
            
            buttonText = pygame.font.SysFont('Showcard Gothic', 30)
            start = buttonText.render("Start!", True, white)
            screen.blit(start,[400,420])
           
            if 500 > pos[0] > 350 and 450 > pos[1] > 400:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    from instructions.py import instructionScreen

            pygame.display.update()

            clock.tick(60)

def main():
    startScreen()

main()
