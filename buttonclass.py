import pygame, os, sys
pygame.init()

class button():

	def __init__(self, screen, color, bright_color, x, y, width, height):
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.color = color
		self.bright_color = bright_color

		mouse = pygame.mouse.get_pos()

		if (self.x + self.width) > mouse[0] > self.x and (self.y + self.height) > mouse[1] > self.y:
			self.rect = pygame.draw.rect(screen, self.bright_color, (self.x, self.y, self.width, self.height))
		else:
			self.rect = pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
