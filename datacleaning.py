import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

df.drop(["Unnamed: 0","Luminosity",'Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1'], axis = 1, inplace = True)
print(df.columns)
df = df.dropna()

df.reset_index(drop=True, inplace=True)
df.to_csv("final.csv")
