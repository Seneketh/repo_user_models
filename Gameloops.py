import pygame
from Textwriter import *
from gamedisplay import *
from Exptools import *
import numpy
import inputbox
from random import randint


class Gameloops(object):

    def __init__(self, framerate, screenSize, game_display, clock, playerbody, obstacleHandler, eyeconnection):

        self.textwriting = Textwriter(screenSize, game_display)
        self.screenSize = screenSize
        self.game_display = game_display
        self.clock = clock
        self.playerbody = playerbody
        self.obstacleHandler = obstacleHandler
        self.framerate = framerate
        self.eyeconnection = eyeconnection
        self.exp_tools = Exptools(self.framerate, self.clock, self.playerbody, self.obstacleHandler, self.eyeconnection)
        self.menu_tick = 15


    def startscreen(self):

        intro = True
        self.game_display.fill(menu_background)
        pygame.display.update()

        self.textwriting.welcome()

        StartBox = self.textwriting.start()

        ExitBox = self.textwriting.exit()

        self.clock.tick(self.menu_tick)

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
                    self.exp_tools.datasaver()
                    quit()

                if event.type == pygame.QUIT:
                    quit()


    def dataentryscreen(self):

        intro = True
        self.game_display.fill(menu_background)
        pygame.display.update()

        self.textwriting.welcome()
        self.textwriting.entryinstructions()


        self.exp_tools.inp_id = (inputbox.ask(self.game_display, 'Your ID'))
        self.exp_tools.inp_gender = (inputbox.ask(self.game_display, 'Gender'))
        self.exp_tools.inp_age = (inputbox.ask(self.game_display, 'Age'))


        pygame.display.update()
        self.clock.tick(self.menu_tick)

        while intro:

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        intro = False

                    if event.key == pygame.K_RETURN:
                        intro = False


    def instructionscreen(self):

        intro = True
        self.game_display.fill(menu_background)
        pygame.display.update()

        self.textwriting.instructions()

        self.textwriting.acknowledge()

        pygame.display.update()
        self.clock.tick(self.menu_tick)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        intro = False


    def levelLoop(self, baselining):

        levelQuit = False
        movement = 0 #gets only initialized here. is used in level loop

        ## workings of model under normal runtime conditions
        if not baselining:
            ##setting new gravity and doubling it for the next level
            self.obstacleHandler.gravity = self.obstacleHandler.nextGravity
            
            if self.obstacleHandler.gravity <= 15:
                self.obstacleHandler.gravity = 15
                
            self.obstacleHandler.nextGravity = self.obstacleHandler.gravity*1.1
            
        while not levelQuit: #inner  loop for the levels
            self.exp_tools.levelTime += 1/float(self.framerate)
            self.exp_tools.deathTime += 1/float(self.framerate)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:

                        self.startscreen()

                    if event.key == pygame.K_d:
                        movement = self.screenSize[0] * 0.01 * self.playerbody.speed
                    if event.key == pygame.K_a:
                        movement = -self.screenSize[0] * 0.01 * self.playerbody.speed
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        movement = 0
                    if event.key == pygame.K_a:
                        movement = 0

                if event.type == pygame.QUIT:
                    self.startscreen()


            #checking collisions before updating screen
            collision = self.playerbody.detectCollision(self.obstacleHandler.obstacles)
            ## important for eyetracking
            self.exp_tools.pupdil_get()
            ## important for eytracking
            dilationlist = self.exp_tools.pupdil_apnd()
            #dilationlist = [] ##debugging thingy for uncoupling eyelink
            if len(dilationlist) >= 10:
                reference = numpy.nanmean(dilationlist[-9:])
                if baselining:
                    self.exp_tools.smooth_dil.append(reference)
                if reference > self.exp_tools.threshold and not baselining:
                    print("ping")
                    ##update for the ingame gravity
                    self.exp_tools.threscount += 1
                    self.obstacleHandler.nextGravity -= numpy.divide(1.0, self.exp_tools.updateTime * self.framerate*0.1)*self.obstacleHandler.gravity*0.1
                
            if collision:

                self.exp_tools.gameTime += self.exp_tools.levelTime

                self.exp_tools.datalogger()

                #level reset:
                movement = 0
                self.exp_tools.deathTime = 0
                self.obstacleHandler.restart()
                self.textwriting.player_death()


            self.obstacleHandler.update()
            self.playerbody.changePosition(movement)

            # graphics call
            updateScreen(self.game_display, self.playerbody, self.obstacleHandler.obstacles)
            self.textwriting.performance_counter(self.obstacleHandler.gravity)

            # updating the display and wating for frame rate
            pygame.display.flip()
            self.clock.tick(self.framerate)

            if self.exp_tools.levelTime > self.exp_tools.updateTime:
                self.exp_tools.gameTime += self.exp_tools.levelTime

                self.exp_tools.datalogger()
                

                #level reset:
                
                self.exp_tools.threshcount = 0+6
                self.exp_tools.levelTime = 0
                self.exp_tools.level_pupdil = []
                break

    def baselineLoop(self):

        self.exp_tools.baselining = True

        self.obstacleHandler.gravity = self.exp_tools.bldifficulty #initial, difficulty

        while self.exp_tools.bldifficulty >= 20:

            self.exp_tools.bldifficulty -= 2.5
            self.obstacleHandler.gravity = self.exp_tools.bldifficulty

            #self.obstacleHandler.restart()

            self.levelLoop(self.exp_tools.baselining)

        self.exp_tools.set_parameters()
        self.exp_tools.exptools_restart()
        
        
    def controlLoop(self):

        self.exp_tools.levelCounter = 0
        self.exp_tools.baselining = True

        self.obstacleHandler.gravity = self.exp_tools.bldifficulty #initial, difficulty

        while self.exp_tools.levelCounter <= 15:

            self.exp_tools.bldifficulty = randint(15, 50)
            self.obstacleHandler.gravity = self.exp_tools.bldifficulty

            #self.obstacleHandler.restart()

            self.levelLoop(self.exp_tools.baselining)

        self.exp_tools.set_parameters()
        self.exp_tools.exptools_restart()
