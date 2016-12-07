import pygame, os, sys
from buttonclass import button
from startscreen import startScreen
from instructions import instructionScreen
from testingscreen import testScreen
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
bright_red = (255, 0, 0)

green = (0, 200, 0)
bright_green = (0, 255, 0)

blue = (0, 0, 200)
bright_blue = (0, 0, 255)

def instruction():
    instruction = instructionScreen()
def main():
    screen = pygame.display.set_mode([800,600])
    
    start = startScreen()
    #startButton = button(green, bright_green, 350, 400, 150, 50)
    #display_startscreen = True
    #startscreen = 1
   
    mouse1 = pygame.mouse.get_pos()


    #instruction = instructionScreen()
    start = startScreen()
    var = True
    done = False
    while not done:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               done = True
           
            if event.type == pygame.MOUSEBUTTONDOWN:
               mouse1 = pygame.mouse.get_pos() 
              
               #start.startButton      
               if 500 > mouse1[0] > 350 and 450 > mouse1[1] > 400 and var:
                   print("this start button works")                                                
                   var = False 
                   instructionScreen()
                   
               elif 475 > mouse1[0] > 325 and 550 > mouse1[1] > 500 and not var: 
                  #print(mouse1)
                  print("this instructions button also works")
                  var = False
                  testScreen()
                   
                  pygame.display.update()
            
        pygame.display.update()   
    pygame.display.update()

    
            
                
main()                            
                  

            
       
