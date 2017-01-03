import pygame
from Textwriter import *


class Gameloops(object):

    # Data storage
    dataDict_list = []
    levelCount = 1
    eyesize = 0
    sizes = []

    def __init__(self, framerate, screenSize, game_display, clock, playerbody, obstacleHandler, Eyeconnection):

        self.textwriting = Textwriter(screenSize, game_display)
        self.screenSize = screenSize
        self.game_display = game_display
        self.clock = clock
        self.playerbody = playerbody
        self.obstacleHandler = obstacleHandler
        self.framerate = framerate
        self.Eyeconnection = Eyeconnection

    def startscreen(self):

        intro = True
        self.game_display.fill((100,100,100))
        pygame.display.update()

        self.textwriting.welcome()

        StartBox = self.textwriting.start()

        ExitBox = self.textwriting.exit()

        pygame.display.update()
        self.clock.tick(15)

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
                    # fieldnames = sorted(list(set(k for d in dataDict_list for k in d)))
                    # with open("cooldat_dilations_endlessrunner.csv", 'w') as out_file:
                    #     writer = csv.DictWriter(out_file, fieldnames=fieldnames, dialect='excel')
                    #     writer.writeheader()
                    #     writer.writerows(dataDict_list)

                    quit()

                if event.type == pygame.QUIT:
                    quit()

    def instructionscreen(self):

        intro = True
        self.game_display.fill((100,100,100))
        pygame.display.update()

        self.textwriting.instructions()

        NextBox = self.textwriting.next()

        BackBox = self.textwriting.back()

        pygame.display.update()
        self.clock.tick(15)

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
        performancetimer = 0

        while not levelQuit: #inner  loop for the levels
            performancetimer += performancetimer + 1/60

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

            ##getiing stuff from eyetracker

            # eyesize = self.Eyeconnection.getInfo()
            # if(mean(sizes) > eyesize):
            #     obstacleHandler.gravity = obstacleHandler.gravity + 1
            # elif(mean(sizes) < eyesize) and obstacleHandler.gravity > 1:
            #     obstacleHandler.gravity = obstacleHandler.gravity - 1

            # global sizes
            # sizes.append(eyesize)

            if collision:

                # storing data
                # global levelCount
                #
                # dataDict_list.append( {'level': levelCount, 'performance': performancetimer, 'pupilsize': sizes} )
                # levelCount += 1 # new level
                # #print(dataDict_list)

                movement = 0
                self.obstacleHandler.restart()
                performancetimer = 0

                self.textwriting.player_death()

            self.obstacleHandler.update()
            self.playerbody.changePosition(movement)

            # graphics call


            updateScreen(self.game_display, self.playerbody, self.obstacleHandler.obstacles)
            self.textwriting.performance_counter(performancetimer)

            # updating the display and wating for frame rate
            pygame.display.flip()
            self.clock.tick(self.framerate)
