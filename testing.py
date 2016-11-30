import pygame
pygame.init()

class gameSprite(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("testsprite.png").convert()
        self.x = 0
        self.y = 0

    def update(self):
        key = pygame.key.get_pressed()
        dist = 5
        if key[pygame.K_DOWN]:
            self.y += dist
        elif key[pygame.K_UP]:
            self.y -= dist
        if key[pygame.K_RIGHT]:
            self.x += dist
        elif key[pygame.K_LEFT]:
            self.x -= dist

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

def main():
    size = [800, 600]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Arcade City")

    clock = pygame.time.Clock()

    done = False

    white = (255, 255, 255)

    character = gameSprite()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True

        character.update()

        screen.fill(white)
        character.draw(screen)

        pygame.display.update()

        clock.tick(60)

main()
