#Show the grating stimulus at different positions

assert '__file__' in locals() #to make sure to not run this inside Jupyter

from psychopy import visual, event, core, data
mywin = visual.Window(size=[800,600], monitor="testMonitor", units="norm", color=[255,255,0])
fixation = visual.GratingStim(win=mywin, size=0.015, pos=[0,0], sf=0, color=-1)
grating = visual.GratingStim(win=mywin, mask="circle", size=0.2, pos=[0,0], sf=3)
event.globalKeys.add(key='escape', func=core.quit)
#we know that stuff...

positions = [-1, -0.5, 0, 0.5, 1]

# 1 repetition of all trials, in sequential order
handler = data.TrialHandler(positions, 1, method='sequential')

# go through all trials as given by the TrialHandler
for trial in handler:
    # set grating stimulus to new position
    grating.setPos([trial,0])
    fixation.draw()
    grating.draw()
    mywin.flip()
    event.waitKeys()