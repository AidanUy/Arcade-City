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

    

        clock = pygame.time.Clock()

        background = pygame.image.load("background.png").convert()
        screen.blit(background, [0, 0])

        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play(loops = -1)
        pygame.mixer.music.set_volume(0.5)
        done = False
        while not done:
            for event in pygame.event.get():
             #   if event.type == pygame.QUIT:
             #      pygame.quit()
                
                   
              #      done = True

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
                    instructionScreen()

            pygame.display.update()

            clock.tick(60)


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
               

                titleText = pygame.font.SysFont('Showcard Gothic', 60)
                subText = pygame.font.SysFont('Showcard Gothic', 25)

                text = titleText.render("Instructions", True, white)
                captionText = subText.render("Hey! Welcome to Arcade City! Start by walking up", True, black)
                captionText2 = subText.render("to and playing Higher or Lower and racking up", True, black)
                captionText3 = subText.render("tickets. Then, when you get enough tickets,", True, black)
                captionText4 = subText.render("different games will be unlocked. Have fun!", True, black)

                screen.blit(text, [200, 80])

                mouse = pygame.mouse.get_pos()

            if 480 > mouse[0] > 325 and 550 > mouse[1] > 500:
                pygame.draw.rect(screen, bright_green, (325, 500, 150, 50))
            else:
                pygame.draw.rect(screen, green, (325, 500, 150, 50))

            buttonText = pygame.font.SysFont('Showcard Gothic', 30)

            screen.blit(caption, [3, 300])
            pygame.draw.rect(screen, white, (45, 320, 670, 110))

            screen.blit(captionText, [45, 325])
            screen.blit(captionText2, [45, 350])
            screen.blit(captionText3, [45, 375])
            screen.blit(captionText4, [45, 400])

            play = buttonText.render("Play!", True, white)
            screen.blit(play, [357, 515])

            if 480 > mouse[0] > 325 and 550 > mouse[1] > 500:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    from gamescreen.py import gamescreen

            pygame.display.update()

            clock.tick(60)


def main():
    startScreen()
    done = False
    while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  
                   pygame.quit()
                   sys.exit()
                   pygame.display.quit()   
                
                   
                   done = True

main()
