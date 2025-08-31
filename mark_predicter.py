# predict the students scores
import pandas as pd
import numpy as np
from sklearn import linear_model
import csv
f=r"E:\ML_ALGO.py\marks_pridictiction.xlsx"
df=pd.read_excel(f)
reg=linear_model.LinearRegression()
reg.fit(df[["hour_of_study"]],df["marks"])
file=open("marks.csv","w+",encoding='ISO-8859-1')
w=csv.writer(file)
l=["name","hour_study","marks"]
w.writerow(l)
op="yes"
while op=="yes":
    name=input("enter your name:")
    n=int(input("enter the hour you studied:"))
    m=reg.predict([[n]]).item()
    l1=[name,n,m]
    w.writerow(l1)
    op=input("Do you want to continue....(yes/no)").lower()
r=csv.reader(file)
for i in r:
    print(i)
file.close()
