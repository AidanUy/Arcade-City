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


class rockPaperScissorsScissors:

    def __init__(self):
        size = [800, 600]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Arcade City")



        done = False

        clock = pygame.time.Clock()

        from random import randint

        #create a list of play options
        t = ["Rock", "Paper", "Scissors"]

        #assign a random play to the computer
        computer = t[randint(0,2)]

        done = False

        clock = pygame.time.Clock()

        screen.fill(black)

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    done = True

            subText = pygame.font.SysFont('Showcard Gothic', 50)
            smallText = pygame.font.SysFont('Showcard Gothic', 20)
            midText = pygame.font.SysFont('Showcard Gothic', 30)

            player = "Scissors"
            if computer == "Scissors":
                cs = midText.render("Tie!", True, white)
            if computer == "Rock":
                cs = midText.render("You lose! Rock smashes scissors.", True, white)
            if computer == "Paper":
                cs = midText.render("You win! Scissors cuts paper.", True, white)

            screen.blit(cs, [165, 260])

            mouse = pygame.mouse.get_pos()
            if 493 > mouse[0] > 343 and 461 > mouse[1] > 411:
                pygame.draw.rect(screen, bright_green, (343, 411, 150, 50))
            else:
                pygame.draw.rect(screen, green, (343, 411, 150, 50))

            if 494 > mouse[0] > 343 and 461 > mouse[1] > 411:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    from rockpaperscissors.py import rockPaperScissors

            pygame.display.update()

            clock.tick(60)

