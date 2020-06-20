from expyriment import misc
import os

data_folder = os.path.join(os.path.dirname(__file__), "data/")
print("Data Folder:", data_folder)
misc.data_preprocessing.write_concatenated_data(data_folder, "simon_task_short", output_file="data.csv")