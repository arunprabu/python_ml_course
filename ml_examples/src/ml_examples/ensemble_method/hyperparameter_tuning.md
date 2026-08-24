# Hyperparameter Tuning: GridSearchCV vs RandomizedSearchCV

Code: [`hyperparameter_tuning.py`](./hyperparameter_tuning.py)

## The scenario

Every model so far picked hyperparameters by hand —
`n_estimators=50`, `max_depth=3`, and so on. Those choices matter: too
shallow and the model underfits, too deep and it memorizes the
training set (exactly what happened to the single tree in
[`bagging_boosting_stacking.md`](./bagging_boosting_stacking.md)).
**Hyperparameter tuning** automates the search for a good combination,
using cross-validation to score each candidate instead of eyeballing
train/test numbers by hand.

We reuse the same churn dataset and tune a `RandomForestClassifier`'s
settings instead of guessing them.

------------------------------------------------------------------------

## Why not just try every value you can think of, by hand?

You could — but the number of *combinations* grows multiplicatively.
This example searches over:

```python
param_grid = {
    "n_estimators": [50, 100, 150],
    "max_depth": [2, 4, 6],
    "min_samples_leaf": [1, 2, 4],
}
```

Three hyperparameters, three values each = `3 × 3 × 3 = 27`
combinations. Add a fourth hyperparameter with 3 values and it jumps to
81. Trying that many combinations by hand, and remembering which was
best, isn't realistic — this is exactly the kind of repetitive search
a computer should do.

------------------------------------------------------------------------

## GridSearchCV — try everything

```python
grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=3,
    scoring="accuracy",
)
grid_search.fit(X_train, y_train)
```

`GridSearchCV` trains a model for **every single combination** in the
grid, and for each one, runs **3-fold cross-validation** (`cv=3`):
split the training data into 3 parts, train on 2, validate on the
third, rotate, and average the 3 scores. That's `27 combinations × 3
folds = 81` models trained for this one call.

Cross-validation matters here specifically because we're using the
result to *choose* a hyperparameter — if we just checked each
candidate once against a single validation split, we could easily pick
whichever candidate got lucky on that one split, not the one that's
actually best on average.

Running the script:

```text
Best params: {'max_depth': 2, 'min_samples_leaf': 4, 'n_estimators': 50}
Best CV accuracy: 0.752
Test accuracy: 1.000
```

Guaranteed to find the best combination **within the grid you
specified** — but only within it. If the real best `max_depth` were
`3`, this grid would never find it, because `3` isn't one of the
values offered.

------------------------------------------------------------------------

## RandomizedSearchCV — try a fixed number of random combinations

```python
random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    n_iter=8,
    cv=3,
    scoring="accuracy",
    random_state=42,
)
```

Instead of trying all 27 combinations, `n_iter=8` samples just 8 of
them at random (each still evaluated with 3-fold CV — `8 × 3 = 24`
models trained, a third of GridSearchCV's work here). Running the
script:

```text
Best params: {'n_estimators': 100, 'min_samples_leaf': 4, 'max_depth': 4}
Best CV accuracy: 0.752
Test accuracy: 1.000
```

It found a **different** combination of parameters than GridSearchCV,
yet matched its cross-validated score exactly, for less than a third
of the training work. That's the appeal: `RandomizedSearchCV` doesn't
guarantee finding the single best combination, but in practice it
often finds something comparably good for a fraction of the compute —
and unlike `GridSearchCV`, you control the search cost directly with
`n_iter`, independent of how many hyperparameters or values you want to
consider.

------------------------------------------------------------------------

## When to use which

- **GridSearchCV** — small search spaces (as here — 27 combinations is
  cheap), or when you need the guarantee of finding the actual best
  combination within your grid, e.g. for a final, careful tuning pass.
- **RandomizedSearchCV** — large search spaces (many hyperparameters,
  or continuous ranges instead of a short list of values), where
  exhaustive search would take too long. Also useful early in a
  project, to quickly get a sense of which hyperparameters matter
  before narrowing down a smaller grid for `GridSearchCV` to finish
  off.
- Both work the same way with any scikit-learn-compatible model —
  including `XGBClassifier`, `LGBMClassifier`, and `CatBoostClassifier`
  (see [`xgboost_handson.md`](./xgboost_handson.md) for
  `RandomizedSearchCV` used directly on an XGBoost model).

------------------------------------------------------------------------

## Try it

```bash
python src/ensemble_method/hyperparameter_tuning.py
```

Then try:

- Add a fourth hyperparameter to `param_grid`, e.g.
  `"max_features": ["sqrt", "log2"]`. How many total combinations does
  that create for `GridSearchCV`? Does `RandomizedSearchCV` with the
  same `n_iter=8` still find a comparably good result?
- Lower `RandomizedSearchCV`'s `n_iter` to `3` — does it still find a
  combination as good as `GridSearchCV`'s, or does search quality start
  to drop off?
