#def __init__(self):
import random
import pygame
pygame.init()

#correct = False
#tickets = 0


def getRandNum():
    num = random.randrange(20)
    return(num)

def test_correct(): #and tickets
    currentNum = getRandNum()
    wins = 0
    tickets = 0
    while (wins < 3 and wins > -1):
        print("My number is " + str(currentNum))
        newNum = getRandNum()
        print("For debuging num is" + str(newNum))
        hOrL = input("Will my next number be higher or lower? (\"h\" or \"l\")")

        if (not(newNum == currentNum)):
            if (hOrL == "h" or hOrL == "H"):
                if(newNum >= currentNum):
                    print("Correct!")
                    wins += 1
                    currentNum = newNum
                else:
                    print("Game Over")
                    wins = -1
            elif (hOrL == "l" or hOrL == "L"):
                if(newNum <= currentNum):
                    print("Correct!")
                    wins += 1
                    currentNum = newNum
                else:
                    print("Game Over")
                    wins = -1
            else:
                print("Invalid response.")
    if(wins == 3):
        print("You win! You here is your ticket!")
        tickets += 1
        return(tickets)
    elif(wins == -1):
        print("You lose. Try again later!")
        return(tickets)


def main():
    print("Welcome to Higher or Lower!")
    print("I will tell you a number.")
    print("You will then need to guess if the next number is higher or lower.")
    print("If you guess correctly 3 times in a row, you win a ticket!")
    tickets = test_correct()
    print("You now have " + str(tickets) + " tickets.")
main()
