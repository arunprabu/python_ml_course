import pandas as pd

from sklearn.ensemble import AdaBoostClassifier, BaggingClassifier, GradientBoostingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

"""
BAGGING vs BOOSTING vs STACKING

All three are ENSEMBLE METHODS: instead of training one model, train
several and combine their predictions. They differ in HOW the models
are trained and combined.

Scenario: a telecom company wants to predict which customers will
cancel their subscription (churn), from tenure, monthly charges, and
how many support tickets they've filed. A single Decision Tree tends
to memorize quirks of the training data (fits the training set
perfectly, but doesn't generalize as well) — ensembling is how you fix
that without throwing the tree away.

  BAGGING (Bootstrap AGGregatING)
    Train many copies of the SAME algorithm on different random
    samples of the training data (drawn with replacement), then
    average their votes. Each model trains independently — they never
    see each other's mistakes. Random Forest is bagging applied
    specifically to decision trees, with one extra trick (each tree
    also only considers a random subset of features at each split).

  BOOSTING
    Train models ONE AT A TIME, in sequence. Each new model focuses on
    the mistakes the previous ones made (AdaBoost reweights the
    misclassified rows; Gradient Boosting fits each new model to the
    previous ensemble's residual errors). The models are not
    independent — each one is a correction to what came before.

  STACKING
    Train several DIFFERENT algorithms (not necessarily trees at all),
    then train a small "meta-model" on top whose job is to learn how
    to best combine their predictions — smarter than a simple vote.
"""


# 1. DATA — customers, no ensemble-specific prep needed

data = {
    "tenure_months": [1, 48, 35, 22, 9, 56, 43, 30, 17, 4, 51, 38, 25, 12, 59, 46, 33, 20, 7, 54,
                       41, 28, 15, 2, 49, 36, 23, 10, 57, 44, 31, 18, 5, 52, 39, 26, 13, 60, 47, 34],
    "monthly_charges": [20, 57, 94, 31, 68, 105, 42, 79, 116, 53, 90, 27, 64, 101, 38, 75, 112, 49, 86, 23,
                         60, 97, 34, 71, 108, 45, 82, 119, 56, 93, 30, 67, 104, 41, 78, 115, 52, 89, 26, 63],
    "support_tickets": [0, 4, 8, 3, 7, 2, 6, 1, 5, 0, 4, 8, 3, 7, 2, 6, 1, 5, 0, 4,
                         8, 3, 7, 2, 6, 1, 5, 0, 4, 8, 3, 7, 2, 6, 1, 5, 0, 4, 8, 3],
    # 0 = stayed, 1 = churned
    "churned": [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1,
                1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)
print(f"\nChurn rate: {df['churned'].mean():.1%}")


# 2. FEATURES (X) and TARGET (y)

X = df[["tenure_months", "monthly_charges", "support_tickets"]]
y = df["churned"]


# 3. SPLIT into training and testing data

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=8, stratify=y
)


# 4. BASELINE — a single Decision Tree

tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train, y_train)

tree_train_acc = accuracy_score(y_train, tree.predict(X_train))
tree_test_acc = accuracy_score(y_test, tree.predict(X_test))

print(f"\nSingle Decision Tree — train: {tree_train_acc:.3f}, test: {tree_test_acc:.3f}")
print("(train == 1.0 is a red flag: the tree has memorized the training rows)")


# 5. BAGGING — many trees, trained independently on random samples, then voted

bagging = BaggingClassifier(estimator=DecisionTreeClassifier(), n_estimators=50, random_state=42)
bagging.fit(X_train, y_train)

print(f"Bagging (50 trees)        — train: {accuracy_score(y_train, bagging.predict(X_train)):.3f}, "
      f"test: {accuracy_score(y_test, bagging.predict(X_test)):.3f}")


# 6. BOOSTING — models trained in sequence, each correcting the last

adaboost = AdaBoostClassifier(n_estimators=50, random_state=42)
adaboost.fit(X_train, y_train)

gradient_boost = GradientBoostingClassifier(n_estimators=50, random_state=42)
gradient_boost.fit(X_train, y_train)

print(f"AdaBoost (50 rounds)      — train: {accuracy_score(y_train, adaboost.predict(X_train)):.3f}, "
      f"test: {accuracy_score(y_test, adaboost.predict(X_test)):.3f}")
print(f"Gradient Boosting (50)    — train: {accuracy_score(y_train, gradient_boost.predict(X_train)):.3f}, "
      f"test: {accuracy_score(y_test, gradient_boost.predict(X_test)):.3f}")


# 7. STACKING — different algorithms, combined by a learned meta-model

stacking = StackingClassifier(
    estimators=[
        ("tree", DecisionTreeClassifier(max_depth=3, random_state=42)),
        ("bagged_trees", BaggingClassifier(n_estimators=20, random_state=42)),
    ],
    final_estimator=LogisticRegression(),
)
stacking.fit(X_train, y_train)

print(f"Stacking (tree + bagging) — train: {accuracy_score(y_train, stacking.predict(X_train)):.3f}, "
      f"test: {accuracy_score(y_test, stacking.predict(X_test)):.3f}")

print(
    "\nNotice the pattern: the single tree gets every training row right but"
    "\nslips on the test set — classic overfitting. Bagging and Stacking both"
    "\nclose that gap on this run; boosting matches the tree's test score here"
    "\nwhile fitting the training data a little less rigidly."
)
