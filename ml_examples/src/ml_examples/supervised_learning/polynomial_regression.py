import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

"""
POLYNOMIAL REGRESSION

Plain Linear Regression can only draw a STRAIGHT LINE. That works badly
when the real relationship is curved.

We will use recorded braking-test data: a car's speed vs how far it
travels before stopping. Braking distance does not grow linearly with
speed — a car going twice as fast needs roughly four times the distance
to stop, because it carries roughly four times the kinetic energy. This
kind of "grows with the square of x" relationship is a classic case for
Polynomial Regression.
"""


# 1. DATA — recorded braking distance at different speeds

data = {
    "speed_kmh": [
        20,
        25,
        30,
        35,
        40,
        45,
        50,
        55,
        60,
        65,
        70,
        75,
        80,
        85,
        90,
        95,
        100,
        105,
        110,
        115,
    ],
    "braking_distance_m": [
        2,
        3,
        5,
        7,
        9,
        11,
        14,
        17,
        20,
        23,
        27,
        31,
        35,
        40,
        45,
        50,
        55,
        61,
        67,
        73,
    ],
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# 2. FEATURES (X) and TARGET (y)

X = df[["speed_kmh"]]

y = df["braking_distance_m"]


# 3. SPLIT into training and testing data

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=10
)


# 4. BASELINE — plain Linear Regression (a straight line) on curved data

linear_model = LinearRegression()

linear_model.fit(X_train, y_train)

linear_r2 = r2_score(y_test, linear_model.predict(X_test))

print(f"\nStraight-line Linear Regression R²:  {linear_r2:.3f}  (underfits — data is curved)")


# 5. POLYNOMIAL REGRESSION — degree 2 captures the curve

poly_model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())

poly_model.fit(X_train, y_train)

poly_r2 = r2_score(y_test, poly_model.predict(X_test))

print(f"Degree-2 Polynomial Regression R²:   {poly_r2:.3f}  (captures the curve)")


# 6. OVERFITTING WARNING — too high a degree memorizes noise, not the trend

overfit_model = make_pipeline(PolynomialFeatures(degree=8), LinearRegression())

overfit_model.fit(X_train, y_train)

overfit_r2 = r2_score(y_test, overfit_model.predict(X_test))

print(f"Degree-8 Polynomial Regression R²:   {overfit_r2:.3f}  (overfit — worse than even the straight line)")


# 7. PREDICT braking distance for a new speed, using the degree-2 model

new_speed = pd.DataFrame({"speed_kmh": [72]})

predicted_distance = poly_model.predict(new_speed)[0]

print(f"\nPredicted braking distance at 72 km/h: {predicted_distance:.1f} m")
