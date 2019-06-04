import pandas as pd
import os

df = pd.read_csv("Results_Sternberg_merged.csv", sep="\t")
df.head()
df2 = df.drop(['Session', 'Clock.Information', 'DataFile.Basename', 'Display.RefreshRate',
       'RuntimeCapabilities',
       'RuntimeVersion', 'RuntimeVersionExpected',
       'StudioVersion', 'SessionStartDateTimeUtc',
       'BlockList.Cycle',
       'PracticeMode', 'Running[Block]',
       'CorrectAnswer', 'digit', 'Digit1', 'Digit2', 'Digit3', 'Digit4',
       'Digit5', 'Digit6', 'Digits', 'Duration1', 'Duration2', 'Duration3',
       'Duration4', 'Duration5', 'Duration6', 'F_DigitPresent',
       'F_NumberDigits', 'PracticeList', 'PracticeList.Cycle',
       'PracticeList.Sample', 'Procedure[Trial]',
       'Running[Trial]', 'TargetDigit',
       'TargetDisplay.CRESP', 'TargetDisplay.RESP',
       'TargetDisplay.RTTime', 'TrialList', 'TrialList.Cycle',
       'TrialList.Sample', 'DigitDisplay.RT', 'DisplayList',
       'DisplayList.Cycle', 'DisplayList.Sample', 'Duration',
       'Procedure[SubTrial]', 'Running[SubTrial]', 'Value', 'SubTrial'
       ], axis="columns").drop_duplicates().reset_index().drop("index", axis="columns")

df2.head()

os.makedirs("subjdata", exist_ok=True)


with open("homework11-samplesolution/data/sternberg_task_01.xpd", "r") as f:
    txt = ""
    for i in f.readlines():
        if i.startswith("#"):
            txt += i
    txt = txt[:-2]

for n, subj in df2.groupby("Subject"):
    df = pd.DataFrame(subj[["Subject", "Procedure[Block]", "NumberDigits", "PresentAbsent", "TargetDisplay.ACC", "TargetDisplay.RT"]])
    df = df.rename(mapper={"Subject": "subject_id", "Procedure[Block]": "Block",
                           "NumberDigits": "Length", "TargetDisplay.RT": "Response Time"}, axis="columns")
    df["Does Appear"] = df["PresentAbsent"] == "present"
    df["Correct Answer"] = df["TargetDisplay.ACC"] == 1.0
    df = df.replace("PracticeBlock", "Practice").replace("TrialBlock", "First Block")
    df = df.reset_index().drop(["PresentAbsent", "TargetDisplay.ACC", "index"], axis="columns")
    df.iloc[72:]["Block"] = "Second Block"
    df.to_csv("data/sternberg_task_"+str(df.iloc[0]["subject_id"]).zfill(3)+".xpd")
    df = df[['subject_id', 'Block', 'Length', 'Does Appear', 'Correct Answer', 'Response Time']]
    this_txt = ""
    with open("data/sternberg_task_"+str(df.iloc[0]["subject_id"]).zfill(3)+".xpd", "r") as f:
        for num, line in enumerate(f.readlines()):
            this_txt += line[line.find(",")+1:]
    with open("data/sternberg_task_"+str(df.iloc[0]["subject_id"]).zfill(3)+".xpd", "w") as f:
        f.write(txt)
        f.write(str(df.iloc[0]["subject_id"]))
        f.write("\n")
        f.write(this_txt)




# df2 = pd.read_csv("data/sternberg_task_102.xpd")
# df
#
# df3 = pd.read_csv("homework11-samplesolution/data/sternberg_task_01.xpd", comment="#")
# df3
