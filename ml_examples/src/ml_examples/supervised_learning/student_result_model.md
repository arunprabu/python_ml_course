# Logistic Regression: Predicting Pass/Fail

Code: [`student_result_model.py`](./student_result_model.py)

## The scenario

A teacher has a record of how many hours each student studied, and
whether they passed or failed the exam. They want a model that looks
at a new student's study hours and predicts which group they're likely
to fall into — **Pass** or **Fail** — so at-risk students can be
flagged early.

This is the classification counterpart to
[`linear_regression_basics.py`](./linear_regression_basics.py), which
uses the exact same `hours` values to predict the actual exam **score**
instead. Comparing the two side by side is the easiest way to feel the
difference between regression and classification:

```text
Linear Regression    -> predicts a number       (score: 0-100)
Logistic Regression   -> predicts a class/prob    (pass / fail)
```

------------------------------------------------------------------------

## Why not just use Linear Regression here?

The target, `passed`, only ever takes two values: `0` (fail) or `1`
(pass). A straight line from Linear Regression would happily predict
`1.4` or `-0.2` for some students — numbers that don't correspond to
any real class. Logistic Regression fixes this by squashing its output
through the **sigmoid function**, which maps any number onto a
probability between 0 and 1:

```text
              ┌───────────────────────┐
hours ───────►│  m*hours + c           │──► sigmoid ──► probability (0-1)
              └───────────────────────┘                     │
                                                              ▼
                                                    ≥ 0.5 → predict Pass (1)
                                                    < 0.5 → predict Fail (0)
```

```text
probability
   1 ┤                              ●●●●●●●
     │                         ●●●●●
     │                     ●●●●
 0.5 ┤ - - - - - - - - -●●- - - - - - - - -
     │              ●●●●
     │        ●●●●●●
   0 ┤●●●●●●●●
     └──────────────────────────────────── hours
```

That S-shaped curve is why it's called *logistic* regression, even
though — confusingly — it's a **classification** algorithm, not a
regression one.

------------------------------------------------------------------------

## When to use Logistic Regression

- The **target is a category with two outcomes** (pass/fail, yes/no,
  spam/not spam). For more than two classes, scikit-learn's
  `LogisticRegression` still works — it handles multi-class problems
  under the hood.
- You want a **probability**, not just a label — `model.predict_proba()`
  gives you "70% likely to pass" rather than just "Pass," which is
  often more useful for ranking or setting your own risk threshold.
- You expect the *log-odds* of the outcome to move roughly linearly
  with the feature(s) — in practice, this just means: as hours studied
  increases, the chance of passing should increase steadily, without
  any sudden jumps or reversals.
- Like Linear Regression, it's fast, cheap, and interpretable — a good
  baseline before reaching for a more complex classifier (Decision
  Tree, Random Forest, etc.).

------------------------------------------------------------------------

## Walking through the code

### 1. Load the data

```python
df = pd.DataFrame(
    {
        "hours": [1, 1.5, 2, ..., 10, 10.5],
        "passed": [0, 0, 0, ..., 1, 1],
    }
)
```

20 students: hours studied, and `1` if they passed, `0` if they
failed. Below roughly 5-5.5 hours, students tend to fail; above that,
they tend to pass.

### 2. Separate features and target

```python
X = df[["hours"]]   # features, must be 2D
y = df["passed"]     # target, 1D
```

### 3. Split into train and test sets

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=56, stratify=y
)
```

30% of students are held out to test the model on data it never
trained on. `stratify=y` keeps the Pass/Fail ratio the same in both
the train and test groups — without it, an unlucky split could put
almost all the "fail" students in one group by chance, especially with
a small dataset like this one.

### 4. Train the model

```python
model = LogisticRegression()
model.fit(X_train, y_train)
```

Instead of learning a slope and intercept for a straight line (like
Linear Regression), Logistic Regression learns the slope and intercept
of the line *inside* the sigmoid — the values that best separate
"pass" from "fail" once squashed into a probability.

### 5. Evaluate

```python
model.score(X_test, y_test)
```

For a classifier, `.score()` returns **accuracy**: the fraction of
test students the model classified correctly. On this dataset it
scores `1.0` — every held-out student was classified correctly, which
makes sense given how cleanly this small, hand-picked dataset separates
around 5-5.5 hours.

### 6. Predict for new students

```python
new_student = pd.DataFrame({"hours": [5.9]})
model.predict(new_student)[0]   # 1 (pass)

lazy_student = pd.DataFrame({"hours": [2.0]})
model.predict(lazy_student)[0]  # 0 (fail)
```

------------------------------------------------------------------------

## Beyond accuracy

Accuracy is easy to read but can be misleading — especially when the
two classes aren't evenly balanced (imagine 95 fails and 5 passes: a
model that always predicts "fail" gets 95% accuracy while being
useless). Other tools worth knowing:

- **`model.predict_proba(X)`** — returns the actual probability for
  each class, not just the final label. Useful when you want to set
  your own decision threshold instead of the default 0.5 (e.g. flag
  anyone below 70% chance of passing, not just those predicted to
  fail).
- **Confusion matrix** (`sklearn.metrics.confusion_matrix`) — breaks
  accuracy down into correct/incorrect predictions *per class*, so you
  can see whether the model's mistakes are false passes or false
  fails.
- **Precision / Recall / F1** (`sklearn.metrics.classification_report`)
  — precision asks "of the students predicted to pass, how many
  actually did?"; recall asks "of the students who actually passed, how
  many did the model catch?" These matter more than raw accuracy when
  one kind of mistake (e.g. missing an at-risk student) is costlier
  than the other.

------------------------------------------------------------------------

## Things to watch for

- **Small dataset, clean separation.** With only 20 hand-picked
  students and a clear cutoff around 5-5.5 hours, `1.0` accuracy is
  expected here — it isn't evidence the model would perform this well
  on messier, real classroom data with more overlap between the two
  groups.
- **One feature only.** Real "at risk" prediction would likely include
  more signals (attendance, past grades, assignment completion) —
  Logistic Regression handles multiple features exactly like Linear
  Regression does, just add more columns to `X`.
- **Extrapolation.** The training data only covers roughly 1-10.5
  hours. Predicting for 0 hours or 20 hours asks the model to
  extrapolate outside what it has seen, the same caution that applies
  to Linear Regression.

------------------------------------------------------------------------

## The complete workflow

```text
DATA
 ↓
FEATURES + TARGET
 ↓
TRAIN / TEST SPLIT (stratified)
 ↓
MODEL (LogisticRegression)
 ↓
LEARN PARAMETERS (slope + intercept, inside the sigmoid)
 ↓
EVALUATION (accuracy, and beyond)
 ↓
PREDICT NEW STUDENTS (class label or probability)
```

This is the same classical ML pattern as the regression examples in
this folder — only the model and the shape of the target change.

------------------------------------------------------------------------

## Try it

```bash
python src/student_result_model.py
```

Then try:

- Add `print(model.predict_proba(new_student))` — how confident is the
  model about the 5.9-hour student, compared to a student at 5.0
  hours?
- Change `test_size` to `0.5` and remove `stratify=y` — run it a few
  times with different `random_state` values. Does accuracy ever drop
  below `1.0`? What does that tell you about `stratify`?
- Compare this file with
  [`linear_regression_basics.py`](./linear_regression_basics.py) side
  by side — same `hours` data, two different questions being asked of
  it.
