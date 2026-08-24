# XGBoost, LightGBM, CatBoost: Overview and When to Use

Code: [`xgboost_lightgbm_catboost.py`](./xgboost_lightgbm_catboost.py)

## What they have in common

All three are **gradient boosting** libraries — the same core idea as
`GradientBoostingClassifier` in
[`bagging_boosting_stacking.md`](./bagging_boosting_stacking.md): build
trees one at a time, each one correcting the ensemble's remaining
errors. What they add on top of scikit-learn's built-in version is
speed, more configuration knobs, and production-grade engineering —
which is why, on structured/tabular data (rows and columns, not images
or raw text), one of these three is usually the default choice in
industry rather than a plain `GradientBoostingClassifier`.

## The scenario

Same telecom-churn idea as `bagging_boosting_stacking.py`, but this
time with a **categorical** feature: `contract_type`
("month-to-month" / "one-year" / "two-year"). This is the detail that
most clearly shows how these three libraries differ in practice.

------------------------------------------------------------------------

## XGBoost

The library that made gradient boosting mainstream for competitive and
production ML. Strong regularization options (`reg_alpha`,
`reg_lambda`), handles missing values internally, and has the largest
ecosystem/community of the three — the most tutorials, the most
Stack Overflow answers, the most battle-testing.

```python
from xgboost import XGBClassifier
model = XGBClassifier(n_estimators=50, max_depth=3, eval_metric="logloss")
model.fit(X_train, y_train)  # X_train must be fully numeric
```

**When to use it:** your default first choice for tabular data,
especially if you want the most mature, most-documented option, or
need fine-grained regularization control.

------------------------------------------------------------------------

## LightGBM

Built by Microsoft with **speed on large datasets** as the priority.
The key structural difference: most gradient boosting libraries grow
trees **level-wise** (fill out every node at the current depth before
going deeper); LightGBM grows trees **leaf-wise** (always split
whichever leaf reduces error the most next, regardless of depth). This
tends to reach a good fit faster but requires modest tuning
(`min_child_samples`, `max_depth`) to avoid overfitting on small
datasets — which is why the script sets `min_child_samples=3` for this
tiny 24-row example, well below the default of 20.

```text
Level-wise (XGBoost default)     Leaf-wise (LightGBM default)
        ●                                 ●
      ╱   ╲                             ╱   ╲
     ●     ●                           ●     ●
    ╱ ╲   ╱ ╲                         ╱ ╲
   ●   ● ●   ●                       ●   ●
                                     ╱ ╲
   (every node at each depth       ●   ●
    gets split before going
    deeper)                       (keeps splitting whichever leaf
                                    helps most, so the tree can grow
                                    deep in one branch and shallow
                                    in another)
```

```python
from lightgbm import LGBMClassifier
model = LGBMClassifier(n_estimators=50, max_depth=3, min_child_samples=3)
model.fit(X_train, y_train)  # also needs fully numeric input
```

**When to use it:** large datasets where training speed matters, or
many features/high-cardinality categoricals (once properly encoded) —
LightGBM has built-in categorical support too via a `categorical_feature`
argument, though CatBoost's version requires less manual setup.

------------------------------------------------------------------------

## CatBoost

Built by Yandex with **categorical features** as the headline feature
(the name is short for "**Cat**egorical **Boost**ing"). Instead of
requiring you to one-hot or label-encode text columns yourself, you
tell CatBoost which columns are categorical and hand it the raw data:

```python
from catboost import CatBoostClassifier
model = CatBoostClassifier(iterations=50, depth=3, verbose=0)
model.fit(X_train, y_train, cat_features=["contract_type"])  # raw text column, no encoding
```

Internally, CatBoost uses a more principled statistical encoding
(ordered target statistics) rather than plain one-hot encoding, which
tends to handle high-cardinality categoricals (postal codes, product
IDs, ...) better than naive encoding would, and avoids one-hot
encoding's other headache: a categorical column with hundreds of
distinct values turning into hundreds of extra sparse columns.

**When to use it:** your data has meaningful categorical columns
(especially high-cardinality ones), you want strong results with less
manual preprocessing/tuning, or you're building a scikit-learn-style
pipeline where minimizing hand-written encoding logic is worth the
tradeoff.

------------------------------------------------------------------------

## Walking through the code

### 1-2. Data with a categorical column, features/target

24 customers, `contract_type` as plain text.

### 3. XGBoost and LightGBM — encode first

```python
X_encoded = pd.get_dummies(X, columns=["contract_type"])
```

`pd.get_dummies` turns the single `contract_type` column into three
binary columns (`contract_type_month-to-month`, `contract_type_one-year`,
`contract_type_two-year`) — this is a required step before either
library will accept the data, since both expect purely numeric input.

### 4. CatBoost — no encoding step

```python
cat_model.fit(Xc_train, y_train2, cat_features=["contract_type"])
```

Same original `X` (with the raw text column), just a `cat_features`
argument telling CatBoost which column to treat specially.

Running the script, all three land on the same test accuracy here —
with 24 rows, this tiny dataset can't meaningfully benchmark the three
libraries against each other. The real takeaway is the **workflow**
difference in the code itself, not the numbers.

------------------------------------------------------------------------

## Choosing between them

| | Best for | Categorical handling | Typical training speed |
| --- | --- | --- | --- |
| **XGBoost** | General-purpose default, strong regularization | Manual encoding required | Solid |
| **LightGBM** | Very large datasets, many features | Manual (or `categorical_feature=`) | Fastest |
| **CatBoost** | Meaningful/high-cardinality categoricals, less manual prep | Native, minimal setup | Slower to train, competitive to use |

In practice, many teams try more than one and let cross-validation
decide — see
[`hyperparameter_tuning.md`](./hyperparameter_tuning.md) for how to
search each one's hyperparameters properly, and
[`xgboost_handson.md`](./xgboost_handson.md) for a full worked example
with XGBoost specifically.

------------------------------------------------------------------------

## Try it

```bash
python src/ensemble_method/xgboost_lightgbm_catboost.py
```

Then try:

- Pass `X` (the raw, unencoded DataFrame) straight into `XGBClassifier.fit()`
  without calling `pd.get_dummies` first — what error do you get, and
  what does it tell you about what XGBoost expects?
- Add a second categorical column (e.g. a made-up `region` column) and
  update the CatBoost `cat_features` list — how much code has to
  change, compared to what you'd need to change for the one-hot-encoded
  XGBoost/LightGBM path?
