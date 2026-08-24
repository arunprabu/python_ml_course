import pandas as pd

from sklearn.cluster import DBSCAN, KMeans

"""
DBSCAN — DENSITY-BASED CLUSTERING

K-Means and Hierarchical Clustering both force every point into some
cluster, and both assume clusters are roughly round/compact blobs.
DBSCAN works differently: it groups together points that are densely
packed, and explicitly labels points that don't belong to any dense
region as NOISE instead of forcing them into a cluster.

Scenario: a delivery company has drop-off coordinates (in km from the
depot, on a simple x/y grid) for a day's deliveries. Most deliveries
cluster around a few busy neighborhoods, but a handful are one-off
addresses far from everything else. DBSCAN finds the neighborhoods
AND flags the one-off addresses as outliers, in a single pass.

DBSCAN has two settings instead of a K:
  eps          -> how close two points must be to count as neighbors
  min_samples  -> how many neighbors a point needs to start/extend a
                  cluster (fewer than that, in a sparse area -> noise)
"""


# 1. DATA — delivery drop-off coordinates, most in three neighborhoods

data = {
    "x_km": [2, 2.2, 1.8, 2.1, 2.4, 1.9, 8, 8.2, 7.9, 8.1, 7.8, 8.3, 15, 15.5, 14.8, 15.2, 0.5, 20, 10],
    "y_km": [3, 3.1, 2.9, 2.7, 3.3, 3.2, 8, 7.8, 8.1, 8.3, 7.9, 8.0, 2, 2.3, 1.8, 2.6, 15, 20, 0.2],
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# 2. FEATURES (X)

X = df[["x_km", "y_km"]]


# 3. TRAIN — DBSCAN labels dense regions as clusters, sparse points as noise (-1)

model = DBSCAN(eps=1.0, min_samples=3)
df["cluster"] = model.fit_predict(X)

print("\nDBSCAN result (cluster -1 means 'noise', not part of any cluster):")
print(df)

n_clusters = len(set(df["cluster"])) - (1 if -1 in df["cluster"].values else 0)
n_noise = (df["cluster"] == -1).sum()
print(f"\nFound {n_clusters} clusters and {n_noise} noise points.")


# 4. COMPARE — force K-Means to find exactly 3 clusters on the same data

kmeans_model = KMeans(n_clusters=3, random_state=0, n_init=10)
df["kmeans_cluster"] = kmeans_model.fit_predict(X)

print("\nFor comparison, K-Means forced into 3 clusters (no noise concept):")
print(df[["x_km", "y_km", "cluster", "kmeans_cluster"]])

print(
    "\nNotice: DBSCAN keeps the three real neighborhoods separate and marks the"
    "\nthree far-away addresses as noise. K-Means has no concept of noise, so it"
    "\nmust force every point (including the outliers) into one of the 3 clusters"
    "\n— and since it also assumes round clusters of similar size, it can even"
    "\nmerge two real neighborhoods together to make the split more 'balanced'."
)
