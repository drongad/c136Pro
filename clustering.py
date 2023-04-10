import pandas as pd 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
df = pd.read_csv("stars_with_gravity.csv")

x= df.iloc[:,[3,4]].values()

wcss = []

for i in range(1,11):
  kmeans = KMeans(n_clusters = i, init = "k-means++", random_state = 42)
  kmeans.fit(x)
  #Inertia is amethod that will return wcss for the given model
  wcss.append(kmeans.inertia_)


plt.plot(range(1,11),wcss)
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()