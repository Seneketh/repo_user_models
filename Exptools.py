import pygame
import csv
import time
import datetime
from random import randint
import numpy as np
class Exptools(object):

    def __init__(self, framerate, clock, playerbody, obstacleHandler, eyeconnection):

        #self.screenSize = screenSize
        self.clock = clock
        self.framerate = framerate
        self.eyeconnection = eyeconnection
        self.level_count = 0
        self.pupdil = 0
        self.dict_list = []
        self.level_pupdil = []
        self.levelTime = 0
        self.gameTime = 0

    def pupdil_get(self, testmode = True):
        '''use in pupdil_apnd'''
        if testmode == True:
            self.pupdil = randint(1000, 2000)
            return self.pupdil
        else:
            # for testing without eyetracker
            self.pupdil = self.eyeconnection.getInfo()
            return self.pupdil

    def pupdil_apnd(self):
        '''during gameloop, remember to set level pubdil to [] on collision'''
        self.level_pupdil.append(self.pupdil)
        return self.level_pupdil

    def datalogger(self):
        '''on collision, set dict list to [] on exit'''

        self.level_count += 1 # new level

        self.dict_list.append(
        {'level': self.level_count,
        'gametime': self.gameTime,
        'leveltime': self.levelTime,
        'mean_pupilsize': np.mean(self.level_pupdil)} )
        #'level_pupdilations': self.level_pupdil
        return self.dict_list

    def datasaver(self):
        '''on exit'''

        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('__%d-%m-%Y__%H:%M:%S')

        fieldnames = sorted(list(set(k for d in self.dict_list for k in d)))
        with open("testdata" + timestamp + ".csv", 'w') as out_file:
            writer = csv.DictWriter(out_file, fieldnames=fieldnames, dialect='excel')
            writer.writeheader()
            writer.writerows(self.dict_list)


# pupdil = self.Eyeconnection.getInfo()
# if(mean(sizes) > pupdil):
#     obstacleHandler.gravity = obstacleHandler.gravity + 1
# elif(mean(sizes) < pupdil) and obstacleHandler.gravity > 1:
#     obstacleHandler.gravity = obstacleHandler.gravity - 1
