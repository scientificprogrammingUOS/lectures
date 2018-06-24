from expyriment import misc
import os

data_folder = os.path.join(os.path.dirname(__file__), "data/")
print(data_folder)
misc.data_preprocessing.write_concatenated_data(data_folder, "responsetime_", output_file="data.csv")