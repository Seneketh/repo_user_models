import numpy

screenSize = (1000, 1000)

y_pixel_lanes = numpy.arange(0, screenSize[1]/2, screenSize[1]/40)

x_pixel_lanes = numpy.arange(0, screenSize[0], screenSize[1]/8)


choice = numpy.random.choice(numpy.arange(1, 7), p=[0.1, 0.05, 0.05, 0.2, 0.4, 0.2])


print(len(y_pixel_lanes))
