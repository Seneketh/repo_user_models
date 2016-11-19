from random import randint;

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

    def __init__(self, maxObstacles, maxLocation, minLocation, gravity, xRange):
        """

        :param maxObstacles: maximum amount of obstacles on the list
        :param maxLocation: upper bound at which an obstacle is destroyed
        :param minLocation: lower bound where the object is spawned
        :param gravity: downward speed of obstacles
        :param xRange: range where obstacles may appear such that [0, Xrange]
        :return: ObstacleList object
        """
        self.obstacles = []
        self.maxObstacles = maxObstacles
        self.maxLocation = maxLocation
        self.minLocation = minLocation
        self.gravity = gravity
        self.xRange = xRange

    def populate(self):
        for i in range(self.maxObstacles):
            xpos = randint(0, self.xRange)
            nextObstacle = ObstacleCube(50, 50, xpos, self.minLocation - self.maxLocation * 1/randint(1, 10))
            self.obstacles.append(nextObstacle)


    def update(self):
        if len(self.obstacles) < self.maxObstacles:
            xpos = randint(0, self.xRange)
            nextObstacle = ObstacleCube(50, 50, xpos, self.minLocation + randint(0,10))
            self.obstacles.append(nextObstacle)

        for cube in self.obstacles:
            if cube.yloc > self.maxLocation:
                self.obstacles.remove(cube)
            cube.changePostion(self.gravity)