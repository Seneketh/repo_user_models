
class PlayerCube(object):
    def __init__(self, xsize, ysize, speed, xloc, yloc, range):
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
        self.yloc = yloc - self.ysize
        self.range = range - self.xsize

    def changePosition(self, xchan):
        """
        :param xloc: new location
        """
        if 0 <= self.xloc + xchan <= self.range:
            self.xloc += xchan

    def detectCollision(self, obstacles):
        for cube in obstacles:
            if self.yloc + self.ysize > cube.yloc + cube.ysize >= self.yloc:
                bounds = cube.xsize
                if self.xloc + self.xsize > cube.xloc + bounds >= self.xloc:
                    return(True)
                elif self.xloc + self.xsize > cube.xloc >= self.xloc:
                    return (True)
        return False



