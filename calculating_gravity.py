import pandas as pd
import csv

df = pd.read_csv("final.csv")

df.drop(["Unnamed: 0"], axis = 1, inplace = True)
df = df.dropna()


df['Radius']=df['Radius'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

print(df.dtypes)
radius = df['Radius'].to_list()
mass = df['Mass'].to_list()
gravity = []

#converting mass and radius to SI units
def converting_values(mass, radius):
    for i in range(0, len(radius)-1):
        radius[i] = radius[i]*6.957e+8
        mass[i] = mass[i]*1.989e+30
    

converting_values(radius, mass)
# radius to meters and mass to kg
def calculate_gravity(radius, mass):
    G = 6.674e-11
    for i in range(0, len(mass)):
        g = (mass[i]*G)/((radius[i])**2)
        gravity.append(g)

calculate_gravity(radius,mass)
df["Gravity"]= gravity
df.to_csv("stars_with_gravity.csv")




