import pandas as pd

from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from xgboost import XGBClassifier

"""
HANDS-ON: Train an XGBoost model and tune hyperparameters.

Follow the numbered steps below and run this file. Then open
xgboost_handson.md for exercises — tweak this same script to complete
them.

Same churn dataset as bagging_boosting_stacking.py and
hyperparameter_tuning.py — this time we take it all the way through:
train a baseline XGBoost model, tune it, evaluate properly, and predict
for a new customer.
"""


# STEP 1 — Load the data

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
print("Sample of the data:")
print(df.head(), "\n")


# STEP 2 — Choose features (X) and target (y)

X = df[["tenure_months", "monthly_charges", "support_tickets"]]
y = df["churned"]


# STEP 3 — Split into train and test sets

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=8, stratify=y
)
print(f"Train rows: {len(X_train)}, Test rows: {len(X_test)}\n")


# STEP 4 — Train a baseline XGBoost model with reasonable default settings

baseline_model = XGBClassifier(n_estimators=100, max_depth=3, eval_metric="logloss", random_state=42)
baseline_model.fit(X_train, y_train)

baseline_train_acc = accuracy_score(y_train, baseline_model.predict(X_train))
baseline_test_acc = accuracy_score(y_test, baseline_model.predict(X_test))
print(f"Baseline XGBoost — train: {baseline_train_acc:.3f}, test: {baseline_test_acc:.3f}\n")


# STEP 5 — Define a hyperparameter search space to tune
#
# n_estimators    -> how many boosting rounds (trees) to build
# max_depth       -> how deep each tree can grow (deeper = more overfitting risk)
# learning_rate   -> how much each new tree corrects the previous ensemble
# subsample       -> fraction of rows each tree trains on (< 1.0 adds randomness, fights overfitting)

param_dist = {
    "n_estimators": [50, 100, 150, 200],
    "max_depth": [2, 3, 4, 5],
    "learning_rate": [0.01, 0.05, 0.1, 0.2],
    "subsample": [0.7, 0.8, 0.9, 1.0],
}


# STEP 6 — Search for better hyperparameters with RandomizedSearchCV

search = RandomizedSearchCV(
    XGBClassifier(eval_metric="logloss", random_state=42),
    param_dist,
    n_iter=12,
    cv=3,
    scoring="accuracy",
    random_state=42,
)
search.fit(X_train, y_train)

tuned_model = search.best_estimator_
print(f"Best params found: {search.best_params_}")
print(f"Best cross-validated accuracy: {search.best_score_:.3f}\n")


# STEP 7 — Evaluate the tuned model on the held-out test set

tuned_train_acc = accuracy_score(y_train, tuned_model.predict(X_train))
tuned_test_acc = accuracy_score(y_test, tuned_model.predict(X_test))

print(f"Tuned XGBoost — train: {tuned_train_acc:.3f}, test: {tuned_test_acc:.3f}")
print("\nFull classification report (tuned model, test set):")
print(classification_report(y_test, tuned_model.predict(X_test)))


# STEP 8 — Use the tuned model to predict for a new customer

new_customer = pd.DataFrame({"tenure_months": [6], "monthly_charges": [95], "support_tickets": [5]})
prediction = tuned_model.predict(new_customer)[0]
probability = tuned_model.predict_proba(new_customer)[0][1]

print(f"\nNew customer (6mo tenure, ₹95 charges, 5 support tickets):")
print(f"  Predicted: {'CHURN' if prediction == 1 else 'STAY'}")
print(f"  Churn probability: {probability:.1%}")

# ---------------------------------------------------------------------------
# TRY IT YOURSELF — see xgboost_handson.md for the full exercises.
# 1. Compare `baseline_train_acc` vs `tuned_train_acc` — which model fits
#    the training data more tightly? What does that suggest about which
#    one is more likely to generalize to new customers?
# 2. Add `early_stopping_rounds` using an eval_set — does training stop
#    before using all of the requested n_estimators?
# 3. Print `tuned_model.feature_importances_` — which feature does the
#    model lean on most to predict churn?
# ---------------------------------------------------------------------------
