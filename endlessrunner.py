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


##GAME PARAMETERS##
#screenSize = (1600, 1200)
screenSize = (1366, 768)
#screenSize = (800, 600)

framerate = 100
playersize_x = screenSize[0] * 0.05
playersize_y = screenSize[0] * 0.05
player_speed = 2.5
obstacle_amount = 12
obstacle_speed = 15
##

##PYGAME INITIALIZATION##
pygame.init() # module inititiation
clock = pygame.time.Clock() # defining a clock for controlling frame rate
game_display = pygame.display.set_mode(screenSize, pygame.HWSURFACE | pygame.FULLSCREEN ) #creating a display box
#
pygame.display.init()
pygame.display.set_caption('Endlessrunner of Doom')
##

# I think this is not required anymore:
# surf = pygame.display.get_surface()
# rectanglethateyetrackerneeds = surf.get_rect()
# width = rectanglethateyetrackerneeds.w
# height = rectanglethateyetrackerneeds.h


##EYETRACKER STUFF##
Eyeconnection = 0 #just so I can work without actually importing eytracker stuff
# Eyeconnection = Eyelinker.Eyehandler(screenSize[0], screenSize[1])
# Eyeconnection.doSetup()
# Eyeconnection.letsGetThePartyStarted()
##

##OBJECTS INITIALIZATION##
playerbody = PlayerCube(playersize_x, playersize_y, player_speed, screenSize[0]*0.5, screenSize[1] - playersize_y , screenSize)
obstacleHandler = ObstacleList(obstacle_amount, screenSize, obstacle_speed, screenSize[1]/8 ,screenSize[0]/40 )
gameloops = Gameloops(framerate, screenSize, game_display, clock, playerbody, obstacleHandler, Eyeconnection)
##


def main():

    gameExit = False
    gameLevel = 1

    while not gameExit: # outer loop for quitting

        obstacleHandler.restart()

        gameloops.startscreen()

        gameloops.instructionscreen()

        gameloops.levelLoop()

        quit()

main()
