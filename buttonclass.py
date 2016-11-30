import pygame
import os
import sys

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
class Button:
	def __init__(self, screen, color, x, y, width, height):
		pygame.display.init()
	
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.color = color
	
		#pygame.draw.rect(screen,color, ((x pos, y pos), (width, height)), thickness)
		
		self.rect = pygame.draw.rect(screen, self.color, ((self.x,self.y), (self.width, self.height)), 0)

		

		



#screen = pygame.display.set_mode([800,600])
#pygame.display.set_caption("Arcade City")
	
		
		#background = pygame.image.load("imagetest.jpg").convert()
		#screen.blit(background,[0,0]) 




screen = pygame.display.set_mode([800,600])
myButton = Button(screen, GREEN, 200, 300, 50, 70)

print(myButton.rect, "this gives the dimensions and location of the rectangle button")

clock = pygame.time.Clock()
clock.tick(60)
pygame.display.flip()


done = False
#while loop

#the collision needs to be a conditional in the while loop. 

#THE BUTTON CLASS ALLOWS YOU TO DO THIS FOR EVERY BUTTON.
while not done:
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			pos = pygame.mouse.get_pos()
			if myButton.rect.collidepoint(pos):
				print("no")
		if event.type == pygame.QUIT:
			pygame.quit()
			done = True
