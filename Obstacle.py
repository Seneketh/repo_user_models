from random import randint;
import numpy

screenSize = (800, 800)

class ObstacleCube(object):

    def __init__(self, xsize, ysize, xloc, yloc):
        """
        :param xsize: width size
        :param ysize: length size
        :param xloc: initial x location in the screen
        :param yloc: intital y location in the screen
        :return: obstacle object
        """
        self.xsize = xsize
        self.ysize = ysize
        self.xloc = xloc
        self.yloc = yloc

    def changePostion(self, ychange):
        """

        :param ychange: speed to travel downward
        :return: nothing
        """
        self.yloc += ychange

class ObstacleList(object):

    def __init__(self, maxObstacles, worldsize, gravity, cubex, cubey):
        """

        :param maxObstacles: maximum amount of obstacles on the list
        :param worldsize: tuple representing the scale of the plane to project on
        :param gravity: downward speed of obstacles
        :param cubex: integer representing cubewidth
        :param cubey: integer representing cubeheight
        :return: ObstacleList object
        """
        self.obstacles = []
        self.maxObstacles = maxObstacles
        self.maxLocation = worldsize[1]
        self.minLocation = 0
        self.gravity = gravity
        self.xRange = worldsize[0]
        self.cubex = cubex
        self.cubey = cubey

    def populate(self):
        y_pixel_lanes = numpy.arange(0, screenSize[1]/2, screenSize[1]/40)
        x_pixel_lanes = numpy.arange(0, screenSize[0], screenSize[1]/8)

        #probabilities of lanes:
        index_x = numpy.random.choice(numpy.arange(0, 8), p=[0.125, 0.125, 0.125, 0.125, 0.125, 0.125 , 0.125 , 0.125])
        index_y = numpy.random.choice(numpy.arange(0, 20), p=[0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])


        for i in range(self.maxObstacles):
            xpos = x_pixel_lanes[index_x]
            ypos = y_pixel_lanes[index_y]
            nextObstacle = ObstacleCube(self.cubex, self.cubey, xpos, ypos)
            self.obstacles.append(nextObstacle)


    def update(self):
        if len(self.obstacles) < self.maxObstacles:
            xpos = randint(0, self.xRange)
            nextObstacle = ObstacleCube(self.cubex, self.cubey, xpos, self.minLocation + randint(0,10))
            self.obstacles.append(nextObstacle)

        for cube in self.obstacles:
            if cube.yloc > self.maxLocation:
                self.obstacles.remove(cube)
            cube.changePostion(self.gravity)

    def restart(self):
        self.obstacles.clear()
        self.populate()
