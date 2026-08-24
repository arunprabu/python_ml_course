# K-Means Clustering: How It Works, Choosing K

Code: [`kmeans_clustering.py`](./kmeans_clustering.py)

## Supervised vs. unsupervised — what's different here

Every example in
[`src/supervised-learning`](../supervised-learning/house_price_prediction.md)
had a target column: a score, a price, a pass/fail label. The model's
job was to learn the mapping from features to that known answer.

Clustering has no target. We only have features, and we ask the
algorithm to find groups of similar rows **on its own**. That's why
it's called **unsupervised** learning — there's no "correct answer" to
supervise the training with, only structure to discover.

## The scenario

A teacher has each student's average study hours per week and
attendance percentage — but no pre-assigned "performance group" label.
K-Means groups the students into clusters of similar students
automatically, which the teacher can then interpret (at-risk, average,
top performers) and act on.

------------------------------------------------------------------------

## How K-Means works

1. Pick **K** (the number of clusters you want) and place K cluster
   centers, initially at random.
2. Assign every point to its **nearest** center.
3. Move each center to the **average position** of the points now
   assigned to it (hence "K-*means*").
4. Repeat steps 2-3 until the centers stop moving.

```text
Round 1                Round 2                Round 3 (settled)
  ●   ●                  ●●                     ●●●
    ×          ──►      ×  ●          ──►      ×
  ●   ●                    ●●                     ●●●
        ×                     ×                        ×
    ●  ●                   ●●●                      ●●●●

× = cluster center      ● = data point, colored by nearest ×
```

Each round, points can switch which center they're closest to, and the
centers themselves drift toward the middle of their group. This
usually converges in a handful of rounds.

------------------------------------------------------------------------

## Walking through the code

### 1-2. Data and features

```python
X = df[["hours_per_week", "attendance_pct"]]
```

18 students, two measurements each, no labels. Notice there's no `y`
at all — clustering only needs `X`.

### 3. Choosing K — the Elbow Method

```python
for k in range(1, 7):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X)
    print(model.inertia_)
```

`inertia_` measures how tightly points are packed around their
assigned center (lower = tighter). Inertia **always** drops as K
increases — push K all the way to the number of rows, and every point
becomes its own cluster with 0 inertia. That's not useful; it's
overfitting the clustering.

The **elbow method** looks for the point where adding another cluster
stops buying you much — where the inertia curve bends like an elbow:

```text
inertia
  │●
  │ ╲
  │  ╲
  │   ●
  │    ╲___
  │        ●___
  │            ●___●___●
  └───────────────────────── K
    1   2   3   4   5   6

              ↑
         the "elbow" — K=3 here: inertia drops
         steeply through K=3, then flattens out
```

Running the script, inertia goes `5175.9 → 1055.0 → 210.8 → 118.5 →
72.3 → 46.9` for K=1..6. The steepest drops happen through K=3; after
that, each extra cluster buys much less. That's the signal to stop at
**K=3**.

### 4-5. Train with K=3, inspect the clusters

```python
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df["cluster"] = model.fit_predict(X)
```

The three resulting clusters line up with three natural groups in the
data:

| Cluster | Avg hours/week | Avg attendance | Read as |
| --- | --- | --- | --- |
| 2 | 3.3 | 56.2% | At-risk |
| 0 | 9.7 | 79.2% | Average |
| 1 | 17.5 | 94.0% | Top performers |

K-Means never labeled these "At-risk" or "Top performers" itself — it
only found that these three groups of points are close together and
far from the other groups. **Interpreting** what a cluster represents
is always a human step that comes after clustering.

### 6. Assign a new student to an existing cluster

```python
new_student = pd.DataFrame({"hours_per_week": [12], "attendance_pct": [84]})
model.predict(new_student)
```

`.predict()` just finds whichever of the 3 learned centers is closest
to the new point — here, the "Average" cluster.

------------------------------------------------------------------------

## When to use K-Means

- You want to discover natural groupings in data with no existing
  labels — segmentation, grouping similar behavior, exploratory
  analysis.
- You have a rough sense of, or can determine via the elbow method,
  roughly how many groups make sense.
- Your clusters are expected to be reasonably round/compact and
  similar in size — K-Means struggles with oddly-shaped or very
  differently-sized clusters (see
  [`dbscan_clustering.md`](./dbscan_clustering.md) for an alternative).
- You want something fast and simple to run again and again (e.g. on
  updated data) — K-Means scales well to larger datasets.

------------------------------------------------------------------------

## Things to watch for

- **Scale your features first.** K-Means measures distance between
  points — if one feature has a much bigger numeric range than
  another, it will dominate the distance calculation. This example
  skips scaling because both features happen to be on comparable
  ranges (single/low-double digits vs. percentages); see
  [`hierarchical_clustering.md`](./hierarchical_clustering.md) and
  [`customer_segmentation.md`](./customer_segmentation.md) for cases
  where scaling clearly matters.
- **K-Means assigns every point to a cluster, even outliers.** A single
  unusual student will still get dragged into whichever cluster is
  "least far," which can distort that cluster's center.
- **Results depend on the random starting centers.** `n_init=10` (used
  in this script) reruns K-Means 10 times with different random starts
  and keeps the best result, which is the scikit-learn default good
  practice — it avoids getting stuck in a poor local grouping from an
  unlucky first guess.

------------------------------------------------------------------------

## Try it

```bash
python src/unsupervised-learning/kmeans_clustering.py
```

Then try:

- Change `k = 3` to `k = 2` or `k = 4` — do the resulting groups still
  make sense as distinct student profiles?
- Add a new student with very low hours but very high attendance (or
  vice versa) — which cluster do they land in, and does that feel
  right?
