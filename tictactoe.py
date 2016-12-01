import pygame, os, sys
pygame.init()

class TicTacToeGame:
	def __init__(self):
		self.winning_combos(
		[6,7,8], [3,4,5], [0,1,2], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]
		self.corners = [0,2,6,8]
		self.sides = [1,3,5,7]
		self.middle = 4
