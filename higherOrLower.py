import pygame
import random
pygame.init()


class higherOrLower:

    size = [800, 600]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Arcade City")


    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)


  # Loop until the user clicks the close button.
    done = False

  # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

  # -------- Main Program Loop -----------
    while not done:
      # --- Main event loop
        for event in pygame.event.get(): # User did something
              if event.type == pygame.QUIT: # If user clicked close
                pygame.quit()
                done = True # Flag that we are done so we exit this loop


    def __init__(self):
        self.wins = 0
        self.correct = False


    def getRandNum(self):
        self.num = Random.randrange(20)
        return(self.num)

    def test_correct(self): #and tickets
        self.currentNum = getRandNum()
        while (self.wins < 3 and self.wins > -1):
            print("My number is " + self.currentNum)
            hOrL = input("Will my next number be higher or lower? (\"h\" or \"l\")")
            self.newNum = getRandNum()
            if (!(self.newNum == self.currentNum)):
                if (hOrL == "h" or hOrL == "H"):
                    if(self.newNum >= self.currentNum):
                        print("Correct!")
                        self.wins += 1
                        self.currentNum = self.newNum
                    else:
                        print("Game Over")
                        self.wins = -1
                elif (hOrL == "l" or hOrL == "L"):
                    if(self.newNum <= self.currentNum):
                        print("Correct!")
                        self.wins += 1
                        self.currentNum = self.newNum
                    else:
                        print("Game Over")
                        self.wins = -1
                else:
                    print("Invalid response.")
        if(self.wins == 3):
            print("You win! You here is your ticket!")
            #tickets += 1
            #return(tickets)
        elseif(self.wins == -1):
            print("You lose. Try again later!")
            #return(tickets)


    def main(self):
        print("Welcome to Higher or Lower!")
        print("I will tell you a number.")
        print("You will then need to guess if the next number is higher or lower.")
        print("If you guess correctly 3 times in a row, you win a ticket!")
        test_correct(self)
    main()
