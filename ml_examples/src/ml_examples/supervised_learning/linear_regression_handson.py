import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

"""
HANDS-ON: Train and evaluate a Linear Regression model, end to end.

Follow the numbered steps below and run this file. Then open
linear_regression_handson.md for exercises — tweak this same script to
complete them.

Scenario: a small business tracks how much it spends on advertising
each month, and the sales revenue that month. Marketing wants a model
that estimates sales from ad spend.
"""


# STEP 1 — Load the data
#
# In a real project this would usually come from a CSV
# (pd.read_csv("monthly_sales.csv")). Here it's written out directly so
# the example runs standalone with no extra files.

data = {
    "ad_spend_k": [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
    "sales_k": [22, 28, 35, 40, 48, 52, 60, 64, 70, 75, 82, 85, 92, 96, 101, 108, 112, 118, 124, 130],
}

df = pd.DataFrame(data)

print("Sample of the data:")
print(df.head(), "\n")


# STEP 2 — Choose features (X) and target (y)

X = df[["ad_spend_k"]]  # must be 2D

y = df["sales_k"]  # 1D


# STEP 3 — Split into train and test sets
#
# We hold out 25% of the months to check the model on data it never saw.

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=10
)

print(f"Train rows: {len(X_train)}, Test rows: {len(X_test)}\n")


# STEP 4 — Create and train the model

model = LinearRegression()

model.fit(X_train, y_train)

print(f"Learned line: sales_k = {model.coef_[0]:.2f} * ad_spend_k + {model.intercept_:.2f}\n")


# STEP 5 — Predict on the test set

y_pred = model.predict(X_test)


# STEP 6 — Evaluate the predictions

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("Evaluation on the test set:")
print(f"  MAE:  {mae:.2f}   (average error, in ₹ thousand)")
print(f"  RMSE: {rmse:.2f}  (typical error, penalizes big misses more)")
print(f"  R²:   {r2:.2f}    (1.0 = perfect fit, 0.0 = no better than guessing the mean)\n")


# STEP 7 — Use the model to predict something new

candidate_spend = 42
new_data = pd.DataFrame({"ad_spend_k": [candidate_spend]})
predicted_sales = model.predict(new_data)[0]

print(f"Predicted sales for ₹{candidate_spend}k ad spend: ₹{predicted_sales:.1f}k")

# ---------------------------------------------------------------------------
# TRY IT YOURSELF — see linear_regression_handson.md for the full exercises.
# 1. Change `test_size` to 0.4 — does R² go up or down? Why might that happen?
# 2. Add a print of `model.score(X_test, y_test)` — how does it compare to r2?
# 3. Predict sales for ad_spend_k = 0 and ad_spend_k = 300. Do both
#    predictions still make sense? What does that tell you about
#    extrapolating outside the training data range?
# ---------------------------------------------------------------------------
