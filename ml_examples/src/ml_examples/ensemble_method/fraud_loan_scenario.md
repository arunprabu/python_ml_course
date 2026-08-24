# Scenario: Fraud Detection and Loan Default Prediction

Code: [`fraud_loan_scenario.py`](./fraud_loan_scenario.py)

## The scenario

Two of the most common real-world uses of gradient boosting share the
same underlying shape: predict a **rare, costly event** — a fraudulent
transaction, a defaulted loan — from structured application/transaction
data. They also share the same trap: **class imbalance**. Most
transactions aren't fraud. Most loans get repaid. A model (or a lazy
baseline) can post a very high *accuracy* by predicting "no" every
time, while catching zero of the cases that actually matter.

This file works through fraud detection in full (Part A), then applies
the exact same playbook to loan default prediction (Part B) — same
techniques, different domain, to show how transferable the approach
is.

------------------------------------------------------------------------

## Part A — Fraud Detection

### The data

48 transactions: `amount`, `hour` (0-23), `distance_from_home_km`,
`tx_last_hour` (how many transactions this card made in the last
hour), `is_foreign`, and the target `is_fraud`. 8 of the 48 (16.7%) are
fraudulent — designed to look like real fraud patterns: unusual hours,
large distances from home, a burst of transactions in a short window,
foreign transactions, and — deliberately — one *tiny* fraudulent
transaction (₹15) mixed in with big ones, mimicking real "card
testing" fraud, where criminals first run a small charge to check a
stolen card still works before attempting a large one. That row exists
specifically so the model can't get away with just checking "is the
amount large."

### The accuracy trap

```python
baseline_predictions = pd.Series(0, index=y_test.index)  # always predict "not fraud"
accuracy_score(y_test, baseline_predictions)   # 0.80  (80%!)
recall_score(y_test, baseline_predictions)     # 0.00  (catches NO fraud)
```

A model that never flags anything still scores 80% accuracy, because
80% of the test transactions genuinely aren't fraud. This is precisely
why accuracy is the wrong metric to optimize (or even report) for an
imbalanced problem like this — a stakeholder skimming an "80% accurate"
headline number would have no idea the model is doing nothing at all.

### Handling the imbalance: `scale_pos_weight`

```python
scale_pos_weight = (y_train == 0).sum() / (y_train == 1).sum()  # 5.6 here

fraud_model = XGBClassifier(
    n_estimators=100, max_depth=3, scale_pos_weight=scale_pos_weight,
    eval_metric="logloss", random_state=42,
)
```

`scale_pos_weight` tells XGBoost to treat a missed fraud case (a false
negative) as roughly `scale_pos_weight` times more costly than a false
alarm on a legitimate transaction, during training — pushing the model
to pay real attention to the minority class instead of optimizing
overall accuracy, which the majority class would otherwise dominate. A
common starting point, used here, is the ratio of majority-to-minority
class counts in the training data.

### Evaluating with the right metrics

```python
precision_score(y_test, fraud_preds)   # of flagged transactions, how many were real fraud
recall_score(y_test, fraud_preds)      # of actual fraud, how much did we catch
f1_score(y_test, fraud_preds)          # balance of the two
confusion_matrix(y_test, fraud_preds)  # [[TN FP] [FN TP]]
```

Running the script, the tuned model reaches precision, recall, and F1
all at `1.00` on this small test set — it caught every fraud case with
no false alarms, including the small "card testing" transaction. In a
real system you'd track **both** precision and recall going forward,
because they trade off against each other: a model tuned to catch more
fraud (higher recall) usually also flags more legitimate transactions
by mistake (lower precision) — the right balance depends on the
business cost of each kind of mistake (annoying a real customer with a
false decline, vs. letting a fraudulent charge through).

------------------------------------------------------------------------

## Part B — Loan Default Prediction

### Same playbook, different domain

```python
loan_scale_pos_weight = (yl_train == 0).sum() / (yl_train == 1).sum()

loan_model = XGBClassifier(
    n_estimators=100, max_depth=3, scale_pos_weight=loan_scale_pos_weight,
    eval_metric="logloss", random_state=42,
)
```

20 loan applications: `credit_score`, `annual_income_k`,
`debt_to_income`, `past_defaults`, `loan_amount_k`, and the target
`defaulted` (25% default rate). Nothing about the *approach* changes
from Part A — imbalanced binary target, `scale_pos_weight` to
compensate, evaluate with precision/recall instead of accuracy. Only
the features and the story behind them are different.

### Feature importance

```python
print(loan_model.feature_importances_)
```

```text
credit_score       1.000
annual_income_k    0.000
debt_to_income     0.000
past_defaults      0.000
loan_amount_k      0.000
```

In this dataset, `credit_score` alone almost perfectly separates
defaulters from non-defaulters (by design, to keep the example small
and clear), so the model leans on it entirely and ignores the rest. A
real loan-default dataset would spread importance across several
correlated signals — but the *mechanism* for reading which features a
gradient boosting model actually relies on is exactly this one line,
regardless of dataset size.

------------------------------------------------------------------------

## Things to watch for in real fraud/default systems

- **The imbalance is usually far more extreme than this example.** Real
  fraud rates are often well under 1%, not 16.7% — techniques like
  `scale_pos_weight`, oversampling the minority class (e.g. SMOTE), or
  anomaly-detection approaches (see `IsolationForest` in the ML
  cheatsheet) become more important as the imbalance grows.
- **Precision/recall tradeoffs are business decisions, not just model
  decisions.** Decide what a false positive costs (a declined
  legitimate purchase, an unfairly rejected loan) vs. a false negative
  (fraud that slips through, a bad loan that gets approved) *before*
  picking a decision threshold.
- **Labels lag reality.** A "not fraud" label often just means "not yet
  disputed" — fraud sometimes gets reported weeks later, which can
  quietly mislabel recent data. Loan defaults have a similar delay:
  you don't know a loan will default until it actually does, months or
  years in.

------------------------------------------------------------------------

## Try it

```bash
python src/ensemble_method/fraud_loan_scenario.py
```

Then try:

- Remove `scale_pos_weight` from the fraud model (or set it to `1`) and
  re-run. On this dataset, recall actually holds at `1.00` even
  without it — the fraud pattern here is deliberately clean and easy to
  separate. `scale_pos_weight` earns its keep on messier, more
  realistic data where the classes overlap more; try shrinking the
  gap between legitimate and fraudulent feature values by hand (e.g.
  make a few fraud rows less extreme) and re-compare recall with and
  without it.
- In Part B, drop `credit_score` from `X_loan` entirely and re-run —
  which feature does `feature_importances_` lean on next?
