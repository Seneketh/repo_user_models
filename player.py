
class PlayerCube(object):
    def __init__(self, xsize, ysize, speed, xloc, yloc, screenSize):
        """
        :param xsize: width size in pixels (should maybe change to screen size later)
        :param ysize: length size in pixels (should maybe change to screen size later)
        :param speed: players movement speed in percentage of screen per keypress
        :param xloc: initial location in the screen in pixels
        :param yloc: initial location in the screen in pixels
        :return: playercube object
        """
        self.xsize = xsize
        self.ysize = ysize
        self.speed = speed
        self.xloc = xloc
        self.yloc = yloc
        self.screensize = screenSize

    def changePosition(self, xchan):
        """
        :param xloc: new location
        """
        if self.xsize/2 < self.xloc + xchan:
            if self.xloc + xchan <= self.screensize[0] - self.xsize/2:
                self.xloc += xchan
            else:
                self.xloc = self.screensize[0] - self.xsize/2
        else:
            self.xloc = self.xsize/2

    def detectCollision(self, obstacles):
        for cube in obstacles:
            if self.yloc + self.ysize/2 > cube.yloc + cube.ysize >= self.yloc - self.ysize/2:
                bounds = cube.xsize/2
                if self.xloc + self.xsize/2 > cube.xloc + bounds >= self.xloc - self.xsize/2:
                    return(True)
                elif self.xloc + self.xsize/2 > cube.xloc - bounds >= self.xloc - self.xsize/2:
                    return (True)
                elif cube.xloc - bounds < self.xloc < cube.xloc + bounds :
                    return (True)
        return False
