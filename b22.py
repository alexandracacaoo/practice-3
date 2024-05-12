import pandas as pd

#Import csv through relative pathing
data = pd.read_csv("/mnt/c/Users/user/Downloads/Exam_Table.csv",skip_blank_lines=True).dropna()

#Filtering data by column
output = data[data["Genus"].str.match("st", case=False)]

#Output File
output.to_csv("./b22_output1.csv", index=False)
