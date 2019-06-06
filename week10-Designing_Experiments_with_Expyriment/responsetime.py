from expyriment import design, control, stimuli, misc, io
import random
control.set_develop_mode(True)

exp = design.Experiment(name="My Experiment")
control.initialize(exp)

fixcross = stimuli.FixCross()
fixcross.preload()
blankscreen = stimuli.BlankScreen()
blankscreen.preload()

b = design.Block(name="Only Block")
for i in range(10):
    waiting_time = random.randint(200, 2000)
    t = design.Trial()
    t.set_factor("waiting_time", waiting_time)
    s = stimuli.Circle(50)
    t.add_stimulus(s)
    b.add_trial(t)
exp.add_block(b)
    
    
exp.data_variable_names = ["Waiting Time", "Response Time"]
    
control.start()

for block in exp.blocks:
    for trial in block.trials:
        fixcross.present()
        exp.clock.wait(trial.get_factor("waiting_time") - trial.stimuli[0].preload())
        trial.stimuli[0].present() 
        button, rt = exp.keyboard.wait(keys=[misc.constants.K_SPACE])
        exp.data.add([trial.get_factor("waiting_time"), rt])
        
            
control.end()            