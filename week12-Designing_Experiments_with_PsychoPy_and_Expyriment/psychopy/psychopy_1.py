assert '__file__' in locals() #to make sure to not run this inside Jupyter

from time import sleep
from psychopy import visual
# create window of size 800x600px on a monitor object we'll call testMonitor and with yellow color
mywin = visual.Window(size=[800,600], monitor="testMonitor", units="norm", color=[255,255,0])

# the scaling unit for object sizes and locations is normalized between -1 and 1
# create grating simulus on our window, size 0.015, center position, spatial frequency 0
# (grating stimulus is otherwise striped), pitch black (-1) color
fixation = visual.GratingStim(win=mywin, size=0.015, pos=[0,0], sf=0, color=-1)
grating = visual.GratingStim(win=mywin, mask="circle", size=0.2, pos=[-0.8,0], sf=3)

sleep(5)