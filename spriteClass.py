import pygame, os, sys
pygame.init()

class gameSprite(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("testsprite.png").convert()
        self.rect = self.image.get_rect()
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
        if self.x < -20:
            self.x = -20
        elif self.x > 725:
            self.x = 725
        if self.y < 0:
            self.y = 0
        elif self.y > 510:
            self.y = 510
        print(self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.rect.move_ip(self.x, self.y)
