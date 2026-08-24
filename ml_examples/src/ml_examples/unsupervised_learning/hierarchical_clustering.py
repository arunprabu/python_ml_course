import pandas as pd

from scipy.cluster.hierarchy import linkage
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler

"""
HIERARCHICAL CLUSTERING

K-Means needs you to decide K up front. Hierarchical Clustering instead
builds a whole TREE of clusters — starting with every point as its own
cluster, then repeatedly merging the two closest clusters, one merge at
a time, until everything is in a single cluster. You then decide
afterwards, by looking at the tree, how many clusters make sense.

Scenario: group animals by two physical traits (weight, height) with
no predefined categories, and see which animals the algorithm decides
are "close" to each other, and in what order.

IMPORTANT: weight_kg ranges from 0.02 to 5000, but height_cm only
ranges from 8 to 300. Without scaling, weight alone would dominate the
distance calculation and height would barely matter. We fix this with
StandardScaler, which puts every feature on the same scale (mean 0,
standard deviation 1) before measuring distance. This matters for
K-Means and DBSCAN too — any distance-based algorithm needs comparable
feature scales.
"""


# 1. DATA — animals with two physical measurements, no category labels

data = {
    "animal": ["Mouse", "Cat", "Dog", "Wolf", "Goat", "Pig", "Horse", "Cow", "Elephant"],
    "weight_kg": [0.02, 4.5, 20, 40, 60, 90, 400, 600, 5000],
    "height_cm": [8, 25, 50, 70, 75, 60, 150, 140, 300],
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# 2. FEATURES (X) — scale before measuring distance

X = df[["weight_kg", "height_cm"]]
X_scaled = StandardScaler().fit_transform(X)


# 3. THE MERGE ORDER — what hierarchical clustering actually builds
#
# `linkage` returns every merge step: which two clusters combined, how
# far apart they were, and how many animals ended up in the result.
# This is the raw data behind a dendrogram (a tree diagram) — see
# hierarchical_clustering.md for what that tree looks like drawn out.

Z = linkage(X_scaled, method="ward")

print("\nMerge steps (ward linkage):")
cluster_names = {i: name for i, name in enumerate(df["animal"])}
next_id = len(df)
for step, (a, b, distance, size) in enumerate(Z, start=1):
    a, b = int(a), int(b)
    name_a = cluster_names[a]
    name_b = cluster_names[b]
    merged_name = f"({name_a} + {name_b})"
    cluster_names[next_id] = merged_name
    print(f"  Step {step}: merge {name_a!r} and {name_b!r} at distance {distance:.2f}")
    next_id += 1


# 4. CUT THE TREE — turn the merge order into actual cluster labels

k = 3
model = AgglomerativeClustering(n_clusters=k, linkage="ward")
df["cluster"] = model.fit_predict(X_scaled)

print(f"\nClustered with K={k}:")
print(df)
