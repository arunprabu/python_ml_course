import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

"""
SCENARIO: House Price Prediction

A real-estate company wants to estimate a house's price
based on:

- area
- number of bedrooms
- age of the house
- distance from city center

We will train a Linear Regression model using historical
house listings and then use it to predict the price of
a brand-new house.
"""


# 1. DATA — historical house listings

data = {
    "area_sqft": [
        1000,
        1200,
        1500,
        1800,
        2000,
        2200,
        2500,
        2800,
        3000,
        1100,
        1400,
        1600,
        1900,
        2100,
        2300,
        2600,
        2900,
        3200,
        1300,
        1700,
    ],
    "bedrooms": [2, 2, 3, 3, 3, 4, 4, 4, 5, 2, 3, 3, 3, 4, 4, 4, 5, 5, 2, 3],
    "age_years": [10, 8, 12, 5, 7, 4, 6, 3, 2, 15, 10, 8, 6, 5, 4, 3, 2, 1, 12, 7],
    "distance_to_city_km": [
        15,
        12,
        10,
        8,
        7,
        6,
        5,
        4,
        3,
        18,
        14,
        11,
        9,
        7,
        6,
        5,
        4,
        3,
        16,
        10,
    ],
    "price": [
        180000,
        210000,
        280000,
        340000,
        370000,
        430000,
        480000,
        540000,
        600000,
        190000,
        260000,
        300000,
        350000,
        410000,
        450000,
        500000,
        560000,
        650000,
        230000,
        320000,
    ],
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# 2. FEATURES (X) and TARGET (y)
X = df[["area_sqft", "bedrooms", "age_years", "distance_to_city_km"]]

y = df["price"]


# 3. SPLIT into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=99
)


# 4. MODEL — train it
model = LinearRegression()

model.fit(X_train, y_train)


# 5. WHAT DID THE MODEL LEARN?
print("\nFeature effects on price:")

for feature, coef in zip(X.columns, model.coef_):
    print(f"  {feature:<25} {coef:>12,.2f}")

print(f"\nIntercept: {model.intercept_:,.2f}")


# 6. EVALUATE
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print(f"MAE:  {mae:,.0f}")
print(f"RMSE: {rmse:,.0f}")
print(f"R²:   {r2:.2f}")


# 7. PREDICT a brand-new house

new_house = pd.DataFrame(
    {
        "area_sqft": [2200],
        "bedrooms": [4],
        "age_years": [5],
        "distance_to_city_km": [8],
    }
)

predicted_price = model.predict(new_house)[0]

print(f"\nPredicted price for the new house: " f"${predicted_price:,.0f}")
