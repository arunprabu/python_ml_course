# Linear Regression: When to Use, Assumptions, Evaluation

Code: [`linear_regression_basics.py`](./linear_regression_basics.py)

## The scenario

A teacher has a record of how many hours each student studied and the
score they got on the exam. They want a model that estimates a
student's score from hours studied, so they can flag students who look
likely to struggle before the exam happens.

This is the same `hours` data used in
[`student_result_model.py`](./student_result_model.py), which predicts
**pass/fail** from hours studied using Logistic Regression. Here we
predict the actual **score**, a continuous number, using Linear
Regression. Comparing the two side by side is a good way to feel the
difference between regression and classification:

```text
Linear Regression    -> predicts a number       (score: 0-100)
Logistic Regression   -> predicts a class/prob    (pass / fail)
```

------------------------------------------------------------------------

## What is Linear Regression learning?

Linear Regression tries to fit a straight line through the data:

```text
score = m * hours + c
```

`m` is the **slope** — how many extra points a student gains per extra
hour studied. `c` is the **intercept** — the model's baseline score
prediction at 0 hours studied.

```text
              FEATURE
           ┌───────────┐
Student ──►│   hours   │──► Linear Regression ──► score (TARGET)
           └───────────┘
```

------------------------------------------------------------------------

## When to use Linear Regression

- The **target is a continuous number** (score, price, temperature,
  salary) — not a category. If you're predicting a category instead,
  that's classification (see `student_result_model.py`).
- You expect the relationship to be roughly **linear**: as hours studied
  goes up, score tends to go up at a fairly steady rate.
- You want a model that's fast to train, cheap to run, and easy to
  explain — the slope tells you directly how much one extra hour of
  study is worth, on average.
- It's a strong **baseline**. Even if you plan to try fancier models
  later, fit a Linear Regression first so you have something to compare
  against.

------------------------------------------------------------------------

## Assumptions

Linear Regression works best — and its coefficients are only
trustworthy — when a few conditions roughly hold:

1. **Linearity** — the true relationship between the feature(s) and the
   target is approximately a straight line. (If it's clearly curved,
   see [`polynomial_regression.md`](./polynomial_regression.md).)
2. **Independence of errors** — one prediction's error doesn't leak
   into another's. This mostly matters for time-series/sequential data,
   where today's error being high often means tomorrow's will be too.
3. **Homoscedasticity** — the size of the errors stays roughly constant
   across the range of predictions, instead of growing or shrinking
   (e.g. the model isn't far more accurate for weak students than for
   strong ones).
4. **Low multicollinearity** — with multiple features, they shouldn't
   be strongly correlated with each other, or the coefficients become
   unstable and hard to interpret. (See
   [`ridge_lasso_regression.md`](./ridge_lasso_regression.md).)
5. **Normally distributed residuals** — the leftover errors
   (`actual - predicted`) roughly follow a bell curve centered at 0,
   rather than being skewed or clustered.

None of these need to hold perfectly — Linear Regression is fairly
robust in practice. But the more they're violated, the less you should
trust the model, and the metrics below are how you check.

------------------------------------------------------------------------

## Walking through the code

### 1. Load the data

```python
data = {"hours": [...], "score": [...]}
df = pd.DataFrame(data)
```

20 students, hand-recorded: hours studied and the score they got.

### 2. Separate features and target

```python
X = df[["hours"]]
y = df["score"]
```

### 3. Split the data

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
```

30% of students are held out as a test set the model never trains on —
that's how we check it generalizes, rather than just memorizing.

### 4. Train the model

```python
model = LinearRegression()
model.fit(X_train, y_train)
```

### 5. Inspect what the model learned

```python
model.coef_[0]      # slope  (m)
model.intercept_     # intercept (c)
```

For example, the model might learn something like:

```text
score = 5.86 * hours + 30.81
```

Interpretation: each extra hour of studying is associated with roughly
6 more points, and a student who studied 0 hours is predicted to score
around 31.

------------------------------------------------------------------------

## Evaluating a regression model

Classification uses accuracy; regression uses **error metrics**
instead, because "exactly right" almost never happens with continuous
numbers — what matters is *how far off* the predictions are.

### MAE (Mean Absolute Error)

```python
mae = mean_absolute_error(y_test, y_pred)
```

The average size of the error, in the same units as the target. If
`MAE = 1.45`, predictions are off by about 1.45 points on average.

### RMSE (Root Mean Squared Error)

```python
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
```

Squares each error before averaging, then square-roots the result back
into the target's units. This penalizes large mistakes more heavily
than MAE does — useful when big misses are especially costly.

### R² (coefficient of determination)

```python
r2 = r2_score(y_test, y_pred)
```

How much of the variation in the target the model explains, relative
to a baseline that always predicts the average score. `R² = 1` is a
perfect fit; `R² = 0` means the model is no better than guessing the
mean; it can go negative for a genuinely bad model.

**Do not read R² as an accuracy percentage.** A high R² does not mean
"80% of predictions are exactly right" — it means the model explains
80% of the variation in the data.

**Rule of thumb:** use MAE/RMSE to answer "how wrong are we, in real
units?", and R² to answer "how much of the pattern did the model
capture?" Check both — a model can have a decent R² but an MAE too
large to be useful, or vice versa.

------------------------------------------------------------------------

## Try it

```bash
python src/linear_regression_basics.py
```

Then see [`linear_regression_handson.md`](./linear_regression_handson.md)
for a guided exercise, and
[`house_price_prediction.md`](./house_price_prediction.md) for a full
multi-feature scenario.
