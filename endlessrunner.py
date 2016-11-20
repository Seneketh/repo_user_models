from player import *
from Obstacle import *
from gamedisplay import *
import pygame

screenSize = (800, 800)


# this block here involves the basic initialisation of pygame
pygame.init() # module inititiation
clock = pygame.time.Clock() # defining a clock for controlling frame rate
game_display = pygame.display.set_mode(screenSize) #creating a display box


# variables for controlling the loop
gameExit = False
gameQuit = False

# objexts that are in play
playerbody = PlayerCube(screenSize[0] * 0.1, screenSize[1] * 0.1, 3, screenSize[0]*0.5, screenSize[1]*0.8, screenSize)
obstacleHandler = ObstacleList(10,screenSize, 10, 50, 70)

while not gameExit: # outer loop for quitting
    movement = 0
    obstacleHandler.restart()

    while not gameQuit: #inner  loop for restarting the game
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    movement = screenSize[0] * 0.01 * playerbody.speed
                if event.key == pygame.K_a:
                    movement = -screenSize[0] * 0.01 * playerbody.speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    movement = 0
                if event.key == pygame.K_a:
                    movement = 0


            if event.type == pygame.QUIT:
                gameExit = True
                gameQuit = True

        #checking collisions before updating screen
        collision = playerbody.detectCollision(obstacleHandler.obstacles)
        if collision:
            movement = 0
            obstacleHandler.restart()

        obstacleHandler.update()
        playerbody.changePosition(movement)

        # graphics call
        updateScreen(game_display, playerbody, obstacleHandler.obstacles)



        # updating the display and wating for frame rate
        pygame.display.flip()
        clock.tick(24)