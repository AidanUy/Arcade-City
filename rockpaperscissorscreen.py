import pygame
pygame.init()




class rockPaperScissorScreen:


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




        # Imports background image and sets as background
        screen.fill(black)




        # Imports background music and loops it indefinitely






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
 
            names = subText.render("Rock, Paper or Scissors?", True, white)
            screen.blit(names, [100, 290])


            mouse = pygame.mouse.get_pos()


            

            paper = smallText.render("Paper", True, white)
            scissor = smallText.render("Scissors", True, white)

            
            if 300 > mouse[0] > 150 and 500 > mouse[1] > 450:
                pygame.draw.rect(screen, bright_green, (150,450,150,50))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen.fill(black)
                    player = "Rock"
                    if player == computer:
                        cs = midText.render("Tie!", True, white)
                    if computer == "Paper":
                        cs = midText.render("You lose! Paper covers rock.", True, white)
                    else:
                        cs = midText.render("You win! Rock smashes scissors.", True, white)
                    screen.blit(cs, [175, 265])
            else:
                pygame.draw.rect(screen, green, (150,450,150,50))

            if 500 > mouse[0] > 350 and 500 > mouse[1] > 450:
                pygame.draw.rect(screen, bright_green, (350,450,150,50))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen.fill(black)
                    player = "Paper"
                    if player == computer:
                        cs = midText.render("Tie!", True, white)
                    if computer == "Scissors":
                        cs = midText.render("You lose! Scissors cuts paper.", True, white)
                    else:
                        cs = midText.render("You win! Paper covers rock.", True, white)
                    screen.blit(cs, [175, 265])
            else:
                pygame.draw.rect(screen, green, (350,450,150,50))

            if 700 > mouse[0] > 550 and 500 > mouse[1] > 450:
                pygame.draw.rect(screen, bright_green, (550,450,150,50))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen.fill(black)
                    player = "Scissors"
                    if player == computer:
                        cs = midText.render("Tie!", True, white)
                    if computer == "Rock":
                        cs = midText.render("You lose! Rock smashes scissors.", True, white)
                    else:
                        cs = midText.render("You win! Scissors cuts paper", True, white)
                    screen.blit(cs, [175, 265])
            else:
                pygame.draw.rect(screen, green, (550,450,150,50))

            rock = smallText.render("Rock", True, white)
            screen.blit(rock, [200, 465])

            paper = smallText.render("Paper", True, white)
            screen.blit(paper, [400, 465])
            
            scissors = smallText.render("Scissors", True, white)
            screen.blit(scissors, [575, 465])

            #if 300 > mouse[0] > 150 and 500 > mouse[1] > 450:
            #    if event.type == pygame.MOUSEBUTTONDOWN:
            #       screen.fill(black)
            #        player = "Rock"
            #        if player == computer:
            #            cs = subText.render("Tie!", True, white)
            #        if computer == "Paper":
            #            cs = subText.render("You lose! Paper covers rock.", True, white)
            #        else:
            #            cs = subText.render("You win! Rock smashes scissors.", True, white)
                    
            #if 500 > mouse[0] > 350 and 500 > mouse[1] > 450:
            #    if event.type == pygame.MOUSEBUTTONDOWN:
            #        screen.fill(black)
            #        player = "Paper"
            #        if player == computer:
            #            cs = subText.render("Tie!", True, white)
            #        if computer == "Scissors":
            #            cs = subText.render("You lose! Scissors cuts paper.", True, white)
            #        else:
            #            cs = subText.render("You win! Paper covers rock.", True, white)

            #if 700 > mouse[0] > 550 and 500 > mouse[1] > 450:
            #    if event.type == pygame.MOUSEBUTTONDOWN:
            #        screen.fill(black)
            #        player = "Scissors"
            #        if player == computer:
            #            cs = subText.render("Tie!", True, white)
            #        if computer == "Rock":
            #            cs = subText.render("You lose! Rock smashes scissors.", True, white)
            #        else:
            #            cs = subText.render("You win! Scissors cuts paper", True, white)


            




            pygame.display.update()




def main():
    c = rockPaperScissorScreen()




main()
















