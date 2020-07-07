assert '__file__' in locals() #to make sure to not run this inside Jupyter

from psychopy import visual, event
from time import sleep

mywin = visual.Window(size=[800,600], monitor="testMonitor", units="norm", color=[255,255,0])

fixation = visual.GratingStim(win=mywin, size=0.015, pos=[0,0], sf=0, color=-1)
grating = visual.GratingStim(win=mywin, mask="circle", size=0.2, pos=[-0.8,0], sf=3)

#without these, the stimulus is not drawn
fixation.draw()
grating.draw()

#also in psychopy, we draw onto the back buffer, and have to *flip* front and back buffer for the stimuli to be shown 
mywin.flip()

sleep(5)