# Things we'll likely need to integrate in our script

# --------------------------------------------------------------
# Start Up

# Import sections
from pylink import * #base pylink module
import gc  # garbage collection (did we need to shut this off?)
import sys  # file operations
import time # necessary for timing


eyelinktracker = EyeLink() # this way, it can be switched to =none to test without eyetracker

# graphics initialization
pylink.openGraphics()

#Opens the EDF file.
edfFileName = "TEST.EDF"; # think we need to make this dynamic. no more than 9 symbols,
                          # all upper case XOR all lower case XOR all numbers
getEYELINK().openDataFile(edfFileName)		

# Eyetracker configuration
pylink.flushGetkeyQueue(); 
getEYELINK().setOfflineMode();  

#Gets the display surface and sends a mesage to EDF file;
surf = pygame.display.get_surface()
getEYELINK().sendCommand("screen_pixel_coords =  0 0 %d %d" %(surf.get_rect().w, surf.get_rect().h))
getEYELINK().sendMessage("DISPLAY_COORDS  0 0 %d %d" %(surf.get_rect().w, surf.get_rect().h))

# Eyetracker setting overrides, seems we can hardcode the settings in the experiment?
# set EDF file contents
# ! need to find out version of EyeLink tracker!
getEYELINK().sendCommand("file_event_filter = LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON")
if tracker_software_ver>=4:
	getEYELINK().sendCommand("file_sample_data  = LEFT,RIGHT,GAZE,AREA,GAZERES,STATUS,HTARGET")
else:
	getEYELINK().sendCommand("file_sample_data  = LEFT,RIGHT,GAZE,AREA,GAZERES,STATUS")

# EL calibration settings, well need to adapt it to our colours
pylink.setCalibrationColors( (0, 0, 0),(255, 255, 255));  	#Sets the calibration target and background color
pylink.setTargetSize(int(surf.get_rect().w/70), int(surf.get_rect().w/300));	#select best size for calibration target
pylink.setCalibrationSounds("", "", "");
pylink.setDriftCorrectSounds("", "off", "off");

# --------------------------------------------------------------
# during the program

# while EL is still running and connected
if(getEYELINK().isConnected() and not getEYELINK().breakPressed()):
	gcwindow_trial.run_trials(surf)

#Do the tracker setup at the beginning of the experiment.
	getEYELINK().doTrackerSetup()

	for trial in range(NTRIALS):
		if(getEYELINK().isConnected() ==0 or getEYELINK().breakPressed()): break;

		while 1:
			ret_value = do_trial(trial, surface)
			endRealTimeMode()
		
			if (ret_value == TRIAL_OK):
				getEYELINK().sendMessage("TRIAL OK");
				break;
			elif (ret_value == SKIP_TRIAL):
				getEYELINK().sendMessage("TRIAL ABORTED");
				break;			
			elif (ret_value == ABORT_EXPT):
				getEYELINK().sendMessage("EXPERIMENT ABORTED")
				return ABORT_EXPT;
			elif (ret_value == REPEAT_TRIAL):
				getEYELINK().sendMessage("TRIAL REPEATED");
			else: 
				getEYELINK().sendMessage("TRIAL ERROR")
				break;
				
	return 0;

while 1:
		error = getEYELINK().isRecording()  # First check if recording is aborted 
		if error!=0:
			end_trial();
			return error

#For each Trial

#Drift correction
	while 1:
		# Checks whether we are still connected to the tracker
		if not getEYELINK().isConnected():
			return ABORT_EXPT;			
		
		# Does drift correction and handles the re-do camera setup situations
		try:
                        print surf.get_rect().w/2,surf.get_rect().h/2
			error = getEYELINK().doDriftCorrect(surf.get_rect().w/2,surf.get_rect().h/2,1,1)
			if error != 27: 
				break;
			else:
				getEYELINK().doTrackerSetup();
		except:
			break #getEYELINK().doTrackerSetup()

# possible useful commands (see Python Pygame/Psychopy manual for details) 
getTrackerVersion()
sendMessage(message_text)


# reading pupil size
newSample = EYELINK.getFloatData()
gaze = newSample. getLeftEye().getGaze()
left_eye_gaze_x = gaze[0]
getPupilSize()

# --------------------------------------------------------------
# shutdown procedure
if getEYELINK() != None:
	# File transfer and cleanup!
	getEYELINK().setOfflineMode();                          
	msecDelay(500);                 

	#Close the file and transfer it to Display PC
	getEYELINK().closeDataFile()
	getEYELINK().receiveDataFile(edfFileName, edfFileName)
	getEYELINK().close();

#Close the experiment graphics	
pylink.closeGraphics()
pygame.display.quit()
