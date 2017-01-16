#!/usr/bin/python

from numpy import *
from random import randint;
import pygame
import time
import csv # data handling

from player import *
from Obstacle import *
from gamedisplay import *
import Eyelinker
from Textwriter import *
from Gameloops import *
from Exptools import *

##GAME PARAMETERS##
screenSize = (1600, 1200)
#screenSize = (1366, 768)
#screenSize = (800, 600)

framerate = 30
playersize_x = screenSize[0] * 0.05
playersize_y = screenSize[0] * 0.05
player_speed = 2.5
obstacle_amount = 12
obstacle_speed = 15
##

##PYGAME INITIALIZATION##
pygame.init() # module inititiation
clock = pygame.time.Clock() # defining a clock for controlling frame rate
game_display = pygame.display.set_mode(screenSize, pygame.FULLSCREEN ) #creating a display box
#
pygame.display.init()
pygame.display.set_caption('Endlessrunner of Doom')
##

##OBJECTS INITIALIZATION##
eyeconnection = Eyelinker.Eyehandler(screenSize[0], screenSize[1])
#eyeconnection = 0 #just so I can work without actually importing eytracker stuff
playerbody = PlayerCube(playersize_x, playersize_y, player_speed, screenSize[0]*0.5, screenSize[1] - playersize_y , screenSize)
obstacleHandler = ObstacleList(obstacle_amount, screenSize, obstacle_speed, screenSize[1]/8.0 ,screenSize[0]/40.0 )
gameloops = Gameloops(framerate, screenSize, game_display, clock, playerbody, obstacleHandler, eyeconnection)

def main():

    eyeconnection.doSetup() # Perform Calibration
    eyeconnection.endSetup() # Start Pygame, start recording

    gameloops.startscreen()
    gameloops.dataentryscreen()

    gameloops.instructionscreen()
    pygame.mouse.set_visible(False)
    gameloops.baselineLoop() #work in progress

    gameExit = False
    curmove = 0
    while not gameExit: # outer loop for quitting

        
        gameloops.exp_tools.baselining = False
        curmove = gameloops.levelLoop(gameloops.exp_tools.baselining, curmove)
        
        if gameloops.exp_tools.gameTime > 200:
            gameExit = True
    
    gameloops.exp_tools.datalogger()
    gameloops.exp_tools.datasaver()
    
    gameloops.baselineLoop()
    pygame.quit()

if __name__ == "__main__":
    main()
