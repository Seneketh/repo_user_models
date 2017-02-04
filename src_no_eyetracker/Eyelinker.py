#from pylink import *
# MUST BE UNCOMMENTED WHEN WHEN WORKING WITH EYETRACKER!!
import pygame

class Eyehandler(object):

    def __init__(self, _rectWidth, _rectHeight, _useEDF=  False ):
        self.tracker = EyeLink()
        pylink.openGraphics()
        self.useEDF = _useEDF

        if self.useEDF:
            getEYELINK().openDataFile("TEST.EDF") ## Keep all characters uppercase when soft coding (recommend string.upper())


        pylink.flushGetkeyQueue()
        getEYELINK().setOfflineMode()


        #Gets the display surface and sends a mesage to EDF file;
        self.rectWidth = _rectWidth
        self.rectHeight = _rectHeight
        getEYELINK().sendCommand("screen_pixel_coords =  0 0 %d %d" %(self.rectWidth, self.rectHeight))
        getEYELINK().sendMessage("DISPLAY_COORDS  0 0 %d %d" %(self.rectWidth, self.rectHeight))

        getEYELINK().sendCommand("select_parser_configuration 0")

        getEYELINK().sendCommand("file_event_filter = LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON")
        getEYELINK().sendCommand("file_sample_data  = LEFT,RIGHT,GAZE,AREA,GAZERES,STATUS,HTARGET")

        getEYELINK().sendCommand("link_event_filter = LEFT,RIGHT,FIXATION,SACCADE,BLINK,BUTTON")
        getEYELINK().sendCommand("link_sample_data  = LEFT,RIGHT,GAZE,GAZERES,AREA,STATUS,HTARGET")

        getEYELINK().sendCommand("button_function 5 'accept_target_fixation'");

        pylink.setCalibrationColors( (0, 0, 0),(255, 255, 255));  	#Sets the calibration target and background color
        pylink.setTargetSize(int(self.rectWidth/70), int(self.rectWidth/300));	#select best size for calibration target
        pylink.setCalibrationSounds("", "", "");
        pylink.setDriftCorrectSounds("", "off", "off");


    def doSetup(self):
        getEYELINK().doTrackerSetup()


    def getInfo(self):
        sample = getEYELINK().getNewestSample()
        return sample.getLeftEye().getPupilSize()


    def endSetup(self):
        getEYELINK().startRecording(1,1,1,1)
        pylink.closeGraphics()

        pylink.beginRealTimeMode(100)
