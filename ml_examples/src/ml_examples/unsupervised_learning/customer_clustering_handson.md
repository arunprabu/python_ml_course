# Hands-on: Cluster Customers by Purchase Behavior

Code: [`customer_clustering_handson.py`](./customer_clustering_handson.py)

## The scenario

A retailer tracks two things per customer: how often they visit each
month (`visits_per_month`) and how much they spend per visit on
average (`avg_basket_value`). There's no label for what *type* of
shopper each customer is — we'll let K-Means find that structure, end
to end, following the same workflow shape as
[`linear_regression_handson.py`](../supervised-learning/linear_regression_handson.py)
in the supervised-learning folder.

------------------------------------------------------------------------

## Steps (already implemented in the script)

### STEP 1 — Load the data

```python
data = {"visits_per_month": [...], "avg_basket_value": [...]}
df = pd.DataFrame(data)
```

20 customers. In a real project this would usually come from
`pd.read_csv("customer_purchases.csv")`.

### STEP 2 — Choose features (X)

```python
X = df[["visits_per_month", "avg_basket_value"]]
```

No target column — clustering only needs `X`.

### STEP 3 — Scale the features

```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

`avg_basket_value` (₹12-90) and `visits_per_month` (1-12) are on
different numeric ranges. Distance-based algorithms always risk
letting the larger-range feature dominate, so scaling first is good
practice — in this particular dataset the four groups turn out to be
separated enough in both dimensions that it doesn't actually change
the result (try Exercise 2 below to confirm), but that isn't something
you can assume in general. See
[`hierarchical_clustering.md`](./hierarchical_clustering.md) for a
dataset where skipping this step would clearly break the result.

### STEP 4 — Choose K with the elbow method

```python
for k in range(1, 7):
    model = KMeans(n_clusters=k, random_state=7, n_init=10)
    model.fit(X_scaled)
    print(model.inertia_)
```

Inertia: `40.0 → 20.8 → 7.3 → 1.0 → 0.7 → 0.6`. The sharpest drop is
between K=3 and K=4 (`7.3 → 1.0`) — that's the elbow, and where K=4 is
chosen. See
[`kmeans_clustering.md`](./kmeans_clustering.md) for the full
explanation of why this method works.

### STEP 5 — Train the final model

```python
model = KMeans(n_clusters=4, random_state=7, n_init=10)
df["cluster"] = model.fit_predict(X_scaled)
```

### STEP 6 — Interpret each cluster

```python
profile = df.groupby("cluster")[["visits_per_month", "avg_basket_value"]].mean()
```

| Cluster | Visits/month | Avg basket | Read as |
| --- | --- | --- | --- |
| 0 | 1.4 | ₹16 | Occasional bargain shoppers |
| 3 | 8.2 | ₹21 | Frequent small-basket regulars |
| 2 | 2.4 | ₹83 | Occasional stock-up shoppers |
| 1 | 10.4 | ₹63 | Most valuable customers (frequent + high spend) |

Two independent behaviors — *how often* someone shops and *how much*
they spend per trip — combine into four distinct shopper types. Notice
this is a genuinely 2D pattern: sorting customers by visits alone, or
by basket value alone, would miss the groups entirely. Clustering on
both together is what reveals them.

### STEP 7 — Assign a new customer to a cluster

```python
new_customer = pd.DataFrame({"visits_per_month": [9], "avg_basket_value": [24]})
new_customer_scaled = scaler.transform(new_customer)
model.predict(new_customer_scaled)
```

A customer visiting 9 times a month with a ₹24 average basket lands in
cluster 3 — frequent small-basket regulars — matching the profile
table above.

------------------------------------------------------------------------

## The complete workflow

```text
DATA (no labels)
 ↓
FEATURES ONLY (no target)
 ↓
SCALE FEATURES
 ↓
CHOOSE K (elbow method)
 ↓
TRAIN (KMeans)
 ↓
INTERPRET CLUSTERS (turn numbers into personas)
 ↓
ASSIGN NEW DATA TO A CLUSTER
```

Compare this to the regression workflow in
[`linear_regression_handson.md`](../supervised-learning/linear_regression_handson.md)
— the big structural difference is there's no train/test split and no
accuracy metric to check against, because there's no "right answer" to
measure against. Evaluating a clustering result is closer to *does
this grouping make sense to a human* than *is this number correct*.

Run it:

```bash
python src/unsupervised-learning/customer_clustering_handson.py
```

------------------------------------------------------------------------

## Exercises — try these by editing the script

1. **Change K.** Set `k = 3`. Which two of the four clusters merge
   into one? Does the merged group still make sense as a single
   marketing persona, or does it blur together two customer types that
   should probably be treated differently?
2. **Turn off scaling.** Change `X_scaled` to `X` everywhere (or set
   `X_scaled = X.values`) and re-run with the original `k = 4`. Do the
   clusters actually change here? (They shouldn't — this dataset's
   groups are separated enough in both dimensions to survive it. Now
   compare with
   [`hierarchical_clustering.py`](./hierarchical_clustering.py), where
   `weight_kg` spans `0.02` to `5000` — try removing `StandardScaler`
   there and compare the printed *merge order*, which does change
   noticeably, even though the final 3-cluster grouping happens to
   come out the same.)
3. **Add a third feature.** Add a `days_since_last_purchase` column
   (make up reasonable numbers, e.g. 1-60) and include it in `X`.
   Re-run the elbow method — does K=4 still look like the right choice,
   or does the elbow shift?
4. **Compare to a persona your business already tracks.** If you were
   marketing lead here, which single cluster would you invest the most
   retention budget in, and why?

------------------------------------------------------------------------

## What "good" clustering looks like here

There's no accuracy score to check, so judge the result by:

- **Separation** — are the cluster centers clearly different from each
  other (as in the profile table above), or are several centers nearly
  on top of one another?
- **Interpretability** — can you describe each cluster in one plain
  sentence a non-technical teammate would understand?
- **Stability** — do the clusters stay roughly the same if you change
  `random_state`? Wildly different results from run to run suggest the
  data doesn't have strong natural structure at that K.
