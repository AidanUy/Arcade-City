import pygame, os, sys
from buttonclass import button
from startscreen import startScreen
from instructions import instructionScreen
pygame.init()

def main():
    
    #instruction = instructionScreen()
    startScreen()
    done = False
    while not done:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               done = True
           
            if event.type == pygame.MOUSEBUTTONDOWN: 
               startScreen()
               mouse1 = pygame.mouse.get_pos()
               #print(mouse1)
               if 500 > mouse1[0] > 350 and 450 > mouse1[1] > 400:
                   print("this button works")
                   instructionScreen()
                  # pygame.display.update() 
           
                   
               if 475 > mouse1[0] > 325 and 550 > mouse1[1] > 500: 
                  print(mouse1)
                  print("aaa")
                  
        pygame.display.update()
main()
