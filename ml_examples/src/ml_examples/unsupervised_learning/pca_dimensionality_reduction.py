import pandas as pd

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

"""
PRINCIPAL COMPONENT ANALYSIS (PCA)

PCA is not a clustering algorithm — it's a DIMENSIONALITY REDUCTION
technique. It takes many (possibly correlated) numeric features and
finds a smaller set of new features, called PRINCIPAL COMPONENTS, that
still capture most of the original variation in the data.

Scenario: we have exam scores for 15 students across 5 subjects —
Math, Physics, Chemistry, English, History. That's 5 numbers per
student, which is hard to plot or reason about at once. PCA compresses
them down to a couple of components we can actually look at.

Why this works here: a student who is strong in Math tends to also be
strong in Physics and Chemistry (all three move together), and a
student strong in English tends to also be strong in History. The 5
subject scores aren't really 5 independent pieces of information —
they're mostly driven by ONE underlying trait: how STEM-inclined vs
Humanities-inclined the student is. PCA finds that trait automatically.
"""


# 1. DATA — 15 students, 5 subject scores each, no group labels

data = {
    "math":      [88, 92, 78, 95, 85, 90, 42, 38, 48, 52, 35, 45, 65, 72, 58],
    "physics":   [82, 88, 85, 78, 95, 87, 45, 35, 50, 40, 42, 48, 60, 65, 62],
    "chemistry": [90, 85, 80, 92, 75, 88, 40, 45, 42, 48, 38, 50, 68, 60, 55],
    "english":   [48, 35, 55, 42, 50, 38, 88, 92, 80, 85, 90, 78, 62, 55, 68],
    "history":   [40, 45, 38, 50, 33, 42, 82, 90, 85, 78, 92, 80, 58, 62, 65],
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# 2. FEATURES (X) — scale first, since PCA is also distance-based

X = df[["math", "physics", "chemistry", "english", "history"]]
X_scaled = StandardScaler().fit_transform(X)


# 3. FIT PCA with ALL components first, to see how much each one explains

pca_full = PCA().fit(X_scaled)

print("\nExplained variance ratio, per component:")
for i, ratio in enumerate(pca_full.explained_variance_ratio_, start=1):
    print(f"  PC{i}: {ratio:.1%}")

cumulative = pca_full.explained_variance_ratio_.cumsum()
print(f"\nCumulative variance explained by the first 2 components: {cumulative[1]:.1%}")


# 4. KEEP only the first 2 components — that's the actual reduction

pca = PCA(n_components=2)
scores = pca.fit_transform(X_scaled)

df["PC1"] = scores[:, 0].round(2)
df["PC2"] = scores[:, 1].round(2)

print("\nEach student reduced from 5 subject scores down to 2 components:")
print(df[["math", "physics", "chemistry", "english", "history", "PC1", "PC2"]])


# 5. INSPECT — what does each component actually represent?

loadings = pd.DataFrame(pca.components_, columns=X.columns, index=["PC1", "PC2"])

print("\nComponent loadings (how much each subject contributes to each component):")
print(loadings.round(2))
