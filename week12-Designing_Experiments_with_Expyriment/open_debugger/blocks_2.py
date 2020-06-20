from expyriment import design, control, stimuli, misc, io
import pandas as pd


def load_df(name):
    df = pd.read_csv(name, sep=';', skip_blank_lines=True, index_col='Index')
    df = df.dropna(subset=['Exp'])
    for column in ['Item', 'Condition', 'List_Num']:
        df[column] = df[column].astype('Int8')
    df['is_pract'] = df['is_pract'].astype('bool')
    df.index = df.index.astype('Int32')
    return df


control.set_develop_mode(False)
control.defaults.window_mode = True
control.defaults.window_size = [800, 600]
control.defaults.initialize_delay = 0

exp = design.Experiment(name="My Experiment")
control.initialize(exp)

conditions = load_df("../bws_study.csv").dropna().groupby("Condition")
print() #[data for nr, data in conditions]
for nr, data in conditions:
    block = design.Block(name="Condition" + str(int(nr)))
    block.set_factor("Condition", nr)
    for nr, sents in data.iterrows():
        t = design.Trial()
        t.set_factor("ItemNum", sents["Item"])
        for sent in ["S1", "S2", "S3", "S4", "S5", "S6", "S7"]:
            s = stimuli.TextLine(text=sents[sent], text_size=20)
            t.add_stimulus(s)
        block.add_trial(t)
    exp.add_block(block)

exp.add_bws_factor("FallsWennCondition", ["Wenn-Condition", "Falls-Condition"])
exp.add_bws_factor("GabGabCondition", ["GabGab-Condition", "GabnichtGab-Condition"])

print() #exp
control.start()

names_to_ids = {block.name: block.id for block in exp.blocks}
if exp.get_permuted_bws_factor_condition("FallsWennCondition") == "Wenn-Condition":
    to_delete = {"Condition2", "Condition6"}
else:
    to_delete = {"Condition1", "Condition5"}

if exp.get_permuted_bws_factor_condition("GabGabCondition") == "GabGab-Condition":
    to_delete.update(["Condition5", "Condition6"])
else:
    to_delete.update(["Condition1", "Condition2"])

print() #exp
for i in to_delete:
    exp.remove_block(exp.find_block(names_to_ids[i])[0])

print("Condition for you:", [i.name for i in exp.blocks])
print(exp.get_permuted_bws_factor_condition("GabGabCondition"))
print(exp.get_permuted_bws_factor_condition("FallsWennCondition"))

for block in exp.blocks:
    for trial in block.trials:
        trial.stimuli[2].present()
        exp.clock.wait(1000)
        trial.stimuli[4].present()
        exp.clock.wait(1000)

control.end()