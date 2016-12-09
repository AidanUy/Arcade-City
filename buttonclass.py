import pygame, os, sys

class button():

	def __init__(self, screen, color, x, y, width, height):
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.color = color

		self.rect = pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
