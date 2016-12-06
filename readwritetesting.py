import pygame, os, sys
pygame.init()

def main():
    size = [800, 600]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Arcade City")

    black = (0, 0, 0)
    white = (255, 255, 255)

    red = (200, 0, 0)
    bright_red = (255, 0, 0)

    green = (0, 200, 0)
    bright_green = (0, 255, 0)

    blue = (0, 0, 200)
    bright_blue = (0, 0, 255)

    done = False

    clock = pygame.time.Clock()

    tick = 0

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True

        tick += 1

        ticket = open("tickets.txt", "w")
        ticket.write(str(tick))
        ticket.close()
        tickets = open("tickets.txt", "r")
        tickets = tickets.read()

        game1unlocked = open("game1state.txt", "r")
        game1Unlocked = game1unlocked.read()

        game2unlocked = open("game2state.txt", "r")
        game2Unlocked = game2unlocked.read()

        if int(tickets) >= 200:
            if game1Unlocked == "False":
                game1unlocked.close()
                game1read = open("game1state.txt", "w")
                game1read.write("True")
                game1read.close()

        if int(tickets) >= 300:
            if game2Unlocked == "False":
                game2unlocked.close()
                game2read = open("game2state.txt", "w")
                game2read.write("True")
                game2read.close()

        unlock1 = open("game1state.txt", "r")
        unlock1 = unlock1.read()

        unlock2 = open("game2state.txt", "r")
        unlock2 = unlock2.read()

        titleText = pygame.font.SysFont('Showcard Gothic', 30)
        unlockText = pygame.font.SysFont('Showcard Gothic', 40)

        ticks = titleText.render(tickets, True, white)
        ticklabel = titleText.render("Tickets", True, white)
        unlockedText1 = unlockText.render("You unlocked Game 1!", True, white)
        unlockedText2 = unlockText.render("You unlocked Game 2!", True, white)

        screen.fill(black)

        pygame.draw.line(screen, red, [660, 0], [660, 93], 7)
        pygame.draw.line(screen, red, [660, 90], [800, 90], 7)

        screen.blit(ticks, [710, 50])
        screen.blit(ticklabel, [670, 10])

        if unlock1 == "True":
            screen.blit(unlockedText1, [200, 300])

        if unlock2 == "True":
            screen.blit(unlockedText2, [200, 350])

        pygame.display.update()

        clock.tick(60)

main()
