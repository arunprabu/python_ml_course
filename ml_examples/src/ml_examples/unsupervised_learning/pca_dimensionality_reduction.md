# Principal Component Analysis (PCA) for Dimensionality Reduction

Code: [`pca_dimensionality_reduction.py`](./pca_dimensionality_reduction.py)

## The scenario

We have exam scores for 15 students across 5 subjects — Math, Physics,
Chemistry, English, History. That's 5 numbers per student, which is
hard to plot, visualize, or feed into simpler downstream steps all at
once. PCA compresses those 5 numbers down to a couple of new ones that
still capture most of what makes each student's profile distinct.

PCA is not a clustering algorithm — it doesn't group rows. It's a
**dimensionality reduction** technique: it looks for a smaller set of
new features (**principal components**) that summarize the original
features with as little information loss as possible. It's often used
*before* clustering, to make the clustering faster and less noisy, or
before plotting, to make many-featured data visualizable in 2D.

------------------------------------------------------------------------

## Why this works: correlated features carry redundant information

A student strong in Math tends to also score well in Physics and
Chemistry — those three move together. A student strong in English
tends to also score well in History. So the 5 subject scores aren't
really 5 independent pieces of information about a student — they're
mostly driven by **one** underlying trait: how STEM-inclined vs.
Humanities-inclined that student is.

```text
     Math ─┐
  Physics ─┼── mostly one underlying trait ──► PC1
Chemistry ─┘   (STEM-inclined  ↔  Humanities-inclined)

  English ─┐
  History ─┘
```

PCA finds that underlying trait automatically, without being told
which subjects are "STEM" or "Humanities" — it only looks at how the
numbers move together.

------------------------------------------------------------------------

## Walking through the code

### 1-2. Data and features, scaled

```python
X_scaled = StandardScaler().fit_transform(X)
```

Scaling matters here too: PCA looks for directions of maximum
*variance*, and a feature with naturally larger numbers (or a wider
spread) would dominate that search even if it isn't actually more
informative.

### 3. Fit PCA with all 5 components first

```python
pca_full = PCA().fit(X_scaled)
pca_full.explained_variance_ratio_
```

This doesn't reduce anything yet — it just tells us, if we kept *all*
5 components, how much of the total variation each one accounts for.
Running the script:

```text
PC1: 95.4%
PC2: 2.6%
PC3: 1.4%
PC4: 0.4%
PC5: 0.3%
```

**PC1 alone explains 95.4% of all the variation** across 5 subjects.
That's the payoff of the redundancy above: almost everything that
differs between these students comes down to one axis (STEM ↔
Humanities inclination), so one number captures almost as much as all
five did. PC1 + PC2 together reach 98.0% — keeping just 2 of the 5
original numbers loses barely anything.

### 4. Keep only 2 components — the actual reduction

```python
pca = PCA(n_components=2)
scores = pca.fit_transform(X_scaled)
```

Each student is now described by `(PC1, PC2)` instead of 5 raw scores.
STEM-strong students land at strongly positive PC1 values (around
`+2` to `+2.7`); Humanities-strong students land at strongly negative
PC1 (around `-1.8` to `-3.0`); the more balanced students sit near
`PC1 ≈ 0`. PC2 is a much smaller, secondary signal on top of that.

### 5. Inspect the loadings — what does each component mean?

```python
pca.components_
```

```text
     math  physics  chemistry  english  history
PC1  0.45     0.45       0.44    -0.45    -0.45
```

The **loadings** show how much each original feature contributes to a
component, and with what sign. PC1 weights Math/Physics/Chemistry
*positively* and English/History *negatively*, by almost equal
amounts — confirming that PC1 is essentially "STEM score average minus
Humanities score average." A student with a very positive PC1 is
strongly STEM-leaning; very negative is strongly Humanities-leaning.

------------------------------------------------------------------------

## Reading "explained variance"

Explained variance ratio tells you how much of the original
information a component preserves — **not** how "accurate" or "good" a
model is (PCA isn't predicting anything). A common rule of thumb: keep
enough components to explain 80-95% of the variance, then drop the
rest. Here, keeping just 2 of the original 5 features retains 98% of
the variance — a strong case for reducing from 5 numbers to 2.

------------------------------------------------------------------------

## When to use PCA

- You have **many correlated numeric features** and want to reduce
  redundancy before clustering, plotting, or feeding into another
  model (fewer, less-correlated inputs often help other algorithms
  too).
- You want to **visualize** high-dimensional data — reducing to 2 or 3
  components lets you actually plot it.
- You want to **speed up** downstream computation on wide datasets by
  cutting the number of features while keeping most of the signal.
- Less useful when features are already mostly independent (nothing
  redundant to compress), or when you need to explain predictions in
  terms of the *original* features — components are combinations of
  all the inputs, which makes them harder to interpret directly than
  the loadings table above.

------------------------------------------------------------------------

## Try it

```bash
python src/unsupervised-learning/pca_dimensionality_reduction.py
```

Then try:

- Add a 6th subject, `art`, with scores that don't clearly follow
  either the STEM or Humanities pattern (e.g. uncorrelated with the
  rest). Does PC1's explained variance ratio go up or down?
- Cluster the students using `PC1`/`PC2` with `KMeans(n_clusters=2)`
  (see [`kmeans_clustering.py`](./kmeans_clustering.py) for the
  pattern) — do the resulting clusters match the STEM/Humanities split
  you'd expect from eyeballing PC1?
