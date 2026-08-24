# Scenario: Customer Segmentation for Marketing

Code: [`customer_segmentation.py`](./customer_segmentation.py)

## The scenario

A marketing team wants to stop sending the same campaign to every
customer. They have two numbers for each customer:

- `annual_income_k` — annual income, in ₹ thousand
- `spending_score` — a 0-100 score based on purchase behavior (how
  it's computed doesn't matter for this example — treat it as "how
  much this customer tends to spend, relative to others")

There's no "segment" column in the data — no one has told them which
customers are budget-conscious vs. premium vs. anything else. That's
exactly the gap clustering fills: find the natural groupings, then
attach a human-readable persona to each one so marketing can target
campaigns instead of guessing.

------------------------------------------------------------------------

## Why clustering, and why K-Means specifically

This is an unsupervised problem — there's no historical "segment"
label to train against, only two measurements per customer. K-Means is
a natural first choice for segmentation:

- it's fast and easy to re-run as new customer data comes in;
- it produces a fixed number of clean, roughly equal-effort segments —
  which is exactly the shape a marketing team wants (a handful of
  named personas, not one giant cluster and a scatter of one-offs);
- the resulting cluster centers are directly interpretable as "the
  average customer in this segment."

(If the concern were mainly about outlier customers or wildly uneven
segment sizes, [`dbscan_clustering.md`](./dbscan_clustering.md) would
be a better fit — see that file for when density-based clustering
wins over K-Means.)

------------------------------------------------------------------------

## Walking through the code

### 1-2. Data and features, scaled

```python
X = df[["annual_income_k", "spending_score"]]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

25 customers. `annual_income_k` (roughly 18-90) and `spending_score`
(0-100) are on different numeric ranges, so — same reasoning as
[`hierarchical_clustering.md`](./hierarchical_clustering.md) — we
scale both features before measuring distance between customers.

### 3. Choose K — elbow method meets business need

```python
for k in range(1, 7):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X_scaled)
    print(model.inertia_)
```

Inertia drops steeply through K=5 (`50.0 → 25.5 → 10.7 → 3.4 → 0.8`)
and then flattens (`0.8 → 0.4` for K=6) — the elbow method supports
K=5. In this case that also lines up with what the marketing team
actually wants: a handful of distinct, nameable personas to design
campaigns around. The elbow method is a **guide**, not an absolute
law — when it agrees with a business constraint like this, that's a
good sign the choice is reasonable, not just mathematically convenient.

### 4-5. Train with K=5, profile each segment

```python
model = KMeans(n_clusters=5, random_state=42, n_init=10)
df["segment"] = model.fit_predict(X_scaled)

profile = df.groupby("segment")[["annual_income_k", "spending_score"]].mean()
```

Averaging income and spending score *within* each cluster turns raw
cluster numbers into something marketing can act on:

| Segment | Income | Spending | Persona |
| --- | --- | --- | --- |
| 2 | ₹25k | 20 | **Budget-conscious** — price-sensitive, respond to low-cost offers |
| 0 | ₹20k | 76 | **Value seekers** — spend beyond their income bracket, target with loyalty/rewards |
| 4 | ₹54k | 51 | **Mainstream** — general campaigns, upsell opportunities |
| 1 | ₹60k | 25 | **Cautious savers** — can afford to spend more but don't; needs trust-building, not discounts |
| 3 | ₹86k | 85 | **Premium customers** — best targets for high-end campaigns |

This is the real value of clustering in a business setting: the
algorithm only produces 5 groups of coordinates — turning those into
personas with names and a marketing angle is a judgment call a human
makes by looking at each segment's profile.

### 6. Assign a new customer to a segment

```python
new_customer = pd.DataFrame({"annual_income_k": [30], "spending_score": [72]})
new_customer_scaled = scaler.transform(new_customer)
model.predict(new_customer_scaled)
```

A new sign-up with modest income but high spending score lands in
segment 0 — **Value seekers** — telling marketing which campaign to
route them into immediately, without waiting for a manual review.

Note that we reuse the **same** `scaler` fitted on the training
customers, rather than fitting a new one on just this single new row —
a new scaler fit on one data point wouldn't mean anything (no spread
to measure). This mirrors how you'd handle new data with any
distance-based model in production.

------------------------------------------------------------------------

## Things to watch for in a real segmentation project

- **Segments can shift over time.** Re-run clustering periodically as
  customer behavior changes — a segmentation from a year ago may no
  longer reflect reality.
- **Two features is a simplification.** Real segmentation often
  includes more signals (purchase frequency, product categories,
  recency) — K-Means handles more features exactly the same way, just
  add more columns to `X`.
- **Cluster count is a business decision as much as a statistical
  one.** Five clean personas are more useful to a marketing team than
  eight statistically "better" but hard-to-act-on micro-segments.

------------------------------------------------------------------------

## Try it

```bash
python src/unsupervised-learning/customer_segmentation.py
```

Then try changing the new customer's values and see which persona they
land in:

- A high-income, low-spending customer — do they land in "Cautious
  savers" as expected?
- A mid-income, mid-spending customer near ₹55k / score 50 — do they
  land in "Mainstream," or does a small change tip them into a
  neighboring segment?
