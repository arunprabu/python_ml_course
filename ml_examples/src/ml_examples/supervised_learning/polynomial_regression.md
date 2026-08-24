# Polynomial Regression for Non-Linear Data

Code: [`polynomial_regression.py`](./polynomial_regression.py)

## The scenario

A driving school records braking-test results: at each test speed, how
far the car travels before it fully stops. They want a model that
estimates braking distance from speed, to build a "safe following
distance" chart.

Braking distance does **not** grow linearly with speed. A car moving
twice as fast carries roughly four times the kinetic energy, so it
needs roughly four times the distance to stop. Plotting speed against
braking distance produces a curve, not a straight line — a good example
of when plain Linear Regression falls short.

------------------------------------------------------------------------

## Why a straight line struggles here

Linear Regression can only fit:

```text
distance = m * speed + c
```

which is, by definition, a straight line. Forced onto genuinely curved
data, it can only compromise — running a bit too high at some speeds
and a bit too low at others, consistently missing the actual shape of
the relationship. This is called **underfitting**.

```text
distance
  │                                    ● actual data (curved)
  │                              ●
  │                        ●
  │                  ●         ╱  straight-line fit
  │            ●          ╱
  │      ●           ╱
  │ ●          ╱
  └──────────────────────────────── speed
```

------------------------------------------------------------------------

## The idea: add powers of x as extra features

Polynomial Regression is still Linear Regression underneath. The trick
is to feed the model extra columns — `speed²`, `speed³`, and so on —
instead of just `speed`:

```text
distance = m1*speed + m2*speed² + ... + c
```

The model is still a straight line/plane in this expanded feature
space, but plotted back against the original `speed`, it looks like a
curve. `scikit-learn` builds this as two steps chained together:

```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
model.fit(X_train, y_train)
```

`PolynomialFeatures(degree=2)` turns a single column `speed` into
`[speed, speed²]` (plus an intercept term); `LinearRegression` then
fits normally on top of that.

------------------------------------------------------------------------

## Walking through the code

### 1. Load the data

```python
data = {"speed_kmh": [...], "braking_distance_m": [...]}
df = pd.DataFrame(data)
```

Recorded braking distance at 20 test speeds, from 20 km/h to 115 km/h.

### 2-3. Features/target, then train/test split

Same pattern as `linear_regression_basics.py` — `X = df[["speed_kmh"]]`,
`y = df["braking_distance_m"]`, with 25% of the speeds held out for
testing.

### 4. Baseline: plain Linear Regression

```python
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
```

On this data, the straight-line model scores around `R² = 0.70` on the
test set — noticeably worse than it looks at first glance, because it
systematically misses the curve at both the low and high end of the
speed range.

### 5. Polynomial Regression, degree 2

```python
poly_model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
poly_model.fit(X_train, y_train)
```

Adding `speed²` lets the model follow the curve almost exactly —
`R² ≈ 0.998` on the same test set.

### 6. Overfitting warning: degree 8

```python
overfit_model = make_pipeline(PolynomialFeatures(degree=8), LinearRegression())
```

With only 20 data points, an 8th-degree polynomial has more than enough
flexibility to bend through the *training* points almost perfectly —
but it does this by chasing noise, not the underlying trend. On the
test set its R² drops to around `0.58`, **worse than the plain straight
line**. This is the key lesson of Polynomial Regression: more curve
capacity is not automatically better.

```text
distance
  │           training points
  │        ●        ╱╲    ╱╲
  │     ●     ╱╲    ╱  ╲  ╱  ╲     ← high-degree curve
  │  ●    ╱  ╲╱  ╲╱      ╲╱    ╲      "memorizes" training
  │    ╱                          ╲   noise, wiggles wildly
  └──────────────────────────────── speed
```

### 7. Predict for a new speed

```python
new_speed = pd.DataFrame({"speed_kmh": [72]})
poly_model.predict(new_speed)
```

------------------------------------------------------------------------

## Choosing the degree

- **Degree 1** = plain Linear Regression (a straight line).
- **Degree 2-3** is usually enough for gently curved, real-world data
  like this one.
- **High degree** (8+, especially with few data points) tends to
  overfit — great training score, poor test score.

Always compare **train** performance against **test** performance. If
train R² is high but test R² is much lower, the degree is probably too
high.

------------------------------------------------------------------------

## When to use it

- You've plotted `x` vs `y` (or checked residuals from a plain Linear
  Regression) and there's a visible curve, not a straight-line trend.
- You still want an interpretable, fast model rather than jumping
  straight to a more complex non-linear algorithm (trees, neural nets,
  etc.).
- You have relatively few input features — polynomial features
  multiply out quickly with many inputs and a high degree, so this
  technique is best suited to a small number of numeric features.

------------------------------------------------------------------------

## Try it

```bash
python src/polynomial_regression.py
```

Compare the R² printed for the straight-line model, the degree-2 model,
and the deliberately-overfit degree-8 model. Then try:

- Changing `degree=8` to `degree=3` or `degree=4` — does it still
  overfit as badly?
- Changing `test_size` — does the straight-line R² change much? Why
  might a different train/test split expose the underfitting more or
  less clearly?
