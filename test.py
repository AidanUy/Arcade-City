import pygame
pygame.init()

class startScreen:


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

        # Load and set up graphics
        background = pygame.image.load("background.png").convert()
        player_image = pygame.image.load("wiz.png").convert()

        # Imports background music and loops it indefinitely
        # pygame.mixer.music.load("music.mp3")
        # pygame.mixer.music.play(loops = -1)

        # -------- Main Program Loop -----------
        while not done:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    pygame.quit()
                    done = True # Flag that we are done so we exit this loop

            screen.blit(background, [0, 0])

            titleText = pygame.font.SysFont('Showcard Gothic', 60)
            subText = pygame.font.SysFont('Showcard Gothic', 20)

            text = titleText.render("Arcade City", True, white)
            cs = subText.render("CS110 Final Project", True, white)
            names = subText.render("Aidan Uy, Crystal Low, Danika Gaviola, Dylan Pan", True, white)

            screen.blit(text, [220, 200])
            screen.blit(cs, [310, 265])
            screen.blit(names, [150, 290])

            mouse = pygame.mouse.get_pos()

            if 300 > mouse[0] > 150 and 500 > mouse[1] > 450:
                pygame.draw.rect(screen, bright_green, (150,450,150,50))
            else:
                pygame.draw.rect(screen, green, (150,450,150,50))

            if 675 > mouse[0] > 425 and 500 > mouse[1] > 450:
                pygame.draw.rect(screen, bright_orange, (425,450,250,50))
            else:
                pygame.draw.rect(screen, orange, (425,450,250,50))

            buttonText = pygame.font.SysFont('Showcard Gothic', 30)

            start = buttonText.render("Start!", True, white)
            screen.blit(start, [173, 465])

            instructions = buttonText.render("Instructions", True, white)
            screen.blit(instructions, [443, 465])

            player_position = pygame.mouse.get_pos()
            x = player_position[0]
            y = player_position[1]
            screen.blit(player_image, [x, y])

            if 300 > x > 150 and 500 > y > 450:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen.fill(white)

            if 675 > x > 425 and 500 > y > 450:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    from instructions.py import instructionScreen
                    

            pygame.display.update()

def main():
    c = startScreen()

main()
