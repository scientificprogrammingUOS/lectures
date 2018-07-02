import pandas as pd
from expyriment import misc
import os
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

# data_folder = "subjdata/"
# print(data_folder)
# misc.data_preprocessing.write_concatenated_data(data_folder, "sternberg_task", output_file="data.csv")


df = pd.read_csv("data.csv", comment="#").sort_values(by="subject_id").dropna()
df = df.rename(mapper={"Does Appear": "does_appear", "Response Time": "response_time", "Correct Answer": "correct_answer"}, axis="columns")
df.head()

NUM_STANDARD_DEVIATIONS = 2

accuracies = df.groupby("subject_id")["correct_answer"].mean()
print("Mean Accuracy by subject:", accuracies.mean(), "Std:", accuracies.std())
min_acc = accuracies.mean()-NUM_STANDARD_DEVIATIONS*accuracies.std()
print("Least Accuracy to be counted:", min_acc)
to_delete = list(accuracies[accuracies<min_acc].index)
print("Deleted will be:", to_delete)
df = df[~df["subject_id"].isin(to_delete)]
df = df[~(df["Block"] == "Practice")]
df = df[df["correct_answer"]].drop("correct_answer", axis="columns")

averaged_times = df.groupby(['subject_id', 'Length', 'does_appear']).mean().reset_index()
global_average = averaged_times.groupby(['Length', 'does_appear'])["response_time"].mean()
global_average.reset_index()

fig, ax = plt.subplots()
for num, obj in global_average.reset_index().groupby("does_appear"):
    obj.plot(x="Length", y="response_time", ax=ax, title="Reaction Time")

ax.legend(["Stimulus does not appear", "Stimulus does appear"])
ax.set(ylabel="Reaction Time (ms)", xlabel="Length of sequence")
plt.show()

fit = smf.ols('response_time ~ does_appear + Length', global_average.reset_index()).fit()
print(fit.summary())
