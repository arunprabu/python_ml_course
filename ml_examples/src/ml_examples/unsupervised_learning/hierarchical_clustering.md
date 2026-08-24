# Hierarchical Clustering

Code: [`hierarchical_clustering.py`](./hierarchical_clustering.py)

## The scenario

We have nine animals with two physical measurements each — weight and
height — and no predefined species groupings. We want to see which
animals the algorithm considers "close" to each other, and crucially,
**in what order** it decides to group them. That ordering is the whole
point of hierarchical clustering, and it's what
[`kmeans_clustering.py`](./kmeans_clustering.py) doesn't give you.

------------------------------------------------------------------------

## How it's different from K-Means

K-Means needs you to decide K (the number of clusters) *before* it
runs. Hierarchical Clustering instead builds a whole **tree** of
clusters:

- Start with every point as its own cluster.
- Repeatedly merge the two **closest** clusters into one.
- Keep going until everything is merged into a single cluster.

You then decide **afterwards**, by looking at the tree, how many
clusters actually make sense — you can even look at several different
cluster counts from the same tree without re-running anything.

This tree, drawn out, is called a **dendrogram**:

```text
distance
  │
5.5┤                                                    ┌─────────────┐
   │                                                    │  Elephant   │
2.1┤                                          ┌──────────┤             │
   │                                          │          └─────────────┘
0.9┤                                ┌─────────┤ Horse+Cow
   │                     ┌──────────┤         └──────────
0.3┤          ┌──────────┤          │ Mouse+Cat
   │          │Wolf+Goat │Dog+Pig   └──────────
0.1┤ ┌────┐  ┌┴───┐    ┌─┴──┐    ┌──────┐
   │ │Wolf│  │Goat│    │Dog │    │ Pig  │  ...
   └─┴────┴──┴────┴────┴────┴────┴──────┴──────────────────────
```

Every merge happens at some **distance** — how dissimilar the two
groups were when they combined. Cutting the tree with a horizontal
line at a given height gives you clusters: cut low, and you get many
small, tight clusters; cut high, and you get fewer, looser ones.

------------------------------------------------------------------------

## Why scaling matters here

```python
X = df[["weight_kg", "height_cm"]]
X_scaled = StandardScaler().fit_transform(X)
```

`weight_kg` ranges from `0.02` (Mouse) to `5000` (Elephant); `height_cm`
only ranges from `8` to `300`. Left unscaled, a weight difference of
even a few kilograms would swamp a height difference of tens of
centimeters in the distance calculation — height would barely matter
at all. `StandardScaler` puts every feature on a comparable scale
(mean 0, standard deviation 1) before distance is measured. This isn't
specific to hierarchical clustering — **any** distance-based algorithm
(K-Means, DBSCAN, k-NN, ...) needs this when features are on different
scales.

You can see the effect concretely: drop `StandardScaler` here (cluster
directly on `X` instead of `X_scaled`) and Horse and Cow end up split
into *different* clusters once you cut at K=4 — even though they're
each other's closest match among the large animals. On the raw,
unscaled scale, small *absolute* weight/height gaps among the small
animals (Mouse vs. Cat is 4.5kg apart; Wolf vs. Goat is 20kg apart) look
smaller than the 200kg raw gap between Horse and Cow — even though
Horse and Cow are proportionally far more similar to each other than
Wolf is to Goat. So every small-animal pair merges before Horse and Cow
get the chance to, and by the time you've made enough merges to reach 4
clusters, Horse and Cow haven't merged yet and land on opposite sides
of the cut. With scaling, all six small/mid animals merge in
proportional terms instead, and Horse+Cow merge together well before
that boundary.

------------------------------------------------------------------------

## Walking through the code

### 1-2. Data and features

Nine animals, `weight_kg` and `height_cm`, scaled before use.

### 3. The merge order

```python
Z = linkage(X_scaled, method="ward")
```

`linkage` runs the whole merging process and returns every step:
which two clusters combined, and at what distance. Running the script
prints:

```text
Step 1: merge 'Wolf' and 'Goat' at distance 0.06
Step 2: merge 'Dog' and 'Pig' at distance 0.13
Step 3: merge 'Horse' and 'Cow' at distance 0.18
Step 4: merge 'Mouse' and 'Cat' at distance 0.20
Step 5: merge '(Wolf + Goat)' and '(Dog + Pig)' at distance 0.29
Step 6: merge '(Mouse + Cat)' and '((Wolf + Goat) + (Dog + Pig))' at distance 0.92
Step 7: merge '(Horse + Cow)' and [everything so far] at distance 2.06
Step 8: merge 'Elephant' and [everything] at distance 5.54
```

Read this as the story of the whole clustering process: the
mid-sized animals (Wolf/Goat, Dog/Pig) pair up first, at very small
distances. Mouse and Cat — despite being very different in size from
Wolf/Goat — still pair up early because they're close to *each other*.
Horse and Cow, the two large farm animals, form their own pair. Only
at the very end, at a distance **more than twice as large as any
previous merge**, does the Elephant join in — the algorithm is telling
us the Elephant genuinely doesn't resemble anything else in the
dataset. `method="ward"` is one way of measuring how far apart two
*clusters* (not just two points) are — it merges whichever pair keeps
each resulting cluster as internally tight as possible.

### 4. Cut the tree into actual clusters

```python
model = AgglomerativeClustering(n_clusters=3, linkage="ward")
df["cluster"] = model.fit_predict(X_scaled)
```

Cutting at K=3 gives: `{Mouse, Cat, Dog, Wolf, Goat, Pig}`,
`{Horse, Cow}`, and `{Elephant}` alone — small/mid animals, large farm
pair, and the outlier. Looking at the merge distances from step 3
above, this is a sensible place to cut: the jump from merging at 2.06
(step 7) to 5.54 (step 8) is the biggest gap in the whole sequence.

------------------------------------------------------------------------

## When to use Hierarchical Clustering

- You don't want to commit to a specific K upfront — you want to
  explore the data at multiple levels of granularity from one run.
- Your dataset is small-to-medium sized. Computing and storing every
  pairwise distance gets expensive fast (roughly `O(n²)` or worse),
  which makes this a poor fit for very large datasets — K-Means or
  DBSCAN scale better.
- You care about the **relationships between clusters**, not just the
  final grouping — e.g. biological taxonomies, organizational
  hierarchies, document topic trees.

------------------------------------------------------------------------

## Try it

```bash
python src/unsupervised-learning/hierarchical_clustering.py
```

Then try:

- Change `k = 3` to `k = 4` in the last section. Which cluster splits,
  and where does the split happen in the merge-step list?
- Change `method="ward"` to `method="single"` (merges based on the
  closest pair of points between two clusters, rather than overall
  compactness) and compare the merge order — does Elephant still merge
  last?
