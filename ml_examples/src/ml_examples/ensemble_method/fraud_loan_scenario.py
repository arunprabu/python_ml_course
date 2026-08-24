import pandas as pd

from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

"""
SCENARIO: Fraud Detection and Loan Default Prediction

Two of the most common real-world uses of gradient boosting share the
same shape: predict a rare, costly event (fraud, default) from
transaction/application data. They also share the same trap —
CLASS IMBALANCE. Most transactions aren't fraud; most loans aren't
defaulted on. A model — or a lazy baseline — can score a very high
ACCURACY just by predicting "no" every time, while being completely
useless at the one thing that actually matters: catching the rare
positive cases.

This file walks through fraud detection in full (Part A), then shows
the same playbook applied to loan default prediction (Part B) — same
techniques, different domain.
"""


# =============================================================================
# PART A — FRAUD DETECTION
# =============================================================================

# 1. DATA — card transactions, mostly legitimate, some fraudulent

fraud_data = {
    "amount": [45, 62, 38, 120, 55, 80, 29, 95, 150, 42, 480, 110, 33, 88, 58, 72, 25, 140, 48, 63,
               90, 105, 39, 77, 52, 68, 44, 99, 120, 35, 60, 85, 50, 73, 41, 96, 59, 82, 47, 65,
               15, 1200, 650, 980, 1500, 720, 1100, 890],
    "hour": [10, 14, 9, 16, 11, 13, 8, 17, 12, 15, 10, 14, 9, 16, 11, 13, 10, 15, 12, 14,
             9, 16, 11, 13, 10, 15, 12, 14, 9, 16, 10, 13, 11, 15, 9, 14, 12, 16, 10, 13,
             3, 2, 4, 1, 3, 2, 4, 1],
    "distance_from_home_km": [1, 2, 0, 3, 1, 2, 0, 4, 1, 2, 3, 1, 0, 2, 1, 3, 0, 2, 1, 4,
                               2, 1, 0, 3, 1, 2, 0, 3, 1, 2, 4, 1, 0, 2, 1, 3, 0, 2, 1, 3,
                               450, 600, 380, 700, 520, 410, 650, 480],
    "tx_last_hour": [1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2,
                      1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1,
                      6, 8, 5, 7, 9, 6, 8, 5],
    "is_foreign": [0] * 40 + [1] * 8,
    # 0 = legitimate, 1 = fraud
    "is_fraud": [0] * 40 + [1] * 8,
}

df = pd.DataFrame(fraud_data)

print("Dataset:")
print(df.describe().round(1))
print(f"\nFraud rate: {df['is_fraud'].mean():.1%} ({df['is_fraud'].sum()} of {len(df)} transactions)")


# 2. FEATURES (X), TARGET (y), TRAIN/TEST SPLIT

X = df.drop(columns="is_fraud")
y = df["is_fraud"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=5, stratify=y
)


# 3. THE ACCURACY TRAP — a baseline that never predicts fraud

baseline_predictions = pd.Series(0, index=y_test.index)

print(f"\n'Always legitimate' baseline accuracy: {accuracy_score(y_test, baseline_predictions):.1%}")
print(f"'Always legitimate' baseline recall (fraud actually caught): {recall_score(y_test, baseline_predictions):.1%}")
print("High accuracy, zero fraud caught — accuracy alone is the wrong metric here.")


# 4. TRAIN — XGBoost, weighted to pay more attention to the rare fraud class
#
# scale_pos_weight tells XGBoost how much more to penalize a missed
# fraud case vs. a missed legitimate one. A common starting point is
# the ratio of negative to positive examples in the training data.

scale_pos_weight = (y_train == 0).sum() / (y_train == 1).sum()
print(f"\nscale_pos_weight = {scale_pos_weight:.1f} "
      f"({(y_train == 0).sum()} legitimate / {(y_train == 1).sum()} fraud in training data)")

fraud_model = XGBClassifier(
    n_estimators=100, max_depth=3, scale_pos_weight=scale_pos_weight,
    eval_metric="logloss", random_state=42,
)
fraud_model.fit(X_train, y_train)

fraud_preds = fraud_model.predict(X_test)


# 5. EVALUATE with the metrics that actually matter for imbalanced classes

print("\nXGBoost fraud model:")
print(f"  Accuracy:  {accuracy_score(y_test, fraud_preds):.2f}")
print(f"  Precision: {precision_score(y_test, fraud_preds):.2f}  (of flagged transactions, how many were really fraud)")
print(f"  Recall:    {recall_score(y_test, fraud_preds):.2f}  (of actual fraud, how much did we catch)")
print(f"  F1:        {f1_score(y_test, fraud_preds):.2f}")
print(f"  Confusion matrix [[TN FP] [FN TP]]:\n{confusion_matrix(y_test, fraud_preds)}")


# =============================================================================
# PART B — LOAN DEFAULT PREDICTION
# =============================================================================
#
# A different domain, same playbook: imbalanced target, XGBoost with
# scale_pos_weight, evaluate with precision/recall instead of accuracy.

loan_data = {
    "credit_score": [720, 680, 750, 690, 710, 660, 740, 700, 730, 670, 760, 695, 715, 685, 705,
                      580, 610, 540, 595, 560],
    "annual_income_k": [65, 52, 80, 58, 70, 48, 75, 60, 72, 50, 85, 55, 68, 53, 62,
                         32, 38, 28, 35, 30],
    "debt_to_income": [0.25, 0.35, 0.20, 0.32, 0.28, 0.40, 0.22, 0.30, 0.24, 0.36, 0.18, 0.31, 0.27, 0.34, 0.29,
                        0.55, 0.60, 0.65, 0.58, 0.62],
    "past_defaults": [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,
                       1, 2, 2, 1, 2],
    "loan_amount_k": [15, 20, 12, 18, 16, 25, 14, 19, 15, 22, 10, 17, 16, 21, 18,
                       30, 35, 28, 32, 29],
    # 0 = repaid, 1 = defaulted
    "defaulted": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  1, 1, 1, 1, 1],
}

loan_df = pd.DataFrame(loan_data)

print("\n\nLoan dataset:")
print(f"Default rate: {loan_df['defaulted'].mean():.1%} ({loan_df['defaulted'].sum()} of {len(loan_df)} loans)")

X_loan = loan_df.drop(columns="defaulted")
y_loan = loan_df["defaulted"]

Xl_train, Xl_test, yl_train, yl_test = train_test_split(
    X_loan, y_loan, test_size=0.3, random_state=1, stratify=y_loan
)

loan_scale_pos_weight = (yl_train == 0).sum() / (yl_train == 1).sum()

loan_model = XGBClassifier(
    n_estimators=100, max_depth=3, scale_pos_weight=loan_scale_pos_weight,
    eval_metric="logloss", random_state=42,
)
loan_model.fit(Xl_train, yl_train)

loan_preds = loan_model.predict(Xl_test)

print("\nXGBoost loan default model:")
print(f"  Precision: {precision_score(yl_test, loan_preds):.2f}")
print(f"  Recall:    {recall_score(yl_test, loan_preds):.2f}")
print(f"  F1:        {f1_score(yl_test, loan_preds):.2f}")

print("\nFeature importance (which signals the model relied on most):")
for feature, importance in sorted(zip(X_loan.columns, loan_model.feature_importances_), key=lambda x: -x[1]):
    print(f"  {feature:<18} {importance:.3f}")
