import pygame
pygame.init()

class rockPaperScissors:

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

            from random import randint

            #create a list of play options
            t = ["Rock", "Paper", "Scissors"]

            #assign a random play to the computer
            computer = t[randint(0,2)]

            names = subText.render("Rock, Paper, or Scissors?", True, white)
            screen.blit(names, [80, 100])

            mouse = pygame.mouse.get_pos()
            (leftclick, rightclick, midclick) = pygame.mouse.get_pressed()

            if 280 > mouse[0] > 130 and 500 > mouse[1] > 450:
                pygame.draw.rect(screen, bright_green, (130,450,150,50))
                if leftclick == 1:
                    pygame.draw.rect(screen, black, (0, 260, 800, 40))
                    player = "Rock"
                    if player == computer:
                        cs = midText.render("Tie!", True, white)
                        pygame.draw.rect(screen, white, (130, 450, 150, 50))#Not yet functional
                    if computer == "Paper":
                        cs = midText.render("You lose! Paper covers rock.", True, white)
                        pygame.draw.rect(screen, red, (130, 450, 150, 50))#Not yet functional
                    else:
                        cs = midText.render("You win! Rock smashes scissors.", True, white)
                    screen.blit(cs, [165, 260])

            else:
                pygame.draw.rect(screen, green, (130, 450, 150, 50))

            if 480 > mouse[0] > 330 and 500 > mouse[1] > 450:
                pygame.draw.rect(screen, bright_green, (330, 450, 150, 50))
                if leftclick == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(screen, black, (0, 260, 800, 40))
                        player = "Paper"
                        if player == computer:
                            cs = midText.render("Tie!", True, white)
                            pygame.draw.rect(screen, white, (330, 450, 150, 50))#Not yet functional
                        if computer == "Scissors":
                            cs = midText.render("You lose! Scissors cuts paper.", True, white)
                            pygame.draw.rect(screen, red, (330, 450, 150, 50))#Not yet functional
                        else:
                            cs = midText.render("You win! Paper covers rock.", True, white)
                        screen.blit(cs, [165, 260])
            else:
                pygame.draw.rect(screen, green, (330, 450, 150, 50))

            if 680 > mouse[0] > 530 and 500 > mouse[1] > 450:
                pygame.draw.rect(screen, bright_green, (530, 450, 150, 50))
                if leftclick == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(screen, black, (0, 260, 800, 40))
                        player = "Scissors"
                        if player == computer:
                            cs = midText.render("Tie!", True, white)
                        if computer == "Rock":
                            cs = midText.render("You lose! Rock smashes scissors.", True, white)
                            pygame.draw.rect(screen, white, (530, 450, 150, 50))#Not yet functional
                        else:
                            cs = midText.render("You win! Scissors cuts paper.", True, white)
                            pygame.draw.rect(screen, red, (530, 450, 150, 50))#Not yet functional
                        screen.blit(cs, [165, 260])
            else:
                pygame.draw.rect(screen, green, (530, 450, 150, 50))

            rock = smallText.render("Rock", True, white)
            screen.blit(rock, [180, 465])

            paper = smallText.render("Paper", True, white)
            screen.blit(paper, [373, 465])

            scissors = smallText.render("Scissors", True, white)
            screen.blit(scissors, [563, 465])

            pygame.display.update()

def main():
    rockPaperScissors()
main()
