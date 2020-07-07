from expyriment import design, control, stimuli, misc, io

control.set_develop_mode(True)

exp = design.Experiment(name="My Experiment")
control.initialize(exp)

for name, color in [["green", misc.constants.C_GREEN], ["red", misc.constants.C_RED]]:
    block = design.Block(name=name.capitalize() + " Stimuli")
    block.set_factor("Color", name)
    for where in [["left", -300], ["right", 300]]:
        t = design.Trial()
        t.set_factor("Position", where[0])
        s = stimuli.Rectangle([50, 50], position=[where[1], 0], colour=color)
        t.add_stimulus(s)
        block.add_trial(t)
    exp.add_block(block)

control.start()

for block in exp.blocks:
    for trial in block.trials:
        trial.stimuli[0].present()
        exp.clock.wait(1000)

control.end()