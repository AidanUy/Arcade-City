import pygame
import sys

class Screen():
	def __init__(self):
		size = [800, 600]

		#pick from one of these WORKS
		screen = pygame.display.set_mode(size)
		pygame.display.set_caption("Arcade City")

		self.background1 = pygame.image.load("imagetest.jpg").convert()
		self.background2 = pygame.image.load("imagetest2.jpg").convert()

		#background = pygame.image.load(self.imagereference).convert()
		#referring to self.imageref inside background does not work because self.imagereference is currently blank
		
		if self.background1:
			screen.blit(self.background1,[0,0])
		else:
			screen.blit(self.background2, [0,0])
		
		clock = pygame.time.Clock()
		clock.tick(60)
		
		pygame.display.flip()

		done = False
		#while loop-----
		while not done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					done = True
		
		

#this is the bare bones of the screen class. i'm not done at all. the whole idea is that it is more general so that each screen (introduction, start, game, shop) use the same class, and we are not "hardcoding" as much as we currently are. see concerns listed in group chat- Crystal 

#http://www.balloonbuilding.com/index.php?chapter=introduction_to_classes&lang=en#section_12
#that's one of the internet sources that I found useful which explained classes. Usually they should be more general so that more instances of that class can be used -- aka code is more efficient
		
		

		

