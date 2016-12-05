from player import *

from Obstacle import *
from gamedisplay import *
from numpy import *
import pygame
import time
from random import randint;

screenSize = (800, 800)
playersize_x = screenSize[0] * 0.08
playersize_y = screenSize[1] * 0.08
player_speed = 3


# this block here involves the basic initialisation of pygame
pygame.init() # module inititiation
clock = pygame.time.Clock() # defining a clock for controlling frame rate
game_display = pygame.display.set_mode(screenSize) #creating a display box
pygame.display.set_caption('Endlessrunner of Doom')

# variables for controlling the loop
gameExit = False

gameLevel = 0
death_pause = 1


# objexts that are in play
playerbody = PlayerCube(playersize_x, playersize_y, player_speed, screenSize[0]*0.5, screenSize[1]*0.8, screenSize)
obstacleHandler = ObstacleList(10,screenSize, 10, screenSize[1]/8 ,screenSize[0]/40 )

# cubex/8 and cubey/40 always result in obstacles that have a grid with 20 lanes in y and 40 lanes in x if resolution is div by 2

def text_objects(text, TextConf):
    TextSurface = pygame.font.Font.render(TextConf, text, True, black)
    return TextSurface, TextSurface.get_rect()

def message_display(text, size , xpos, ypos, pause):
    TextConf = pygame.font.Font('freesansbold.ttf', size)
    TextSurface, TextRectangle = text_objects(text, TextConf)
    TextRectangle.center = (xpos, ypos)
    game_display.blit(TextSurface, TextRectangle) #display it
    pygame.display.flip()
    time.sleep(pause)
    TextRectCoord = (TextRectangle[0], TextRectangle[0]+TextRectangle[2], TextRectangle[1], TextRectangle[1]+TextRectangle[3])
    return(TextRectCoord)

def player_death():
    message_display('You died horribly', 90, screenSize[0]/2, screenSize[1]/2, 1)

def Welcome():
    return message_display('Endlessrunner of Doom', 50, screenSize[0]/2, screenSize[1]/2 - 200, 0.5)

def Start():
    return message_display('Start Game', 30, screenSize[0]/2, screenSize[1]/2, 0)


def Exit():
    return message_display('Exit Game', 30, screenSize[0]/2, screenSize[1]/2 + 50, 0)

def performance_counter(time):
    message_display('You survived '+ str(time) + ' Seconds', 15, 200, 20, 0)

def Startscreen():

    intro = True
    game_display.fill((255,255,255))
    pygame.display.update()

    Welcome()

    StartBox = Start()

    ExitBox = Exit()

    pygame.display.update()
    clock.tick(15)
    while intro:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():

            if mouse[0] > StartBox[0] and mouse[0] < StartBox[1] and mouse[1] > StartBox[2] and mouse[1] < StartBox[3] and click[0] == 1:
                intro = False

            if mouse[0] > ExitBox[0] and mouse[0] < ExitBox[1] and mouse[1] > ExitBox[2] and mouse[1] < ExitBox[3] and click[0] == 1:
                quit()

            if event.type == pygame.QUIT:
                quit()



def levelLoop():
    levelQuit = False
    movement = 0 #gets only initialized here. is used in level loop

    while not levelQuit: #inner  loop for the levels
        performance_counter(time.process_time()) #TODO FIX gets redrawn after each collition detectCollision all the time

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
                Startscreen()

        #checking collisions before updating screen
        collision = playerbody.detectCollision(obstacleHandler.obstacles)
        if collision:
            movement = 0
            obstacleHandler.restart()

            player_death()

        obstacleHandler.update()
        playerbody.changePosition(movement)

        # graphics call
        updateScreen(game_display, playerbody, obstacleHandler.obstacles)

        # updating the display and wating for frame rate
        pygame.display.flip()
        clock.tick(40)


while not gameExit: # outer loop for quitting


    obstacleHandler.restart()
    Startscreen()
    levelLoop()

    quit()
