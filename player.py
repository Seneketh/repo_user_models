
class PlayerCube(object):
    def __init__(self, xsize, ysize, speed, xloc, yloc):
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

    def changePosition(self, xchan):
        """
        :param xloc: new location
        """
        self.xloc += xchan
