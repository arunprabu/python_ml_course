# Ridge and Lasso Regression (Regularization)

Code: [`ridge_lasso_regression.py`](./ridge_lasso_regression.py)

## The scenario

An HR team exports a spreadsheet of employee records to predict monthly
salary. The export includes:

| Column                 | Meaning                                    |
| ----------------------- | ------------------------------------------ |
| `years_experience`      | Genuinely related to salary                |
| `certifications`        | Genuinely related to salary                |
| `birth_month`           | Included in the export, unrelated to salary |
| `favorite_color_code`   | A code from an old HR survey, unrelated to salary |
| `monthly_salary_k`      | Actual salary in ₹ thousand — our **target** |

This is a very common real-world situation: a dataset export includes
every column that happened to be collected, whether or not it has
anything to do with the target. Plain Linear Regression has no way to
know that `birth_month` and `favorite_color_code` are irrelevant — it
will still assign them some nonzero coefficient if doing so reduces
training error even slightly.

------------------------------------------------------------------------

## The problem: overfitting to irrelevant/unstable features

Plain Linear Regression fits the training data as closely as possible,
with no penalty for how large the coefficients get. That causes
trouble when:

- some features are **irrelevant** — pure noise with respect to the
  target, like `birth_month` here;
- features are **correlated with each other** (multicollinearity) —
  the model can't tell which one "deserves credit," so it may assign
  large, unstable coefficients that would swing a lot if the data
  changed slightly.

Both symptoms are a sign the model has **overfit**: it looks fine on
training data but generalizes worse than it should.

------------------------------------------------------------------------

## The idea: penalize large coefficients

Ridge and Lasso are Linear Regression with an extra term added to what
the model minimizes — a penalty based on the size of the coefficients,
controlled by a hyperparameter `alpha` (bigger `alpha` = stronger
regularization = smaller coefficients):

| Model | Penalty | Effect |
| --- | --- | --- |
| **Ridge** (`Ridge`) | L2: sum of squared coefficients | Shrinks all coefficients toward 0, smoothly. Rarely drives one to *exactly* 0. |
| **Lasso** (`Lasso`) | L1: sum of absolute coefficients | Can shrink coefficients all the way to **exactly 0** — effectively removing that feature from the model. |

```python
from sklearn.linear_model import Ridge, Lasso

ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=1.0)
```

------------------------------------------------------------------------

## Walking through the code

### 1-3. Data, features/target, train/test split

Same pattern as the other examples — 20 employee records, `X` holds
all four columns, `y` is `monthly_salary_k`, with 25% held out for
testing.

### 4. Train three models on the exact same data

```python
models = {
    "Linear Regression": LinearRegression(),
    "Ridge (alpha=1.0)": Ridge(alpha=1.0),
    "Lasso (alpha=1.0)": Lasso(alpha=1.0),
}
```

### 5. Compare the coefficients

Running the script prints a table like:

```text
                      r2  years_experience  certifications  birth_month  favorite_color_code
model
Linear Regression  0.970              3.17            3.43         0.10                 0.42
Ridge (alpha=1.0)  0.968              3.30            3.10         0.10                 0.41
Lasso (alpha=1.0)  0.967              3.92            1.71         0.03                 0.00
```

Read across the columns for `birth_month` and `favorite_color_code`:

- **Linear Regression** still assigns both a small but nonzero weight
  — it has no reason not to.
- **Ridge** shrinks them only slightly.
- **Lasso** drives `favorite_color_code` to **exactly 0** and
  `birth_month` very close to 0 — it has effectively removed the
  irrelevant columns from the model, while `years_experience` and
  `certifications` stay clearly nonzero.

All three models score almost the same R² on the test set — the point
isn't that regularization makes the model "more accurate" here, it's
that Lasso tells you *which features actually matter*, which plain
Linear Regression can't.

------------------------------------------------------------------------

## When to use which

- **Ridge** — you believe most/all features are at least somewhat
  useful, and you mainly want to tame multicollinearity and reduce
  overfitting without removing any feature outright.
- **Lasso** — you have several features and suspect some are
  irrelevant; you want the model itself to pick a smaller, more
  interpretable subset.
- **Elastic Net** (`ElasticNet`, not shown here) — a blend of both,
  useful when you want some feature selection *and* better stability
  with correlated features.
- **Plain Linear Regression** — still fine when you have few features,
  they're not strongly correlated, and you're not seeing signs of
  overfitting.

------------------------------------------------------------------------

## Picking `alpha`

`alpha=0` is identical to plain Linear Regression; larger values
regularize more aggressively. Too large, and even genuinely useful
features get shrunk too much, hurting accuracy (underfitting). In
practice, `alpha` is tuned with cross-validation (`RidgeCV`, `LassoCV`)
rather than guessed, and the right value also depends heavily on the
scale of your features and target.

------------------------------------------------------------------------

## Try it

```bash
python src/ridge_lasso_regression.py
```

Then try:

- Raising Lasso's `alpha` from `1.0` to `3.0` or `5.0` — at what point
  does it start zeroing out `certifications` too, and what happens to
  the test R² when it does?
- Raising Ridge's `alpha` the same way — does it ever drive a
  coefficient to *exactly* 0?
