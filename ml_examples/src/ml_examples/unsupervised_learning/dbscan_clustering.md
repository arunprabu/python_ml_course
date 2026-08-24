# DBSCAN for Density-Based Clustering

Code: [`dbscan_clustering.py`](./dbscan_clustering.py)

## The scenario

A delivery company has drop-off coordinates for a day's deliveries (in
km, on a simple x/y grid from the depot). Most deliveries cluster
around a few busy neighborhoods — but a handful are one-off addresses
far from everything else. We want to find the neighborhoods **and**
flag the one-off addresses as outliers, in a single pass.

------------------------------------------------------------------------

## Why not just use K-Means?

K-Means and Hierarchical Clustering share two assumptions that don't
hold here:

1. **Every point belongs to some cluster.** There's no concept of "this
   point doesn't really belong anywhere" — an outlier still gets
   dragged into whichever cluster happens to be closest.
2. **Clusters are roughly round and similarly sized.** K-Means
   specifically tries to make clusters compact around a center, so if
   you force it to find, say, 3 clusters, it will find *some* 3-way
   split even if the "real" structure is 3 tight neighborhoods plus 3
   scattered outliers.

DBSCAN (**D**ensity-**B**ased **S**patial **C**lustering of
**A**pplications with **N**oise) drops both assumptions. It groups
points that are packed **densely** together, and explicitly labels
anything outside a dense region as **noise** — cluster `-1` — instead
of forcing it somewhere.

------------------------------------------------------------------------

## How it works

DBSCAN takes two settings instead of a K:

- **`eps`** — how close two points need to be to count as neighbors.
- **`min_samples`** — how many neighbors a point needs (within `eps`)
  before it counts as part of a dense region.

Conceptually:

```text
       ┌ eps radius
   ●   │
  ╱ ╲  ▼
 ●   ● ○ ●        ● = point with ≥ min_samples neighbors within eps
  ╲ ╱             → part of a cluster, and can "grow" the cluster
   ●               by pulling in ITS neighbors too

         ●         a lone point with too few neighbors within eps
                    → labeled noise (-1), not forced into any cluster
```

Clusters grow outward through connected dense regions — which is why
DBSCAN can find clusters of unusual or irregular shapes, not just
round blobs, and why isolated points simply never get pulled in.

------------------------------------------------------------------------

## Walking through the code

### 1-2. Data and features

19 delivery coordinates: 6 near one neighborhood, 6 near another, 4
near a third, and 3 scattered far away from anything.

### 3. Train DBSCAN

```python
model = DBSCAN(eps=1.0, min_samples=3)
df["cluster"] = model.fit_predict(X)
```

Running the script:

```text
Found 3 clusters and 3 noise points.
```

The three real neighborhoods come back as clusters `0`, `1`, `2`; the
three scattered addresses all come back labeled `-1` — noise, not
forced into any cluster.

### 4. Compare against K-Means, forced to 3 clusters

```python
kmeans_model = KMeans(n_clusters=3, random_state=0, n_init=10)
df["kmeans_cluster"] = kmeans_model.fit_predict(X)
```

K-Means has no way to say "these 3 points don't belong anywhere" — it
must place every point, including the outliers, into one of exactly 3
clusters. In this run, it even merges two of the real neighborhoods
together (to keep the 3-way split more balanced) while giving one
far-flung outlier its own entire cluster. DBSCAN's result matches
what's actually happening in the data much more closely.

------------------------------------------------------------------------

## Choosing `eps` and `min_samples`

There's no formula that always works, but a few rules of thumb:

- **`min_samples`** — a common starting point is `2 × number of
  features` (so `4` for 2D data); smaller values make DBSCAN more
  tolerant of sparse regions, larger values make it stricter about
  what counts as "dense."
- **`eps`** — too small, and even real clusters fragment into many
  tiny pieces (or become entirely noise); too large, and separate
  clusters start merging into one. In this example, `eps` between
  `0.8` and `1.5` all give the same clean 3-clusters-plus-noise result
  — a sign the parameter choice is robust here, not a lucky guess. A
  more rigorous approach for real data is a **k-distance plot** (plot
  each point's distance to its k-th nearest neighbor, sorted — the
  "elbow" of that curve is a reasonable `eps`).

------------------------------------------------------------------------

## When to use DBSCAN

- You expect **noise/outliers** in the data and want them identified,
  not forced into a cluster.
- Clusters might be **irregularly shaped** (e.g. geographic/spatial
  data, arcs, chains) rather than round blobs.
- You **don't know K** in advance, and don't want to guess it — DBSCAN
  decides the number of clusters from the data and your density
  settings.
- Not a great fit when clusters have very different densities from
  each other — a single `eps` may be too loose for the dense cluster
  and too tight for the sparse one at the same time.

------------------------------------------------------------------------

## Try it

```bash
python src/unsupervised-learning/dbscan_clustering.py
```

Then try:

- Lower `eps` to `0.3` — what happens to the 3 real neighborhoods? Do
  any of them fragment or turn entirely into noise?
- Raise `min_samples` to `6` — does the sparser 4-point neighborhood
  (indices 12-15) survive as its own cluster, or does it get
  reclassified as noise?
