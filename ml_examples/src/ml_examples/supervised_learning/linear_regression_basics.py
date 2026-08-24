import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

"""
LINEAR REGRESSION BASICS

Linear Regression predicts a NUMBER by fitting a straight line through
the data:

    y = m * x + c

Here we predict a student's exam score (0-100) from hours studied.

This uses the exact same "hours" values as the pass/fail example in
student_result_model.py, so you can compare the two side by side:

    Linear Regression   -> predicts a number     (score)
    Logistic Regression  -> predicts a class/prob  (pass/fail)
"""


# 1. DATA — hours studied vs exam score

data = {
    "hours": [
        1,
        1.5,
        2,
        2.5,
        3,
        3.5,
        4,
        4.5,
        5,
        5.5,
        6,
        6.5,
        7,
        7.5,
        8,
        8.5,
        9,
        9.5,
        10,
        10.5,
    ],
    "score": [
        35,
        38,
        42,
        44,
        50,
        48,
        55,
        58,
        60,
        63,
        65,
        68,
        72,
        75,
        78,
        80,
        83,
        85,
        90,
        92,
    ],
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# 2. FEATURES (X) and TARGET (y)

X = df[["hours"]]

y = df["score"]


# 3. SPLIT into training and testing data

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


# 4. MODEL — train it

model = LinearRegression()

model.fit(X_train, y_train)


# 5. WHAT DID THE MODEL LEARN?

print(f"\nLearned line: score = {model.coef_[0]:.2f} * hours + {model.intercept_:.2f}")


# 6. EVALUATE

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print(f"MAE:  {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²:   {r2:.2f}")


# 7. PREDICT for a new student

new_student = pd.DataFrame({"hours": [6.5]})

predicted_score = model.predict(new_student)[0]

print(f"\nPredicted score for 6.5 hours studied: {predicted_score:.1f}")
