import pandas as pd

from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

"""
XGBOOST, LIGHTGBM, CATBOOST: OVERVIEW AND WHEN TO USE

All three are GRADIENT BOOSTING libraries — the same core idea as
GradientBoostingClassifier in bagging_boosting_stacking.py (build trees
one at a time, each correcting the previous ensemble's mistakes), just
faster, more configurable, and more production-hardened than
scikit-learn's built-in version. They're the default choice for
serious work on structured/tabular data.

Scenario: the same telecom-churn idea as
bagging_boosting_stacking.py, but now with a CATEGORICAL feature,
`contract_type` ("month-to-month" / "one-year" / "two-year") — the
detail that most clearly separates these three libraries in practice.
"""


# 1. DATA — customers, including one categorical column

data = {
    "tenure_months": [3, 8, 15, 20, 5, 30, 12, 45, 2, 24, 36, 4, 18, 48, 30, 12, 6, 40, 55, 20, 33, 50, 15, 60],
    "monthly_charges": [95, 110, 75, 100, 60, 120, 90, 105, 70, 55, 48, 65, 52, 45, 58, 50, 125, 40, 35, 130, 38, 42, 45, 30],
    "contract_type": (
        ["month-to-month"] * 8 + ["one-year"] * 8 + ["two-year"] * 8
    ),
    "churned": [1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)
print(f"\nChurn rate: {df['churned'].mean():.1%}")


# 2. FEATURES (X) and TARGET (y), then a train/test split shared by all three

X = df[["tenure_months", "monthly_charges", "contract_type"]]
y = df["churned"]


# 3. XGBOOST and LIGHTGBM — both need NUMERIC input
#
# `contract_type` is text, so it has to be one-hot encoded into numeric
# columns before either library will accept it.

X_encoded = pd.get_dummies(X, columns=["contract_type"])

Xe_train, Xe_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.3, random_state=3, stratify=y
)

xgb_model = XGBClassifier(n_estimators=50, max_depth=3, eval_metric="logloss", random_state=42)
xgb_model.fit(Xe_train, y_train)
print(f"\nXGBoost  (one-hot encoded) test accuracy: {accuracy_score(y_test, xgb_model.predict(Xe_test)):.2f}")

lgb_model = LGBMClassifier(n_estimators=50, max_depth=3, min_child_samples=3, random_state=42, verbose=-1)
lgb_model.fit(Xe_train, y_train)
print(f"LightGBM (one-hot encoded) test accuracy: {accuracy_score(y_test, lgb_model.predict(Xe_test)):.2f}")


# 4. CATBOOST — hands the RAW categorical column straight to the model
#
# No one-hot encoding needed. Just tell CatBoost which column(s) are
# categorical via `cat_features`, and pass the original text column.

Xc_train, Xc_test, y_train2, y_test2 = train_test_split(
    X, y, test_size=0.3, random_state=3, stratify=y
)

cat_model = CatBoostClassifier(iterations=50, depth=3, verbose=0, random_state=42)
cat_model.fit(Xc_train, y_train2, cat_features=["contract_type"])
print(f"CatBoost (raw categorical)  test accuracy: {accuracy_score(y_test2, cat_model.predict(Xc_test)):.2f}")

print(
    "\nAll three trained successfully and land on comparable accuracy here —"
    "\nthe real difference isn't in this tiny demo's accuracy, it's in the"
    "\nworkflow: XGBoost/LightGBM made us encode `contract_type` by hand;"
    "\nCatBoost took the original text column directly."
)
