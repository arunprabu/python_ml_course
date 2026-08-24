# Hands-on: Train an XGBoost Model and Tune Hyperparameters

Code: [`xgboost_handson.py`](./xgboost_handson.py)

## The scenario

Same telecom-churn problem as
[`bagging_boosting_stacking.py`](./bagging_boosting_stacking.py) and
[`hyperparameter_tuning.py`](./hyperparameter_tuning.py) — this file is
where those two topics come together end to end: train a baseline
XGBoost model, tune it properly with `RandomizedSearchCV`, evaluate the
tuned model correctly, and use it to make a real prediction.

------------------------------------------------------------------------

## Steps (already implemented in the script)

### STEP 1-3 — Load data, choose features/target, split

Same 40-customer churn dataset used throughout this folder:
`tenure_months`, `monthly_charges`, `support_tickets` → `churned`.

### STEP 4 — Train a baseline XGBoost model

```python
baseline_model = XGBClassifier(n_estimators=100, max_depth=3, eval_metric="logloss", random_state=42)
baseline_model.fit(X_train, y_train)
```

```text
Baseline XGBoost — train: 0.929, test: 0.917
```

A reasonable starting point, picked by hand rather than tuned. Note
the small train/test gap already — a sign this baseline isn't wildly
overfit, but there's still room to see if better settings exist.

### STEP 5 — Define the search space

```python
param_dist = {
    "n_estimators": [50, 100, 150, 200],
    "max_depth": [2, 3, 4, 5],
    "learning_rate": [0.01, 0.05, 0.1, 0.2],
    "subsample": [0.7, 0.8, 0.9, 1.0],
}
```

Four hyperparameters, four values each = 256 possible combinations —
big enough that `GridSearchCV` would mean training 256×3 = 768 models
just for a 3-fold search. This is exactly the situation
[`hyperparameter_tuning.md`](./hyperparameter_tuning.md) described as
`RandomizedSearchCV`'s home turf.

What each one controls:

- **`n_estimators`** — how many boosting rounds (trees) to build.
- **`max_depth`** — how deep each tree can grow. Deeper trees fit more
  complex patterns, but overfit faster.
- **`learning_rate`** — how much each new tree is allowed to correct
  the ensemble. Lower values need more rounds but often generalize
  better ("learn slowly and carefully" vs. "learn fast and sloppily").
- **`subsample`** — the fraction of training rows each tree sees.
  Below `1.0` adds randomness (similar in spirit to bagging), which
  fights overfitting.

### STEP 6 — Search with RandomizedSearchCV

```python
search = RandomizedSearchCV(
    XGBClassifier(eval_metric="logloss", random_state=42),
    param_dist, n_iter=12, cv=3, scoring="accuracy", random_state=42,
)
search.fit(X_train, y_train)
```

Tries 12 of the 256 combinations (each scored with 3-fold
cross-validation). Running the script:

```text
Best params found: {'subsample': 0.9, 'n_estimators': 100, 'max_depth': 2, 'learning_rate': 0.01}
Best cross-validated accuracy: 0.678
```

Notice the cross-validated score (0.678) is *lower* than the
baseline's raw test accuracy (0.917) — that's expected, not a bug.
Cross-validation scores tend to look more conservative/realistic than
a single train/test split, especially on a small dataset like this
one, because it's averaging performance across several different
validation slices instead of reporting the one split that happened to
go well.

### STEP 7 — Evaluate the tuned model properly

```python
print(classification_report(y_test, tuned_model.predict(X_test)))
```

```text
Tuned XGBoost — train: 0.857, test: 0.917
```

The tuned model's **test** accuracy matches the baseline (0.917), but
its **train** accuracy is noticeably lower (0.857 vs. 0.929) — the
search landed on a shallower tree (`max_depth=2`) with a slow
`learning_rate=0.01`, which fits the training data less tightly. On
this tiny dataset the test score doesn't move, but the tuned model is
the more conservative, less overfit choice — the same pattern as
stacking beating the single tree on train/test balance in
`bagging_boosting_stacking.py`, not raw accuracy. `classification_report`
gives you precision/recall/F1 per class in one call, useful any time
you want more than a single accuracy number (see
[`fraud_loan_scenario.md`](./fraud_loan_scenario.md) for why that
matters even more on imbalanced data).

### STEP 8 — Predict for a new customer

```python
new_customer = pd.DataFrame({"tenure_months": [6], "monthly_charges": [95], "support_tickets": [5]})
tuned_model.predict_proba(new_customer)
```

```text
Predicted: CHURN
Churn probability: 72.5%
```

A short-tenure, high-charge, high-ticket-count customer — exactly the
profile the training data associates with churn.

------------------------------------------------------------------------

## The complete workflow

```text
DATA
 ↓
FEATURES + TARGET
 ↓
TRAIN / TEST SPLIT
 ↓
BASELINE MODEL (sensible defaults)
 ↓
DEFINE SEARCH SPACE
 ↓
RandomizedSearchCV (cross-validated search)
 ↓
EVALUATE TUNED MODEL (test set + classification_report)
 ↓
PREDICT NEW DATA
```

This is the same shape as
[`linear_regression_handson.md`](../supervised-learning/linear_regression_handson.md)
in the supervised-learning folder, with one addition in the middle:
tuning. For any model with hyperparameters (which is most of them),
"train once with defaults" is a reasonable first draft, but "search for
better settings with cross-validation" is the step that turns a
draft into something you'd actually ship.

Run it:

```bash
python src/ensemble_method/xgboost_handson.py
```

------------------------------------------------------------------------

## Exercises — try these by editing the script

1. **Compare overfitting, not just accuracy.** `baseline_train_acc` is
   0.929 vs. `tuned_train_acc` at 0.857, while both score 0.917 on
   test. Which model would you trust more on a *different* batch of
   new customers, and why?
2. **Add early stopping.** Pass `early_stopping_rounds=10` to
   `XGBClassifier` and an `eval_set=[(X_test, y_test)]` to `.fit()` —
   then print `model.best_iteration`. Does training stop before
   reaching the requested `n_estimators`? (It does — around round 47
   out of 200 in one run — because XGBoost detects the validation
   score has stopped improving and halts early rather than continuing
   to overfit.)
3. **Inspect feature importance.** Print
   `tuned_model.feature_importances_` alongside `X.columns` — which
   feature does the model rely on most to predict churn? Does that
   match your intuition from looking at the raw data?
4. **Switch the scorer.** Change `scoring="accuracy"` to
   `scoring="f1"` in the `RandomizedSearchCV` call — does the search
   land on the same best parameters, or different ones?

------------------------------------------------------------------------

## What "good" tuning looks like here

On a dataset this small (40 rows), don't expect tuning to produce a
dramatic accuracy jump — there's only so much a search can discover
from so little data, and test-set accuracy moves in coarse steps
(1/12 ≈ 8.3% per row). Judge success less by "did the test number go
up" and more by: did the search find a model with a **smaller
train/test gap** (less overfitting), and does the **cross-validated**
score (not a single lucky test split) look reasonable? On a real,
larger dataset, this same workflow typically does show clearer
accuracy gains from tuning — the mechanics here transfer directly, the
scale of improvement is what mostly changes.
