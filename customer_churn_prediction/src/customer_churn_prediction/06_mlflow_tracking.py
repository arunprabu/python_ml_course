"""
Example 6: Experiment Tracking with MLflow

In examples 4 and 5 we trained models and printed the scores to the screen.
The problem: once you close the terminal, those numbers are gone. If you try
10 different settings, you have to remember which one worked best.

MLflow solves this. It records every training run - the settings you used,
the scores you got, and the model itself - so you can compare them later
in a web dashboard.

Three things we log for each run:
  1. Parameters  - the settings we chose (n_estimators, max_depth, ...)
  2. Metrics     - the results we measured (accuracy, precision, recall, f1)
  3. Model       - the trained model file itself
"""

import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Where MLflow stores everything (creates an "mlflow.db" file in the project)
mlflow.set_tracking_uri("sqlite:///mlflow.db")

# All runs from this script are grouped under one experiment name
mlflow.set_experiment("customer_churn")

# ----------------------------------------------------------------------
# 1. Load the data (same as examples 4 and 5)
# ----------------------------------------------------------------------
df = pd.read_csv("data/customer_churn_featured.csv")

X = df.drop(["customer_id", "churned"], axis=1)
X = pd.get_dummies(X, drop_first=True)
y = df["churned"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------------------------------------------------
# 2. Three different model settings we want to compare
# ----------------------------------------------------------------------
experiments = [
    {"n_estimators": 50, "max_depth": 3},
    {"n_estimators": 100, "max_depth": 5},
    {"n_estimators": 200, "max_depth": 10},
]

print("=" * 80)
print("MLFLOW EXPERIMENT TRACKING")
print("=" * 80)
print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")
print(f"Runs to log: {len(experiments)}\n")

results = []

# ----------------------------------------------------------------------
# 3. Train each model inside an MLflow run
# ----------------------------------------------------------------------
for i, params in enumerate(experiments, start=1):

    # Everything inside this "with" block belongs to one run
    with mlflow.start_run(run_name=f"random_forest_{i}"):

        # --- log the settings we are using ---
        mlflow.log_params(params)

        # --- train ---
        model = RandomForestClassifier(random_state=42, **params)
        model.fit(X_train, y_train)

        # --- evaluate ---
        y_pred = model.predict(X_test)
        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "precision": precision_score(y_test, y_pred, zero_division=0),
            "recall": recall_score(y_test, y_pred, zero_division=0),
            "f1": f1_score(y_test, y_pred, zero_division=0),
        }

        # --- log the results ---
        mlflow.log_metrics(metrics)

        # --- log the trained model itself ---
        mlflow.sklearn.log_model(model, name="model")

        results.append({**params, **metrics})

        print(f"Run {i}: {params}")
        print(f"        accuracy={metrics['accuracy']:.4f}  f1={metrics['f1']:.4f}")

# ----------------------------------------------------------------------
# 4. Compare the runs
# ----------------------------------------------------------------------
comparison = pd.DataFrame(results).sort_values("accuracy", ascending=False)

print("\n" + "=" * 80)
print("COMPARISON OF ALL RUNS (best first)")
print("=" * 80)
print(comparison.to_string(index=False))

best = comparison.iloc[0]
print(f"\n✓ Best run: n_estimators={int(best['n_estimators'])}, "
      f"max_depth={int(best['max_depth'])} -> accuracy={best['accuracy']:.4f}")

print("\n" + "=" * 80)
print("TRACKING COMPLETE")
print("=" * 80)
print("✓ Run details saved to 'mlflow.db', trained models saved in 'mlruns/'")
print("\nTo see them in the MLflow dashboard, run:")
print("    uv run mlflow ui --backend-store-uri sqlite:///mlflow.db")
print("\nThen open http://localhost:5000 in your browser.")
