import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")

pygame.display.update()

font = pygame.font.SysFont(None, 25)


def snake(block,snakelen):
    for XnY in snakelen:
      pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block,block])


def message(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width / 3, display_height / 2])


clock = pygame.time.Clock()


def gameLoop():
    gameExit = False
    gameOver = False
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_X_change = 0
    lead_Y_change = 0
    block = 10
    FPS = 10
    snakeList=[]
    snanelen=1

    randApplex=round(random.randrange(0,display_width)/10.0)*10.0
    randAppley=round(random.randrange(0,display_height)/10.)*10.0

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message("you loose ,press  'c' to play again or press 'q' to quit.", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_X_change = -block
                    lead_Y_change = 0

                if event.key == pygame.K_RIGHT:
                    lead_X_change = block
                    lead_Y_change = 0

                if event.key == pygame.K_UP:
                    lead_Y_change = -block
                    lead_X_change = 0
                if event.key == pygame.K_DOWN:
                    lead_Y_change = block
                    lead_X_change = 0

            # if event.type==pygame.KEYUP:
            #     if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
            #         lead_X_change=0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_X_change
        lead_y += lead_Y_change
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, block, block])
        pygame.draw.rect(gameDisplay, red, [randApplex,randAppley, block, block])
        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList)>snanelen:
            del(snakeList[0])

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver=True


        snake(block,snakeList)

        pygame.display.update()
        clock.tick(FPS)
        if lead_x==randApplex and lead_y==randAppley:
            print("chalo kuch to huaa")
            randApplex = round(random.randrange(0, display_width) / 10.0) * 10.0
            randAppley = round(random.randrange(0, display_height) / 10.) * 10.0
            snanelen+=1

    pygame.quit()
    quit()


gameLoop()
