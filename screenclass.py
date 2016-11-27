import pygame, sys

class Screen:
	def __init__(self):
		size = [800, 600]
		self.screen = pygame.display.set_mode(size)
		pygame.display.set_caption("Arcade City")

		self.imagereference = ""
		background = pygame.image.load(self.imagereference).convert()
		#i don't know if you can refer to self.imagereference like that, but this is the logic behind it. also why couldn't you?
		screen.blit(background, [0,0])
		
		done = False
		clock = pygame.time.Clock()


#this is the bare bones of the screen class. i'm not done at all. the whole idea is that it is more general so that each screen (introduction, start, game, shop) use the same class, and we are not "hardcoding" as much as we currently are. see concerns listed in group chat- Crystal 

#http://www.balloonbuilding.com/index.php?chapter=introduction_to_classes&lang=en#section_12
#that's one of the internet sources that I found useful which explained classes. Usually they should be more general so that more instances of that class can be used -- aka code is more efficient
		

		

