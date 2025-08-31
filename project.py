import numpy as np
import pandas as pd
from sklearn import linear_model
import warnings
import csv
import os
warnings.filterwarnings("ignore")
result=pd.read_csv(r"E:\salary\Salary_dataset.csv")
reg=linear_model.LinearRegression()
reg.fit(result[["YearsExperience"]],result["Salary"])
file_exists = os.path.isfile("employee.csv")
file=open("employee.csv","a")
w=csv.writer(file)
if not file_exists:
    l=["experience","salary"]
    w.writerow(l)
op="yes"
while op=="yes":
    user=int(input("enter the experience:"))
    l1=[user,*(reg.predict([[user]]))]
    w.writerow(l1)
    op=input("enter do u want to continue...(yes/no)").lower()
file.close()