import pygame, os, sys
pygame.init()

class rockPaperScissors:

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

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    done = True

            subText = pygame.font.SysFont('Showcard Gothic', 50)
            smallText = pygame.font.SysFont('Showcard Gothic', 20)
            midText = pygame.font.SysFont('Showcard Gothic', 30)



            names = subText.render("Rock, Paper, or Scissors?", True, white)
            screen.blit(names, [80, 100])

            mouse = pygame.mouse.get_pos()
            (leftclick, rightclick, midclick) = pygame.mouse.get_pressed()

            if 280 > mouse[0] > 130 and 500 > mouse[1] > 450:
                pygame.draw.rect(screen, bright_green, (130,450,150,50))
                if leftclick == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        from rockpaperscissors.py import rockPaperScissorsRock

            else:
                pygame.draw.rect(screen, green, (130, 450, 150, 50))

            if 480 > mouse[0] > 330 and 500 > mouse[1] > 450:
                pygame.draw.rect(screen, bright_green, (330, 450, 150, 50))
                if leftclick == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        from rockpaperscissorspaper.py import rockPaperScissorsPaper
            else:
                pygame.draw.rect(screen, green, (330, 450, 150, 50))

            if 680 > mouse[0] > 530 and 500 > mouse[1] > 450:
                pygame.draw.rect(screen, bright_green, (530, 450, 150, 50))
                if leftclick == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        from rockpaperscissorsscissors.py import rockPaperScissorsScissors
            else:
                pygame.draw.rect(screen, green, (530, 450, 150, 50))

            rock = smallText.render("Rock", True, white)
            screen.blit(rock, [180, 465])

            paper = smallText.render("Paper", True, white)
            screen.blit(paper, [373, 465])

            scissors = smallText.render("Scissors", True, white)
            screen.blit(scissors, [563, 465])

            pygame.display.update()

            clock.tick(60)

def main():
    rockPaperScissors()
main()
