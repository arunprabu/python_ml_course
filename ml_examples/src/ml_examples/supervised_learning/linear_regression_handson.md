# Hands-on: Train and Evaluate a Linear Regression Model

Code: [`linear_regression_handson.py`](./linear_regression_handson.py)

## The scenario

A small business tracks how much it spends on advertising each month
and the sales revenue that month. Marketing wants a model that
estimates sales from ad spend, so they can justify next quarter's
budget.

This is a guided, run-it-yourself walkthrough of the full workflow for
training and evaluating a Linear Regression model — the same steps
apply to almost any regression problem, including the other examples
in this folder.

------------------------------------------------------------------------

## Steps (already implemented in the script)

### STEP 1 — Load the data

```python
data = {"ad_spend_k": [...], "sales_k": [...]}
df = pd.DataFrame(data)
```

20 months of recorded ad spend and sales, in ₹ thousand. In a real
project this would usually come from `pd.read_csv("monthly_sales.csv")`
instead of being written directly in the script.

### STEP 2 — Choose features (X) and target (y)

```python
X = df[["ad_spend_k"]]   # must be 2D
y = df["sales_k"]         # 1D
```

### STEP 3 — Split into train/test sets

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=10
)
```

25% of the months are held out so we can measure performance on data
the model never saw during training.

### STEP 4 — Create and train the model

```python
model = LinearRegression()
model.fit(X_train, y_train)
```

### STEP 5 — Predict on the test set

```python
y_pred = model.predict(X_test)
```

### STEP 6 — Evaluate

```python
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
```

See [`linear_regression_basics.md`](./linear_regression_basics.md) for
what MAE, RMSE, and R² each mean and how to read them.

### STEP 7 — Use the trained model on new input

```python
new_data = pd.DataFrame({"ad_spend_k": [42]})
model.predict(new_data)
```

------------------------------------------------------------------------

## The complete workflow

```text
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
PREDICTIONS ON TEST SET
 ↓
EVALUATION (MAE, RMSE, R²)
 ↓
PREDICTION ON NEW DATA
```

Once this pattern feels familiar, you'll recognize it in
`house_price_prediction.py`, `polynomial_regression.py`, and
`ridge_lasso_regression.py` too — the model and the data change, but
the workflow stays the same.

Run it:

```bash
python src/linear_regression_handson.py
```

------------------------------------------------------------------------

## Exercises — try these by editing the script

1. **Change the split.** Set `test_size=0.4`. Does R² go up or down?
   With fewer training months, is the learned line noticeably
   different (check the printed slope/intercept)?
2. **Compare two ways of getting R².** Add
   `print(model.score(X_test, y_test))` right after evaluation.
   `.score()` on a regressor returns R² automatically — confirm it
   matches the `r2_score(...)` value already printed.
3. **Test extrapolation.** Predict sales for `ad_spend_k = 0` and for
   `ad_spend_k = 300`. The training data only covers roughly ₹5k-₹100k
   — do both predictions still look sensible? What does this suggest
   about trusting a linear model outside the range it was trained on?
4. **Add a second feature.** Add a `discount_pct` column (make up
   reasonable numbers, e.g. 0-20) to the data, decide on a plausible
   effect on `sales_k`, and include it in `X`. Retrain and check
   whether R² improves and what coefficient the new feature gets.
5. **Break an assumption on purpose.** Pick a few rows and change
   `sales_k` to something wildly inconsistent with the trend (an
   outlier), then re-run. What happens to MAE, RMSE, and R²? Which
   metric moves more, and why?

------------------------------------------------------------------------

## What "good" metrics look like here

There's no universal cutoff — it depends on the problem and what
decisions will be made from the predictions. As a sanity check for this
exercise: R² above ~0.7 suggests the model is capturing a real trend;
MAE/RMSE should be small relative to the typical `sales_k` values in
the data (a few ₹ thousand, not tens of thousands). Compare train-set
and test-set metrics too — a much better train score than test score is
a sign of overfitting.
