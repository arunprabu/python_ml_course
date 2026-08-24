import pandas as pd

from sklearn.cluster import KMeans

"""
K-MEANS CLUSTERING

Every example so far has had a TARGET column (score, price, pass/fail)
that the model was trained to predict — that's SUPERVISED learning.

Clustering is UNSUPERVISED: there is no target. We only have features,
and we ask the model to find groups of similar rows on its own.

Scenario: a teacher has each student's average study hours per week
and attendance percentage, but no "performance group" label. K-Means
groups the students into clusters of similar students automatically.

HOW K-MEANS WORKS (conceptually):
  1. Pick K (the number of clusters) and place K random cluster centers.
  2. Assign every point to its nearest center.
  3. Move each center to the average position of the points assigned to it.
  4. Repeat steps 2-3 until the centers stop moving.
"""


# 1. DATA — students with no performance label, just two measurements

data = {
    "hours_per_week": [2, 3, 4, 3.5, 5, 2.5, 8, 9, 10, 11, 9.5, 10.5, 15, 16, 18, 17, 19, 20],
    "attendance_pct": [50, 55, 60, 58, 62, 52, 75, 78, 80, 82, 79, 81, 90, 92, 95, 93, 96, 98],
}

df = pd.DataFrame(data)

print("Dataset (no labels — just two measurements per student):")
print(df)


# 2. FEATURES (X) — clustering has no y, only X

X = df[["hours_per_week", "attendance_pct"]]


# 3. CHOOSING K — the Elbow Method
#
# Inertia = how tightly packed the points are around their cluster
# center (lower is tighter). Inertia always drops as K increases — with
# K = number of rows, every point is its own cluster and inertia is 0.
# The "elbow" is the K where adding another cluster stops helping much.

print("\nElbow method — inertia for different values of K:")
for k in range(1, 7):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X)
    print(f"  K={k}: inertia = {model.inertia_:.1f}")


# 4. TRAIN the final model with the chosen K

k = 3
model = KMeans(n_clusters=k, random_state=42, n_init=10)
df["cluster"] = model.fit_predict(X)

print(f"\nClustered with K={k}:")
print(df)


# 5. INSPECT the clusters — what does each group look like?

print("\nCluster centers (average hours_per_week, attendance_pct):")
centers = pd.DataFrame(model.cluster_centers_, columns=X.columns)
print(centers.round(1))


# 6. ASSIGN a new student to an existing cluster

new_student = pd.DataFrame({"hours_per_week": [12], "attendance_pct": [84]})
predicted_cluster = model.predict(new_student)[0]

print(f"\nNew student (12 hrs/week, 84% attendance) assigned to cluster: {predicted_cluster}")
