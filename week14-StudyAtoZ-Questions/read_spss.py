# import csv
# import savReaderWriter
# with savReaderWriter.SavReader("Resultate_Sternberg_Empra_I_SS2018.sav", returnHeader=True) as reader:
#     with open('results.csv', 'w') as csvfile:
#         spamwriter = csv.writer(csvfile, delimiter=',')
#         header = reader.next()
#         for record in reader:
#             spamwriter.writerow(record)
#
# rename_mapper = dict(zip(["b'VP_Nr'", "b'Alter'", "b'Geschlecht'", "b'RT_1_1'", "b'RT_2_1'",
#        "b'RT_3_1'", "b'RT_4_1'", "b'RT_5_1'", "b'RT_6_1'", "b'RT_1_2'",
#        "b'RT_2_2'", "b'RT_3_2'", "b'RT_4_2'", "b'RT_5_2'", "b'RT_6_2'",
#        "b'mRT_ja'", "b'Anzahl_Ziffern'", "b'mRT_nein'"],
# ["VP_Nr", "Alter", "Geschlecht", "RT_1_1", "RT_2_1",
#        "RT_3_1", "RT_4_1", "RT_5_1", "RT_6_1", "RT_1_2",
#        "RT_2_2", "RT_3_2", "RT_4_2", "RT_5_2", "RT_6_2",
#        "mRT_ja", "Anzahl_Ziffern", "mRT_nein"]))
# df = pd.read_csv('results.csv').rename(mapper=rename_mapper, axis="columns")



import pandas as pd
import numpy as np
df = pd.read_csv('results.csv', index_col=0)
all_subs = df.drop(["mRT_ja", "Anzahl_Ziffern", "mRT_nein"], axis="columns")
all_subs.head()

averaged = df[["mRT_ja", "Anzahl_Ziffern", "mRT_nein"]].dropna()
averaged
