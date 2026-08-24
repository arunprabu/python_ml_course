import pandas as pd

from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

pd.set_option("display.max_columns", None)  # print wide tables on one line, not wrapped
pd.set_option("display.width", 120)

"""
RIDGE AND LASSO REGRESSION (REGULARIZATION)

Ridge and Lasso are Linear Regression PLUS a penalty on large
coefficients ("regularization"). This matters when a dataset includes
features that don't actually explain the target — which happens often
in real spreadsheets, where every column that was collected tends to
get thrown into the model whether it's useful or not.

Scenario: predicting an employee's monthly salary. Two features are
genuinely related to salary (years of experience, certifications
earned). Two more were included in the data export but have nothing to
do with salary (birth month, a favorite-color code) — the kind of
irrelevant column that sneaks into real datasets.
"""


# 1. DATA — employee records, including two irrelevant columns

data = {
    "years_experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "certifications": [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 1, 0, 2, 1, 3, 2, 4, 3, 5, 4],
    "birth_month": [3, 7, 11, 1, 5, 9, 2, 6, 10, 4, 8, 12, 3, 7, 11, 1, 5, 9, 2, 6],
    "favorite_color_code": [2, 4, 1, 5, 3, 2, 4, 1, 5, 3, 2, 4, 1, 5, 3, 2, 4, 1, 5, 3],
    "monthly_salary_k": [
        35,
        39,
        46,
        48,
        55,
        59,
        67,
        68,
        76,
        79,
        38,
        36,
        47,
        47,
        58,
        56,
        67,
        67,
        79,
        76,
    ],
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# 2. FEATURES (X) and TARGET (y)

X = df[["years_experience", "certifications", "birth_month", "favorite_color_code"]]

y = df["monthly_salary_k"]


# 3. SPLIT into training and testing data

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=7
)


# 4. TRAIN three models on the exact same data

models = {
    "Linear Regression": LinearRegression(),
    "Ridge (alpha=1.0)": Ridge(alpha=1.0),
    "Lasso (alpha=1.0)": Lasso(alpha=1.0),
}

rows = []

for name, model in models.items():
    model.fit(X_train, y_train)
    r2 = r2_score(y_test, model.predict(X_test))
    rows.append({"model": name, "r2": round(r2, 3), **dict(zip(X.columns, model.coef_.round(2)))})


# 5. COMPARE — how does each model treat the two irrelevant features?

comparison = pd.DataFrame(rows).set_index("model")

print("\nCoefficients learned by each model:")
print(comparison)

print(
    "\nNotice: 'birth_month' and 'favorite_color_code' have nothing to do"
    " with salary.\nLasso pushes both close to (or exactly) 0 — feature"
    " selection — while Ridge only\nshrinks them slightly, and plain"
    " Linear Regression keeps them around."
)
