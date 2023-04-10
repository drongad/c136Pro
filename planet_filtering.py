import pandas as pd
import matplotlib.pyplot as plt
import csv

df1 = pd.read_csv("stars_with_gravity.csv")

distance_data = []
for j in df1.Distance:
    if float(j) <= 100.0:
        distance_data.append(True)

    else:
        distance_data.append(False)

d = pd.Series(distance_data)
star_distance = df1[d]
        
star_distance.reset_index(inplace=True, drop=True)
    
gravity_data = []

for i in star_distance.Gravity:
    if float(i) > 150.0 and float(i)<350.0:
        gravity_data.append(True)

    else:
        gravity_data.append(False)

g = pd.Series(gravity_data)

gravity_value = star_distance[g]

gravity_value.reset_index(inplace=True, drop=True)

gravity_value.to_csv("filtered_stars.csv")
