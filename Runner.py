import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Game:
    def __init__(self):
        self.tickets = 0

    def startScreen(self, screen):
        
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

        #if 494 > mouse[0] > 343 and 461 > mouse[1] > 411:
        #    if event.type == pygame.MOUSEBUTTONDOWN:
        #        from instructions.py import instructionScreen

        pygame.display.update()


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
                
        win.startScreen(screen)
        clock.tick(60)
if __name__ == "__main__":
    main()
