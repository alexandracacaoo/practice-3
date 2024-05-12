import pandas as pd

#Import csv through relative pathing
data = pd.read_csv("/mnt/c/Users/user/Downloads/Exam_Table.csv",skip_blank_lines=True).dropna()

#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html
averages = data.groupby("Scientific Name")["Size Est (cm)"].mean()

#New DataFrame
output = pd.DataFrame({"Scientific Name": ["Pomacentrus adelus"], "Average count": averages["Pomacentrus adelus"]})

#Output File
output.to_csv("./b55_output1.csv", index=False)