
from player import *
from Obstacle import *
#import timeit
from gamedisplay import *
from numpy import *
import pygame
import time
from random import randint;
import csv # data handling

#screenSize = (1600, 1200)
screenSize = (1366, 768)
#screenSize = (800, 600)
framerate = 60
playersize_x = screenSize[0] * 0.05
playersize_y = screenSize[0] * 0.05
player_speed = 2.5
obstacle_amount = 12
obstacle_speed = 15

# this block here involves the basic initialisation of pygame
pygame.init() # module inititiation
clock = pygame.time.Clock() # defining a clock for controlling frame rate
game_display = pygame.display.set_mode(screenSize, pygame.HWSURFACE  ) #creating a display box
# | pygame.FULLSCREEN

pygame.display.set_caption('Endlessrunner of Doom')

# variables for controlling the loop
gameExit = False
gameLevel = 0


# objexts that are in play
playerbody = PlayerCube(playersize_x, playersize_y, player_speed, screenSize[0]*0.5, screenSize[1] - playersize_y , screenSize)
obstacleHandler = ObstacleList(obstacle_amount, screenSize, obstacle_speed, screenSize[1]/8 ,screenSize[0]/40 )

# cubex/8 and cubey/40 always result in obstacles that have a grid with 20 lanes in y and 40 lanes in x if resolution is div by 2

# Data storage
dataDict_list = []
levelCount = 0

def text_objects(text, TextConf, color):
    TextSurface = pygame.font.Font.render(TextConf, text, True, color)
    return TextSurface, TextSurface.get_rect()

def message_display(text, size , xpos, ypos, pause, color):
    TextConf = pygame.font.Font('freesansbold.ttf', size)
    TextSurface, TextRectangle = text_objects(text, TextConf, color)
    TextRectangle.center = (xpos, ypos)
    game_display.blit(TextSurface, TextRectangle) #display it
    pygame.display.flip()
    time.sleep(pause)
    TextRectCoord = (TextRectangle[0], TextRectangle[0]+TextRectangle[2], TextRectangle[1], TextRectangle[1]+TextRectangle[3])
    return(TextRectCoord)

def player_death():
    performancetimer = time.process_time()
    performancetimer = time.process_time() - performancetimer
    message_display('You died horribly', 90, screenSize[0]/2, screenSize[1]/2, 1, black)
    
def Welcome():
    return message_display('Endlessrunner of Doom', 50, screenSize[0]/2, screenSize[1]/2 - 200, 0.5, black)

def Start():
    return message_display('Start Game', 30, screenSize[0]/2, screenSize[1]/2, 0, black)

def Exit():
    return message_display('Exit Game', 30, screenSize[0]/2, screenSize[1]/2 + 50, 0, black)
    
def performance_counter(time):
    message_display('You survived '+ str(round(time, 1)) + ' Seconds', 20, 140, 15, 0, red)

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

            if mouse[0] > StartBox[0] and mouse[0] < StartBox[1] and mouse[1] > StartBox[2] and mouse[1] < StartBox[3] and click[0] == 1 :
                intro = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                if event.key == pygame.K_RETURN:
                    intro = False


            if mouse[0] > ExitBox[0] and mouse[0] < ExitBox[1] and mouse[1] > ExitBox[2] and mouse[1] < ExitBox[3] and click[0] == 1:
                print("Exit")

                # save all data to file
                fieldnames = sorted(list(set(k for d in dataDict_list for k in d)))
                with open("data.csv", 'w') as out_file:
                    writer = csv.DictWriter(out_file, fieldnames=fieldnames, dialect='excel')
                    writer.writeheader()
                    writer.writerows(dataDict_list)
                            
                quit()

            if event.type == pygame.QUIT:
                quit()


def levelLoop():
    levelQuit = False
    movement = 0 #gets only initialized here. is used in level loop
    performancetimer = 0
          
    while not levelQuit: #inner  loop for the levels
        performancetimer += 1/framerate
        #elapsed_time = time.process_time() - t

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Startscreen()
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

            # storing data
            global levelCount
            dataDict_list.append( {'level': levelCount, 'perf_time': performancetimer, 'mov': movement} )
            levelCount += 1 # new level
            print(dataDict_list)
            
            movement = 0
            obstacleHandler.restart()
            performancetimer = 0

            player_death()

        obstacleHandler.update()
        playerbody.changePosition(movement)

        # graphics call
        updateScreen(game_display, playerbody, obstacleHandler.obstacles)
        performance_counter(performancetimer) #TODO FIX gets redrawn after each collition detectCollision all the time

        # updating the display and wating for frame rate
        pygame.display.flip()
        clock.tick(framerate)


while not gameExit: # outer loop for quitting


    obstacleHandler.restart()
    Startscreen()
    levelLoop()
    
    quit()
