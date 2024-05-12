import pandas as pd

#Import csv through relative pathing
data = pd.read_csv("/mnt/c/Users/user/Downloads/Exam_Table.csv",skip_blank_lines=True).dropna()

data.transpose().to_csv("./b7_output1.csv")

