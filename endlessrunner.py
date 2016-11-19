from player import *
from Obstacle import *
import pygame

screenSize = (800, 800)
bgcolor = (36,36,72)
black = (0, 0, 0)
obstaclecolor = (18,108,18)
playercolor = (108, 18, 18)
green = (0, 255, 0)
blue = (0,0,255)
selected = (255, 0, 0)


# this block here involves the basic initialisation of pygame
pygame.init() # module inititiation
clock = pygame.time.Clock() # defining a clock for controlling frame rate
game_display = pygame.display.set_mode(screenSize) #creating a display box


# variables for controlling the loop
gameExit = False
gameQuit = False

# objexts that are in play
playerbody = PlayerCube(screenSize[0] * 0.1, screenSize[1] * 0.1, 3, screenSize[0]*0.5, screenSize[1]*0.8)
obstacleHandler = ObstacleList(10, screenSize[1], 0, 3, screenSize[0])
obstacleHandler.populate() # call for the initial cubes so that they don't all appear at once

while not gameExit: # outer loop for quitting
    while not gameQuit: #inner  loop for restarting the game

        # for loop handling all input events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    playerbody.changePosition(screenSize[0] * 0.01 * playerbody.speed)
                if event.key == pygame.K_a:
                    playerbody.changePosition(-screenSize[0] * 0.01 * playerbody.speed)

            if event.type == pygame.QUIT:
                gameExit = True
                gameQuit = True

        # functions seeting the new display
        game_display.fill(bgcolor)
        obstacleHandler.update()
        pygame.draw.rect(game_display, playercolor, [playerbody.xloc - playerbody.xsize * 0.5, playerbody.yloc - playerbody.ysize * 0.5 , playerbody.xsize, playerbody.ysize])
        for obstacle in obstacleHandler.obstacles:
            pygame.draw.rect(game_display, obstaclecolor, [obstacle.xloc - obstacle.xsize * 0.5, obstacle.yloc - obstacle.ysize * 0.5 , obstacle.xsize, obstacle.ysize])



        # updating the display and wating for frame rate
        pygame.display.flip()
        clock.tick(24)