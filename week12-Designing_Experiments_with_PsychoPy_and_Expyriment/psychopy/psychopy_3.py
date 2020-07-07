assert '__file__' in locals() #to make sure to not run this inside Jupyter

from psychopy import visual, event, core

mywin = visual.Window(size=[800,600], monitor="testMonitor", units="norm", color=[255,255,0])

fixation = visual.GratingStim(win=mywin, size=0.015, pos=[0,0], sf=0, color=-1)
grating = visual.GratingStim(win=mywin, mask="circle", size=0.2, pos=[-0.8,0], sf=3)

#global keys kan be pressed at any time during the experiment to executed the specified function
event.globalKeys.add(key='escape', func=core.quit)

fixation.draw()
grating.draw()
mywin.flip()

#without arguments, this waits for any keypress - alternatively, you could specify which keys to look for
event.waitKeys()
mywin.flip()

event.waitKeys()