import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Game:
    def __init__(self):
        self.tickets = 0

    def startScreen(self, screen, win):
        titleText = pygame.font.SysFont('Showcard Gothic', 60)
        subText = pygame.font.SysFont('Showcard Gothic', 20)

        text = titleText.render("Arcade City", True, WHITE)
        cs = subText.render("CS110 Final Project", True, WHITE)
        names = subText.render("Aidan Uy, Crystal Low, Danika Gaviola, Dylan Pan", True, WHITE)

        screen.blit(text, [220, 200])
        screen.blit(cs, [310, 265])
        screen.blit(names, [150, 290])

        mouse = pygame.mouse.get_pos()

        if 493 > mouse[0] > 343 and 461 > mouse[1] > 411:
            pygame.draw.rect(screen, RED, (343, 411, 150, 50))
        else:
            pygame.draw.rect(screen, GREEN, (343, 411, 150, 50))

        buttonText = pygame.font.SysFont('Showcard Gothic', 30)

        start = buttonText.render("Start!", True, WHITE)
        screen.blit(start, [365, 425])

        for event in pygame.event.get():
             if 494 > mouse[0] > 343 and 461 > mouse[1] > 411:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    win.instructionScreen(screen, win)
                    pygame.display.update()
                    return
                    
        pygame.display.update()

    def instructionScreen(self, screen, win):
        
        background = pygame.image.load("background.png").convert()
        screen.blit(background, [0, 0])
        caption = pygame.image.load("caption.png").convert()
        oak = pygame.image.load("oak.png").convert()
        oak.set_colorkey(BLACK)
        screen.blit(oak, [570, 130])
        titleText = pygame.font.SysFont('Showcard Gothic', 60)
        subText = pygame.font.SysFont('Showcard Gothic', 25)

        text = titleText.render("Instructions", True, WHITE)
        captionText = subText.render("Hey! Welcome to Arcade City! Start by walking up", True, BLACK)
        captionText2 = subText.render("to and playing Higher or Lower and racking up", True, BLACK)
        captionText3 = subText.render("tickets. Then, when you get enough tickets,", True, BLACK)
        captionText4 = subText.render("different games will be unlocked. Have fun!", True, BLACK)

        screen.blit(text, [200, 80])

        mouse = pygame.mouse.get_pos()

        if 480 > mouse[0] > 325 and 550 > mouse[1] > 500:
            pygame.draw.rect(screen, RED, (325, 500, 150, 50))
        else:
            pygame.draw.rect(screen, GREEN, (325, 500, 150, 50))

        buttonText = pygame.font.SysFont('Showcard Gothic', 30)

        screen.blit(caption, [3, 300])
        pygame.draw.rect(screen, WHITE, (45, 320, 670, 110))

        screen.blit(captionText, [45, 325])
        screen.blit(captionText2, [45, 350])
        screen.blit(captionText3, [45, 375])
        screen.blit(captionText4, [45, 400])

        play = buttonText.render("Play!", True, WHITE)
        screen.blit(play, [357, 515])

        #if 480 > mouse[0] > 325 and 550 > mouse[1] > 500:
        #    if event.type == pygame.MOUSEBUTTONDOWN:
        #        from gamescreen.py import gamescreen

        pygame.display.update()
        
    def clearScreen(self, screen):
        screen.fill(WHITE)
        
def main():
    pygame.init()
    size = [800, 600]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Arcade City")
    done = False
    clock = pygame.time.Clock()
    win = Game()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True
                
        win.startScreen(screen, win)
        clock.tick(60)
if __name__ == "__main__":
    main()
