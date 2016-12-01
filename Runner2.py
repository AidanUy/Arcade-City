import pygame
import sys
from buttonclass import button
from spriteClass import gameSprite

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Game:
    def __init__(self):
        self.tickets = 0

    def startScreen(self, screen):
        pygame.display.init()
        titleText = pygame.font.SysFont('Showcard Gothic', 60)
        subText = pygame.font.SysFont('Showcard Gothic', 20)

        text = titleText.render("Arcade City", True, WHITE)
        cs = subText.render("CS110 Final Project", True, WHITE)
        names = subText.render("Aidan Uy, Crystal Low, Danika Gaviola, Dylan Pan", True, WHITE)

        screen.blit(text, [220, 200])
        screen.blit(cs, [310, 265])
        screen.blit(names, [150, 290])
        #self.delete = 
        #mouse = pygame.mouse.get_pos()

     
        
        pygame.display.update()



    def instructionScreen(self, screen, sScreen):
        pygame.display.init()
        titleText = pygame.font.SysFont('Showcard Gothic', 60)
        text = titleText.render("INSTRUCTIONS!", True, WHITE)
        screen.blit(text, [200,400])
        
        pygame.display.update()

def main():
    pygame.init()
    size = [800, 600]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Arcade City")


    done = False
    clock = pygame.time.Clock()



    sScreen = Game()
    s_screen_method = sScreen.startScreen(screen)
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
                done = True
        
            startButton = button(screen, GREEN, RED, 300, 400, 200, 100)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos1 = startButton.mouse 
                if startButton.rect.collidepoint(pos1):
                   sScreen.instructionScreen(screen,sScreen)
                     
        		  
        pygame.display.update()
    clock.tick(60)		     
        
if __name__ == "__main__":
    main()
