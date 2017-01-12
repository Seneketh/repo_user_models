from random import randint;
import numpy

def coordMaker(screenSize, xprobabilities = [float(1)/8]*8, yprobabilities = [float(1)/20]*20 ):

    x_pixel_lanes = numpy.arange(0, screenSize[0], screenSize[0]/(len(xprobabilities)))
    y_pixel_lanes = numpy.arange(0, screenSize[1]/2, screenSize[1]/(len(yprobabilities)*2))

    x_pixel_lanes = x_pixel_lanes + (screenSize[0]/8)/2

    #probabilities of lanes:
    index_x = numpy.random.choice(numpy.arange(0, 8), p = xprobabilities)
    index_y = numpy.random.choice(numpy.arange(0, 20), p = yprobabilities)

    return (x_pixel_lanes[index_x], y_pixel_lanes[index_y])


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

    def __init__(self, maxObstacles, screensize, gravity, cubex, cubey):
        """

        :param maxObstacles: maximum amount of obstacles on the list
        :param screensize: size of the canvas to be projected on
        :param gravity: downward speed of obstacles
        :param cubex: integer representing cubewidth
        :param cubey: integer representing cubeheight
        :return: ObstacleList object
        """
        self.obstacles = []
        self.screenSize = screensize
        self.maxObstacles = maxObstacles
        self.maxLocation = screensize[1]
        self.minLocation = 0
        self.gravity = gravity
        self.nextGravity = 11
        self.xRange = screensize[0]
        self.cubex = cubex
        self.cubey = cubey
        self.padding = 2

    def populate(self):
        for i in range(self.maxObstacles):
            coords = coordMaker(self.screenSize)

            xpos = coords[0]
            ypos = coords[1]
            nextObstacle = ObstacleCube(self.cubex, self.cubey, xpos, ypos)
            self.obstacles.append(nextObstacle)


    def update(self):
        self.padding -= 1
        
        if len(self.obstacles) < self.maxObstacles and self.padding == 0:
            coords = coordMaker(self.screenSize)
            

            xpos = coords[0]
            ypos = coords[1]
            nextObstacle = ObstacleCube(self.cubex, self.cubey, xpos, self.minLocation + randint(0,2))
            self.obstacles.append(nextObstacle)

        for cube in self.obstacles:
            if cube.yloc > self.maxLocation:
                self.obstacles.remove(cube)
            cube.changePostion(self.gravity)
            
        if self.padding < 0:
            self.padding = 1

    def restart(self):
        self.obstacles = []
        
