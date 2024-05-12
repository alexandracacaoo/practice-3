import pandas as pd

#Import csv through relative pathing
data = pd.read_csv("/mnt/c/Users/user/Downloads/Exam_Table.csv",skip_blank_lines=True).dropna()

sn = data["Scientific Name"].unique()
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html
averages = data.groupby("Scientific Name")["Size Est (cm)"].mean()

#New Dataframe
output = pd.DataFrame({"Scientific Names": sn, "Averages": averages})
#Output File

output.to_csv("./b44_output1.csv", index=False)