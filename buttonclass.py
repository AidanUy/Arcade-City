import pygame, os, sys

class button():

	def __init__(self, screen, color, bright_color, x, y, width, height):
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.color = color
		self.bright_color = bright_color
             
		self.mouse = pygame.mouse.get_pos()

		if (self.x + self.width) > self.mouse[0] > self.x and (self.y + self.height) > self.mouse[1] > self.y:
			self.rect = pygame.draw.rect(screen, self.bright_color, (self.x, self.y, self.width, self.height))
		else:
			self.rect = pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
			
		#if self.width + self.x > self.mouse > self.x and self.height + self.y > self. mouse > self.y:
			#if event.type == pygame.MOUSEBUTTONDOWN:
				#from instructions import <--- WE WOULD NEED TO ADD A WHILE NOT DONE ON TOP IN ORDER
				#TO MAKE IT SO THAT IT WORKS, but we would need to also find a way to make the FILE that we import
				#code from and the CLASS that we are importing as general as possible so that we could replace
				#them with each instance
