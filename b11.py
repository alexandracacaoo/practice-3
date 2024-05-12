import pandas as pd

#Import csv through relative pathing
data = pd.read_csv("/mnt/c/Users/user/Downloads/Exam_Table.csv",skip_blank_lines=True).dropna()

#Filtering data by column
output = data[data["Interval"]=="30-0"]

#Output File
output.to_csv("./b1_output1.csv", index=False)
