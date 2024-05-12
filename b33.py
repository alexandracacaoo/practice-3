import pandas as pd

#Import csv through relative pathing
data = pd.read_csv("/mnt/c/Users/user/Downloads/Exam_Table.csv",skip_blank_lines=True).dropna()

#https://pandas.pydata.org/docs/reference/api/pandas.unique.html
sn = data["Scientific Name"].unique()

output = pd.DataFrame({"Scientific Names": sn})

#Output File
output.to_csv("./b33_output1.csv", index=False)