import pygame
pygame.init()

class instructionScreen:

    def __init__(self):
        size = [800, 600]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Arcade City")

        black = (0, 0, 0)
        white = (255, 255, 255)
        orange = (250, 105, 0)
        green = (0, 200, 0)

        bright_orange = (255, 130, 0)
        bright_green = (0, 255, 0)

        # Loop until the user clicks the close button
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        # Set black background
        screen.fill(black)

        # Imports background music and loops it indefinitely
        ######### Hmm, how to do this without music restarting??????

        # -------- Main Program Loop -----------
        while not done:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    pygame.quit()
                    done = True # Flag that we are done so we exit this loop

            titleText = pygame.font.SysFont('Showcard Gothic', 60)

            text = titleText.render("Instructions", True, white)

            screen.blit(text, [200, 80])

            mouse = pygame.mouse.get_pos()

            if 485 > mouse[0] > 335 and 550 > mouse[1] > 500:
                pygame.draw.rect(screen, bright_green, (335, 500, 150, 50))
            else:
                pygame.draw.rect(screen, green, (335, 500, 150, 50))

            buttonText = pygame.font.SysFont('Showcard Gothic', 30)

            play = buttonText.render("Play!", True, white)
            screen.blit(play, [367, 515])

            if 485 > mouse[0] > 335 and 550 > mouse[1] > 500:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    from gamescreen.py import gamescreen

            pygame.display.update()

def main():
    instructionScreen()

main()
