import itertools

import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, train_test_split

"""
HYPERPARAMETER TUNING: GridSearchCV vs RandomizedSearchCV

Every model so far used hyperparameters we just picked by hand
(n_estimators=50, max_depth=3, ...). Those choices matter — too shallow
and the model underfits, too deep and it overfits, like the single tree
in bagging_boosting_stacking.py. Hyperparameter tuning is the process
of searching for a good combination automatically, using
cross-validation to judge each candidate instead of guessing.

Same churn dataset as bagging_boosting_stacking.py — this time we tune
a RandomForestClassifier's settings instead of picking them by hand.

  GridSearchCV
    Try EVERY combination of the hyperparameter values you list.
    Exhaustive and guaranteed to find the best combo *within the grid
    you specified* — but the number of combinations (and therefore the
    time it takes) multiplies fast as you add more values or more
    hyperparameters.

  RandomizedSearchCV
    Try a fixed NUMBER of random combinations instead of all of them.
    Won't necessarily find the exact best combo in the grid, but often
    finds a comparably good one for a fraction of the compute — useful
    when the search space is too large to try exhaustively.
"""


# 1. DATA — same customers as bagging_boosting_stacking.py

data = {
    "tenure_months": [1, 48, 35, 22, 9, 56, 43, 30, 17, 4, 51, 38, 25, 12, 59, 46, 33, 20, 7, 54,
                       41, 28, 15, 2, 49, 36, 23, 10, 57, 44, 31, 18, 5, 52, 39, 26, 13, 60, 47, 34],
    "monthly_charges": [20, 57, 94, 31, 68, 105, 42, 79, 116, 53, 90, 27, 64, 101, 38, 75, 112, 49, 86, 23,
                         60, 97, 34, 71, 108, 45, 82, 119, 56, 93, 30, 67, 104, 41, 78, 115, 52, 89, 26, 63],
    "support_tickets": [0, 4, 8, 3, 7, 2, 6, 1, 5, 0, 4, 8, 3, 7, 2, 6, 1, 5, 0, 4,
                         8, 3, 7, 2, 6, 1, 5, 0, 4, 8, 3, 7, 2, 6, 1, 5, 0, 4, 8, 3],
    "churned": [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1,
                1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
}

df = pd.DataFrame(data)


# 2. FEATURES (X), TARGET (y), TRAIN/TEST SPLIT

X = df[["tenure_months", "monthly_charges", "support_tickets"]]
y = df["churned"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=8, stratify=y
)


# 3. DEFINE the search space — every hyperparameter we're willing to try

param_grid = {
    "n_estimators": [50, 100, 150],
    "max_depth": [2, 4, 6],
    "min_samples_leaf": [1, 2, 4],
}

total_combinations = len(list(itertools.product(*param_grid.values())))
print(f"Search space: {total_combinations} combinations "
      f"({' × '.join(str(len(v)) for v in param_grid.values())})")


# 4. GridSearchCV — try every combination, scored with cross-validation

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=3,
    scoring="accuracy",
)
grid_search.fit(X_train, y_train)

print(f"\nGridSearchCV — fit {len(grid_search.cv_results_['params'])} candidates × 3 folds "
      f"= {len(grid_search.cv_results_['params']) * 3} models trained")
print(f"  Best params: {grid_search.best_params_}")
print(f"  Best CV accuracy: {grid_search.best_score_:.3f}")
print(f"  Test accuracy: {accuracy_score(y_test, grid_search.predict(X_test)):.3f}")


# 5. RandomizedSearchCV — try a fixed NUMBER of random combinations instead

random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    n_iter=8,
    cv=3,
    scoring="accuracy",
    random_state=42,
)
random_search.fit(X_train, y_train)

print(f"\nRandomizedSearchCV — fit {len(random_search.cv_results_['params'])} candidates × 3 folds "
      f"= {len(random_search.cv_results_['params']) * 3} models trained")
print(f"  Best params: {random_search.best_params_}")
print(f"  Best CV accuracy: {random_search.best_score_:.3f}")
print(f"  Test accuracy: {accuracy_score(y_test, random_search.predict(X_test)):.3f}")

print(
    "\nRandomizedSearchCV tried less than a third of the combinations"
    "\nGridSearchCV did, landed on a DIFFERENT set of parameters, and still"
    "\nmatched GridSearchCV's cross-validated score. On a small grid like"
    "\nthis one, GridSearchCV is cheap enough to just run — the payoff for"
    "\nRandomizedSearchCV shows up once the grid gets too large to search"
    "\nexhaustively in reasonable time."
)
