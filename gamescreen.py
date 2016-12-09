import pygame, os, sys
from buttonclass import button
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
bright_red = (255, 0, 0)

green = (0, 200, 0)
bright_green = (0, 255, 0)

blue = (0, 0, 200)
bright_blue = (0, 0, 255)

class gameScreen:

    def __init__(self):
        size = [800, 600]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Arcade City")

        clock = pygame.time.Clock()

        background = pygame.image.load("bggamescreen.png").convert()
        screen.blit(background, [0, 0])

        building1img = pygame.image.load("buildingrps.png").convert()
        building1 = pygame.transform.scale(building1img, (120, 260))

        building2img = pygame.image.load("buildinghl.png").convert()
        building2 = pygame.transform.scale(building2img, (130, 300))

        building3img = pygame.image.load("buildingpaint.png").convert()
        building3 = pygame.transform.scale(building3img, (110, 225))

        screen.blit(building1, [90, 196])
        screen.blit(building2, [250, 156])
        screen.blit(building3, [420, 230])

        ticketFile = open("tickets.txt", "r")
        tickets = ticketFile.read()

        titleText = pygame.font.SysFont('Showcard Gothic', 30)
        subText = pygame.font.SysFont('Showcard Gothic', 15)

        ticks = titleText.render(tickets, True, white)
        ticklabel = titleText.render("Tickets", True, white)

        pygame.draw.line(screen, red, [660, 0], [660, 93], 7)
        pygame.draw.line(screen, red, [660, 90], [800, 90], 7)

        screen.blit(ticks, [707, 50])
        screen.blit(ticklabel, [670, 10])

        if int(tickets) == 0:
            captionImg = pygame.image.load("caption.png").convert()
            caption = pygame.transform.scale(captionImg, (500, 70))
            instructgirlimg = pygame.image.load("instructgirl.png").convert()
            instructgirl = pygame.transform.scale(instructgirlimg, (80, 80))
            instructgirl.set_colorkey(black)

            screen.blit(instructgirl, [-10, -10])
            screen.blit(caption, [0, 65])
            pygame.draw.rect(screen, white, (25, 75, 430, 50))

            captionText = subText.render("Start playing!  Remember, to unlock Higher or Lower,", True, black)
            captionText2 = subText.render("you need 300 tickets!", True, black)
            screen.blit(captionText, [25, 75])
            screen.blit(captionText2, [25, 90])

        elif 0 < int(tickets) < 200:
            captionImg = pygame.image.load("caption.png").convert()
            caption = pygame.transform.scale(captionImg, (500, 70))
            instructgirlimg = pygame.image.load("instructgirl.png").convert()
            instructgirl = pygame.transform.scale(instructgirlimg, (80, 80))
            instructgirl.set_colorkey(black)

            screen.blit(instructgirl, [-10, -10])
            screen.blit(caption, [0, 65])
            pygame.draw.rect(screen, white, (25, 75, 430, 50))

            remainingTicks = str(300 - int(tickets))

            captionText = subText.render(("Keep playing!  You still need " + remainingTicks + " more tickets to"), True, black)
            captionText2 = subText.render("unlock Higher or Lower.", True, black)
            screen.blit(captionText, [25, 75])
            screen.blit(captionText2, [25, 90])

        elif 200 <= int(tickets) < 300:
            captionImg = pygame.image.load("caption.png").convert()
            caption = pygame.transform.scale(captionImg, (500, 70))
            instructgirlimg = pygame.image.load("instructgirl.png").convert()
            instructgirl = pygame.transform.scale(instructgirlimg, (80, 80))
            instructgirl.set_colorkey(black)

            screen.blit(instructgirl, [-10, -10])
            screen.blit(caption, [0, 65])
            pygame.draw.rect(screen, white, (25, 75, 430, 50))

            remainingTicks = str(300 - int(tickets))

            captionText = subText.render(("You're almost there!  You're just " + remainingTicks + " tickets away"), True, black)
            captionText2 = subText.render("from unlocking Higher or Lower!", True, black)
            screen.blit(captionText, [25, 75])
            screen.blit(captionText2, [25, 90])

        elif int(tickets) >= 300:
            captionImg = pygame.image.load("caption.png").convert()
            caption = pygame.transform.scale(captionImg, (500, 70))
            instructgirlimg = pygame.image.load("instructgirl.png").convert()
            instructgirl = pygame.transform.scale(instructgirlimg, (80, 80))
            instructgirl.set_colorkey(black)

            screen.blit(instructgirl, [-10, -10])
            screen.blit(caption, [0, 65])
            pygame.draw.rect(screen, white, (25, 75, 430, 50))

            remainingTicks = str(int(tickets) - 300)

            captionText = subText.render("Nice job!  Be careful though, if you lose more than", True, black)
            captionText2 = subText.render((remainingTicks + " tickets, you'll have to get back to 300 tickets to"), True, black)
            captionText3 = subText.render("play Higher or Lower again!", True, black)
            screen.blit(captionText, [25, 75])
            screen.blit(captionText2, [25, 90])
            screen.blit(captionText3, [25, 105])

        ticketFile.close()

        pygame.display.update()

        clock.tick(60)
