import pandas as pd
import csv
import matplotlib.pyplot as plt

df = pd.read_csv("filtered_stars.csv")

name = df["Star_name"].to_list()
radius = df['Radius'].to_list()
mass = df['Mass'].to_list()
gravity = df['Gravity'].to_list()
distance = df['Distance'].to_list()

name.sort()
radius.sort()
mass.sort()
gravity.sort()

plt.plot(name, mass)
plt.title("Name vs. Mass")
plt.xlabel("Name") 
plt.ylabel("Mass") 
plt.show()

plt.plot(name, gravity)
plt.title("Name vs. Gravity")
plt.xlabel("Name") 
plt.ylabel("Gravity") 
plt.show()

plt.plot(name, radius)
plt.title("Name vs. Radius")
plt.xlabel("Name") 
plt.ylabel("Radius") 
plt.show()

plt.scatter(name, distance)
plt.title("name vs. Distance")
plt.xlabel("Name") 
plt.ylabel("Distance") 
plt.show()