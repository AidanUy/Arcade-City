import pygame
pygame.init()

class rockPaperScissorsPaper:
    
    def __init__(self):
        size = [800, 600]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Arcade City")

        black = (0, 0, 0)
        white = (255, 255, 255)
        red = (255, 0, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)

        orange = (250, 105, 0)
        bright_orange = (255, 130, 0)
        green = (0, 200, 0)
        bright_green = (0, 255, 0)

        from random import randint

        #create a list of play options
        t = ["Rock", "Paper", "Scissors"]

        #assign a random play to the computer
        computer = t[randint(0,2)]


        # Loop until the user clicks the close button
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        # Set black background
        screen.fill(black)

        # -------- Main Program Loop -----------
        while not done:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    pygame.quit()
                    done = True # Flag that we are done so we exit this loop

 

                    
            subText = pygame.font.SysFont('Showcard Gothic', 50)
            smallText = pygame.font.SysFont('Showcard Gothic', 20)
            midText = pygame.font.SysFont('Showcard Gothic', 30)

            player = "Paper"
            if computer == "Paper":
                cs = midText.render("Tie!", True, white)
            if computer == "Scissors":
                cs = midText.render("You lose! Scissors cuts paper.", True, white)
            if computer == "Rock":
                cs = midText.render("You win! Paper covers rock.", True, white)

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

def main():
    rockPaperScissorsPaper()
main()
