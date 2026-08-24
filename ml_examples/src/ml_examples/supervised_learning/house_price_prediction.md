# Scenario: House Price Prediction

Code: [`house_price_prediction.py`](./house_price_prediction.py)

## The scenario

A real-estate company wants a quick estimate of a house's market price
based on a few known facts about it.

They have a dataset of past house sales:

  Feature / Target        Meaning
  ----------------------- --------------------------------------
  `area_sqft`             Size of the house
  `bedrooms`              Number of bedrooms
  `age_years`             Age of the house
  `distance_to_city_km`   Distance from the city center
  `price`                 Actual selling price, our **target**

Our goal is simple:

> Given the characteristics of a house, predict its price.

This is a good Linear Regression problem because `price` is a
**continuous number**.

We expect some useful relationships:

-   Larger houses generally cost more.
-   More bedrooms generally increase price.
-   Older houses may be worth less.
-   Houses farther from the city center may be worth less.

The relationships do not need to be perfectly true. Linear Regression is
trying to find a useful approximation from the historical data.

------------------------------------------------------------------------

## What are the features and target?

The four things we know about a house are our **features**:

``` text
area_sqft
bedrooms
age_years
distance_to_city_km
```

The thing we want to predict is the **target**:

``` text
price
```

In the code:

``` python
X = df[
    [
        "area_sqft",
        "bedrooms",
        "age_years",
        "distance_to_city_km"
    ]
]

y = df["price"]
```

Think of it as:

``` text
                 FEATURES
              ┌───────────────┐
House ───────►│ area          │
              │ bedrooms      │
              │ age           │
              │ distance      │
              └───────┬───────┘
                      │
                      ▼
               Linear Regression
                      │
                      ▼
                   PRICE
                  TARGET
```

------------------------------------------------------------------------

## What does Linear Regression learn?

Linear Regression tries to learn an equation like:

``` text
price =
    w1 × area_sqft
  + w2 × bedrooms
  + w3 × age_years
  + w4 × distance_to_city_km
  + b
```

The `w` values and `b` are the **parameters learned by the model**.

For example, the model might learn something conceptually like:

``` text
price =
    150 × area
  + 20,000 × bedrooms
  - 800 × age
  - 2,500 × distance
  + 50,000
```

The exact numbers above are only an illustration. The actual values are
learned from the training data.

### Important: features are not parameters

This example is also useful for understanding a common ML confusion.

We have:

``` text
4 features
```

but Linear Regression learns:

``` text
5 parameters
```

Four coefficients:

``` text
w1 → area coefficient
w2 → bedroom coefficient
w3 → age coefficient
w4 → distance coefficient
```

and one intercept:

``` text
b → intercept
```

So:

> **Features are the inputs. Parameters are the values the model learns
> to combine those inputs.**

------------------------------------------------------------------------

## Why start with Linear Regression?

### 1. It is simple

The model is easy to understand:

``` text
Input features
      ↓
weighted combination
      ↓
predicted price
```

It is much easier to explain than many complex models.

For example, a coefficient can give us an interpretation such as:

> Holding the other features constant, an additional bedroom is
> associated with an increase of approximately ₹X in the model's
> predicted price.

The phrase **"holding the other features constant"** is important.

------------------------------------------------------------------------

### 2. It gives us a baseline

Linear Regression is often a useful **baseline model**.

Suppose we later try:

-   Decision Tree
-   Random Forest
-   XGBoost
-   Neural Network

We should first know how well a simple model performs.

If Linear Regression achieves an acceptable result, a much more
complicated model may not be necessary.

If a complex model performs significantly better, then the additional
complexity may be justified.

------------------------------------------------------------------------

### 3. The coefficients provide insight

Unlike some black-box models, Linear Regression gives us coefficients
that we can inspect:

``` python
for feature, coef in zip(X.columns, model.coef_):
    print(feature, coef)
```

A positive coefficient means that, all else equal, increasing that
feature increases the model's prediction.

A negative coefficient means that, all else equal, increasing that
feature decreases the model's prediction.

However, **coefficient size alone does not tell us which feature is most
important**, because the features use different units.

For example:

``` text
area       → square feet
bedrooms   → number of rooms
age        → years
distance   → kilometers
```

Comparing `150` for area directly with `20,000` for bedrooms would
therefore be misleading.

------------------------------------------------------------------------

# Walking through the code

## 1. Load the data

The example uses a small dataset directly in the Python file.

``` python
data = {
    "area_sqft": [...],
    "bedrooms": [...],
    "age_years": [...],
    "distance_to_city_km": [...],
    "price": [...]
}

df = pd.DataFrame(data)
```

This represents historical house sales.

In a real application, the data could instead come from:

-   CSV
-   Excel
-   SQL database
-   API
-   data warehouse

For learning purposes, keeping the dataset inside the Python file makes
the example easy to reproduce.

------------------------------------------------------------------------

## 2. Separate features and target

``` python
X = df[
    [
        "area_sqft",
        "bedrooms",
        "age_years",
        "distance_to_city_km"
    ]
]

y = df["price"]
```

Remember:

``` text
X → what the model knows
y → what the model needs to predict
```

------------------------------------------------------------------------

## 3. Split the data

We don't want the model to see every house during training.

``` python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=99
)
```

With 20 houses, approximately:

``` text
16 houses → training
 4 houses → testing
```

The model learns from the training houses.

The test houses are kept aside.

This lets us ask:

> Can the model make good predictions for houses it has never seen
> before?

That is much more useful than checking how well it predicts the same
data it was trained on.

------------------------------------------------------------------------

## 4. Train the model

``` python
model = LinearRegression()

model.fit(X_train, y_train)
```

This is where learning happens.

The model looks at the training examples and searches for coefficients
that produce predictions close to the known prices.

Conceptually:

``` text
Training data
     ↓
Find useful coefficients
     ↓
w1, w2, w3, w4, b
     ↓
Learned Linear Regression model
```

------------------------------------------------------------------------

## 5. Inspect what the model learned

``` python
for feature, coef in zip(X.columns, model.coef_):
    print(feature, coef)
```

You can also inspect:

``` python
model.intercept_
```

The result gives us the learned parameters.

For example:

``` text
area_sqft              150.20
bedrooms             18250.40
age_years             -812.30
distance_to_city_km  -2410.70
```

The interpretation would be approximately:

``` text
area:
  Increasing area tends to increase predicted price.

bedrooms:
  Increasing bedrooms tends to increase predicted price.

age:
  Increasing age tends to decrease predicted price.

distance:
  Increasing distance tends to decrease predicted price.
```

Again, these are model relationships, not proof that changing one
real-world variable by itself will cause the price to change by exactly
that amount.

------------------------------------------------------------------------

## 6. Evaluate the model

Now we ask:

> How good are the predictions on houses the model did not train on?

``` python
y_pred = model.predict(X_test)
```

We then compare:

``` text
actual price
     vs
predicted price
```

using evaluation metrics.

### MAE

``` python
mae = mean_absolute_error(y_test, y_pred)
```

MAE tells us the average absolute prediction error.

If:

``` text
MAE = ₹25,000
```

we can roughly say:

> The model's predictions are off by about ₹25,000 on average.

------------------------------------------------------------------------

### RMSE

``` python
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
```

RMSE is similar to MAE, but it penalizes large errors more heavily.

That makes it useful when very large prediction mistakes are
particularly undesirable.

------------------------------------------------------------------------

### R²

``` python
r2 = r2_score(y_test, y_pred)
```

R² tells us how much of the variation in the target is explained by the
model relative to a simple mean-based baseline.

For example:

``` text
R² = 0.80
```

means the model explains about 80% of the variation in the test data
under the R² definition.

Do not interpret R² as:

> "The model is 80% accurate."

R² is not an accuracy percentage.

------------------------------------------------------------------------

# 7. Predict a brand-new house

Finally, we give the model a house it has never seen:

``` python
new_house = pd.DataFrame(
    {
        "area_sqft": [2200],
        "bedrooms": [4],
        "age_years": [5],
        "distance_to_city_km": [8],
    }
)
```

Then:

``` python
predicted_price = model.predict(new_house)[0]
```

The complete ML workflow is:

``` text
Historical house data
        ↓
Separate X and y
        ↓
Train / test split
        ↓
Train Linear Regression
        ↓
Learn parameters
        ↓
Make predictions
        ↓
Evaluate predictions
        ↓
Predict a new house
```

------------------------------------------------------------------------

# Things to watch for in a real house-price model

The example is intentionally simple. Real-world data introduces
additional problems.

## Multicollinearity

`area_sqft` and `bedrooms` may be correlated.

For example:

``` text
Bigger house → usually more bedrooms
```

When features are strongly correlated, individual coefficients can
become unstable or difficult to interpret.

For such cases, techniques such as Ridge or Lasso regression can be
useful.

See:

[`ridge_lasso_regression.md`](./ridge_lasso_regression.md)

------------------------------------------------------------------------

## Non-linear relationships

Real house prices may not change linearly.

For example, the effect of distance might look more like:

``` text
Price
  │\
  │ \
  │  \
  │    \__
  │        \____
  └────────────── Distance
```

The first few kilometers from the city center might matter much more
than the next few kilometers.

If the relationship is clearly non-linear, consider:

-   Polynomial Regression
-   engineered features
-   tree-based models

See:

[`polynomial_regression.md`](./polynomial_regression.md)

------------------------------------------------------------------------

## Outliers

Imagine most houses cost between:

``` text
₹200,000 - ₹600,000
```

but one luxury mansion costs:

``` text
₹5,000,000
```

That unusual data point can have a large influence on a Linear
Regression model.

Always inspect unusual observations before trusting the model.

------------------------------------------------------------------------

## Extrapolation

Suppose the training data contains:

``` text
400 - 3000 sqft
1 - 5 bedrooms
```

Then asking the model to predict:

``` text
10,000 sqft
20 bedrooms
```

is dangerous.

The model is being asked to predict outside the range of data it learned
from.

A good rule is:

> **Interpolation is generally safer than extrapolation.**

------------------------------------------------------------------------

# One important learning point

This example demonstrates the complete classical ML pattern:

``` text
DATA
 ↓
FEATURES + TARGET
 ↓
TRAIN / TEST SPLIT
 ↓
MODEL
 ↓
LEARN PARAMETERS
 ↓
PREDICTIONS
 ↓
EVALUATION
 ↓
NEW PREDICTION
```

Once you understand this workflow, the same pattern appears across many
other ML problems.

The model changes.

The data changes.

The target changes.

But the overall workflow remains remarkably similar.

------------------------------------------------------------------------

# Try it

Run:

``` bash
python src/house_price_prediction.py
```

Then change the values in `new_house`:

``` python
new_house = pd.DataFrame(
    {
        "area_sqft": [2200],
        "bedrooms": [4],
        "age_years": [5],
        "distance_to_city_km": [8],
    }
)
```

Try questions such as:

-   What happens if the area increases from 2200 to 3000 sqft?
-   What happens if the house has one additional bedroom?
-   What happens if the house is 20 years older?
-   What happens if the house is farther from the city?

This is a good way to build intuition for what the learned parameters
actually do.
