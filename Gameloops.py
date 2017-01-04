import pygame
from Textwriter import *
from gamedisplay import *
from Exptools import *
import numpy

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
        self.exp_tools = Exptools(framerate, clock, playerbody, obstacleHandler, eyeconnection)
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

                    quit()

                if event.type == pygame.QUIT:
                    quit()

    def instructionscreen(self):

        intro = True
        self.game_display.fill(menu_background)
        pygame.display.update()

        self.textwriting.instructions()

        NextBox = self.textwriting.next()

        BackBox = self.textwriting.back()

        pygame.display.update()
        self.clock.tick(self.menu_tick)

        while intro:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            for event in pygame.event.get():

                if mouse[0] > NextBox[0] and mouse[0] < NextBox[1] and mouse[1] >NextBox[2] and mouse[1] < NextBox[3] and click[0] == 1 :
                    intro = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.startscreen()

                    if event.key == pygame.K_RETURN:
                        intro = False

                if mouse[0] > BackBox[0] and mouse[0] < BackBox[1] and mouse[1] > BackBox[2] and mouse[1] < BackBox[3] and click[0] == 1:
                    self.startscreen()


    def levelLoop(self):

        levelQuit = False
        movement = 0 #gets only initialized here. is used in level loop

        while not levelQuit: #inner  loop for the levels
            self.exp_tools.levelTime += 1/float(self.framerate)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:

                        self.exp_tools.datasaver()

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

            self.exp_tools.pupdil_get()

            self.exp_tools.pupdil_apnd()

            if collision:

                self.exp_tools.gameTime += self.exp_tools.levelTime

                self.exp_tools.datalogger()

                #level reset:
                movement = 0
                self.exp_tools.levelTime = 0
                self.exp_tools.level_pupdil = []
                self.obstacleHandler.restart()
                self.textwriting.player_death()

            self.obstacleHandler.update()
            self.playerbody.changePosition(movement)

            # graphics call
            updateScreen(self.game_display, self.playerbody, self.obstacleHandler.obstacles)
            self.textwriting.performance_counter(round(self.exp_tools.levelTime, 3))

            # updating the display and wating for frame rate
            pygame.display.flip()
            self.clock.tick(self.framerate)
