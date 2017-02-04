import pygame
from gamedisplay import *
import time
import os
from Textwrapper import *

class Textwriter(object):

    def __init__(self, screenSize, game_display):

        self.screenSize = screenSize
        self.game_display = game_display

    def text_objects(self, text, TextConf, color):
        TextSurface = pygame.font.Font.render(TextConf, text, True, color)
        return TextSurface, TextSurface.get_rect()

    def instructions(self):
        font = pygame.font.Font('freesansbold.ttf', self.screenSize[0]/45)

        string = "This space is for the instructions for the experiment\n\n\n\n\nYou will now play a training phase to get used to the game. Relax and enjoy the game.\n\n\n\n\n"

        rect = pygame.Rect(( self.screenSize[0]*0.1,  self.screenSize[1]*0.1, self.screenSize[0]*0.85,  self.screenSize[1]*0.7))

        rendered_text = render_textrect(string, font, rect, white, menu_background, 0)

        self.game_display.blit(rendered_text, rect.topleft)

    def message_display(self, text, size ,xpos ,ypos, pause, color):
        TextConf = pygame.font.Font('freesansbold.ttf', size)
        TextSurface, TextRectangle = self.text_objects(text, TextConf, color)
        TextRectangle.center = (xpos, ypos)
        self.game_display.blit(TextSurface, TextRectangle) #display it
        pygame.display.flip()
        time.sleep(pause)
        TextRectCoord = (TextRectangle[0], TextRectangle[0]+TextRectangle[2], TextRectangle[1], TextRectangle[1]+TextRectangle[3])
        return(TextRectCoord)

    def player_death(self):
        self.message_display('You died horribly', self.screenSize[0]/13, self.screenSize[0]/2, self.screenSize[1]/2, 1, black)

    def welcome(self):
        return self.message_display('Endlessrunner of Doom',  self.screenSize[0]/20, self.screenSize[0]/2, self.screenSize[1]*0.25, 0.5, black)

    def entryinstructions(self):
        return self.message_display('Please enter the requested data and confirm with Enter',  self.screenSize[0]/45, self.screenSize[0]/2, self.screenSize[1]*0.33, 0.6, white)

    def start(self):
        return self.message_display('Start Game', self.screenSize[0]/40, self.screenSize[0]/2, self.screenSize[1]/2, 0, white)

    def exit(self):
        return self.message_display('Exit Game  &  Save Data', self.screenSize[0]/40, self.screenSize[0]/2, self.screenSize[1]/2 + 100, 0, white)

    def back(self):
        return self.message_display('Back',  self.screenSize[0]/40, self.screenSize[0]*0.15, self.screenSize[1]*0.85, 0, black)

    def acknowledge(self):
        return self.message_display('Continue by pressing Enter', self.screenSize[0]/40, self.screenSize[0]*0.5, self.screenSize[1]*0.9, 0, black)

    def performance_counter(self, time):
        self.message_display('You survived '+ str(time) + ' Seconds',  self.screenSize[0]/85, 140, 15, 0, red)
