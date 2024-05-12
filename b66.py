import pandas as pd

#Import csv through relative pathing
data = pd.read_csv("/mnt/c/Users/user/Downloads/Exam_Table.csv",skip_blank_lines=True).dropna()

#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html
data["HRID"] = data["Location"].apply(lambda x: x.replace(",","-").replace(" ","")) +"-"+ data["Site"] +"-"+ data["Replicate"].astype(int).astype(str)

data.to_csv("./b6_output1.csv", index=False)