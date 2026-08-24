# Bagging vs Boosting vs Stacking

Code: [`bagging_boosting_stacking.py`](./bagging_boosting_stacking.py)

## The scenario

A telecom company wants to predict which customers are about to cancel
their subscription (`churned`), from tenure, monthly charges, and how
many support tickets they've filed. A single Decision Tree tends to
memorize the quirks of whatever training rows it sees — it can hit
100% accuracy on training data while doing noticeably worse on new
customers. **Ensemble methods** fix this by combining several models
instead of relying on one.

All three techniques here train multiple models and combine their
predictions — the difference is entirely in **how**.

------------------------------------------------------------------------

## Bagging (Bootstrap AGGregatING)

Train many copies of the **same** algorithm, each on a different
random sample of the training data (drawn *with replacement* — some
rows appear more than once, some not at all, in each sample). Every
model trains **independently** — none of them ever see each other's
predictions or mistakes. To predict, take a majority vote (or average)
across all of them.

```text
Training data
     │
     ├──► random sample 1 ──► Tree 1 ──┐
     ├──► random sample 2 ──► Tree 2 ──┤
     ├──► random sample 3 ──► Tree 3 ──┼──► majority vote ──► prediction
     │         ...                     │
     └──► random sample N ──► Tree N ──┘
```

Each individual tree, trained on a slightly different slice of data,
makes somewhat different mistakes. Averaging over many such trees
cancels a lot of that noise out — this is what reduces overfitting.
**Random Forest** is bagging applied specifically to decision trees,
with one extra trick: each tree also only considers a random *subset
of features* at each split, decorrelating the trees even further.

------------------------------------------------------------------------

## Boosting

Train models **one at a time, in sequence**. Each new model is built
specifically to correct the mistakes of the ensemble so far:

- **AdaBoost** — after each round, misclassified rows get a higher
  weight, so the next model is forced to pay more attention to them.
- **Gradient Boosting** — each new model is trained to predict the
  *residual error* (how wrong the current ensemble still is), and gets
  added on top.

```text
Tree 1 ──► predictions, some wrong
   │
   ▼ (focus harder on what Tree 1 got wrong)
Tree 2 ──► corrects some of Tree 1's mistakes
   │
   ▼ (focus harder on what's still wrong)
Tree 3 ──► corrects more mistakes
   │
   ▼
  ...
   │
   ▼
final prediction = weighted sum of all trees
```

Unlike bagging, boosting's models are **not independent** — each one
only makes sense in the context of what came before it, so boosting
can't be parallelized across trees the way bagging can. In exchange,
boosting often reaches a more accurate model with fewer trees, because
every new tree is targeted at whatever is still being gotten wrong.

------------------------------------------------------------------------

## Stacking

Train several **different** algorithms (not necessarily trees at all —
could mix a tree, a linear model, an SVM, ...), then train a small
**meta-model** on top whose only job is to learn how to best combine
their predictions.

```text
                ┌──► Model A (e.g. Decision Tree) ──► prediction A ──┐
Training data ──┼──► Model B (e.g. Bagged Trees)  ──► prediction B ──┼──► meta-model ──► final prediction
                └──► Model C (e.g. ...)            ──► prediction C ──┘
```

This is more flexible than a simple vote — the meta-model can learn
things like "trust Model A more when the input looks like *this*, but
lean on Model B when it looks like *that*." The tradeoff is more
moving parts, more compute, and more risk of overfitting the
meta-model if you're not careful with cross-validation (which
scikit-learn's `StackingClassifier` handles internally).

------------------------------------------------------------------------

## Walking through the code

### 1-3. Data, features/target, train/test split

40 customers, 3 numeric features, a `churned` label with a deliberately
noisy pattern (a few customers break the "obvious" rule, same as real
data would).

### 4. Baseline: a single Decision Tree

```python
tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train, y_train)
```

Running the script:

```text
Single Decision Tree — train: 1.000, test: 0.917
```

Perfect training accuracy is the tell: with no depth limit, the tree
keeps splitting until every training row is classified correctly —
including the noisy exceptions, which it has no way to distinguish
from real patterns. That's overfitting.

### 5. Bagging

```python
bagging = BaggingClassifier(estimator=DecisionTreeClassifier(), n_estimators=50, random_state=42)
```

```text
Bagging (50 trees) — train: 1.000, test: 1.000
```

Each of the 50 trees still overfits its own bootstrap sample, but they
overfit to *different* noise. Averaging their votes cancels much of
that out — the ensemble's test accuracy reaches 1.000 here, closing
the gap the single tree left open.

### 6. Boosting

```python
adaboost = AdaBoostClassifier(n_estimators=50, random_state=42)
gradient_boost = GradientBoostingClassifier(n_estimators=50, random_state=42)
```

```text
AdaBoost (50 rounds)   — train: 1.000, test: 0.917
Gradient Boosting (50) — train: 1.000, test: 0.917
```

Both match the single tree's test score on this run rather than
beating it outright — with only 40 rows, there's a limit to how much
signal any method can extract. The real-world case for boosting is
usually made on larger datasets, where its sequential error-correction
consistently pulls ahead of both a single tree and bagging.

### 7. Stacking

```python
stacking = StackingClassifier(
    estimators=[("tree", DecisionTreeClassifier(max_depth=3, random_state=42)),
                ("bagged_trees", BaggingClassifier(n_estimators=20, random_state=42))],
    final_estimator=LogisticRegression(),
)
```

```text
Stacking (tree + bagging) — train: 0.964, test: 1.000
```

The most interesting row: stacking's **train** accuracy is *lower*
than the single tree's (0.964 vs. 1.000), yet its **test** accuracy is
higher (1.000 vs. 0.917). It fit the training data slightly less
tightly and generalized better as a result — a small, concrete example
of why "100% training accuracy" is a warning sign, not a goal.

------------------------------------------------------------------------

## When to use which

- **Bagging / Random Forest** — your base model (often a tree)
  overfits, and you want variance reduction with minimal tuning.
  Trains fast because every model is independent and can run in
  parallel.
- **Boosting** (Gradient Boosting, XGBoost, LightGBM, CatBoost — see
  [`xgboost_lightgbm_catboost.md`](./xgboost_lightgbm_catboost.md)) —
  you want the best possible accuracy on structured/tabular data and
  are willing to tune more carefully; it's the default choice for most
  competitive/production tabular ML today.
- **Stacking** — you already have several genuinely different models
  (maybe from different teams, or different algorithm families) and
  want to combine their strengths rather than pick just one winner.
  Most valuable when the base models make *different kinds* of
  mistakes — combining several near-identical models gains little.

------------------------------------------------------------------------

## Try it

```bash
python src/ensemble_method/bagging_boosting_stacking.py
```

Then try:

- Limit the single tree with `max_depth=3` — does its test accuracy
  improve, and does it stop hitting 100% on the training set?
- Increase `n_estimators` for AdaBoost and Gradient Boosting to 200 —
  does test accuracy change on this dataset, or does it plateau?
