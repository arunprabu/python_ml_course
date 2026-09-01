import os
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

# --------------------------------------------------
# Configuration
# --------------------------------------------------

DATA_PATH = "data/customer_churn_featured.csv"
MODEL_PATH = "artifacts/tuned_churn_model.pkl"

os.makedirs("artifacts", exist_ok=True)


# --------------------------------------------------
# Load data
# --------------------------------------------------

df = pd.read_csv(DATA_PATH)

X = df.drop(["customer_id", "churned"], axis=1)
y = df["churned"]


# --------------------------------------------------
# Identify feature types
# --------------------------------------------------

categorical_features = X.select_dtypes(include=["object", "category"]).columns.tolist()

numerical_features = X.select_dtypes(exclude=["object", "category"]).columns.tolist()

print(f"Numerical features: {len(numerical_features)}")
print(f"Categorical features: {len(categorical_features)}")


# --------------------------------------------------
# Preprocessing
# --------------------------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore", drop="first"),
            categorical_features,
        ),
        (
            "numerical",
            "passthrough",
            numerical_features,
        ),
    ]
)


# --------------------------------------------------
# Model pipeline
# --------------------------------------------------

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "classifier",
            RandomForestClassifier(random_state=42),
        ),
    ]
)


# --------------------------------------------------
# Train/test split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)


print("=" * 80)
print("HYPERPARAMETER TUNING WITH GRID SEARCH")
print("=" * 80)

print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")
print(f"Features: {X.shape[1]}")


# --------------------------------------------------
# Hyperparameter grid
# --------------------------------------------------

param_grid = {
    "classifier__n_estimators": [50, 100, 200],
    "classifier__max_depth": [5, 10, 15],
    "classifier__min_samples_split": [2, 5, 10],
}


total_combinations = (
    len(param_grid["classifier__n_estimators"])
    * len(param_grid["classifier__max_depth"])
    * len(param_grid["classifier__min_samples_split"])
)

print(f"Parameter grid combinations: {total_combinations}")
print()


# --------------------------------------------------
# Grid Search
# --------------------------------------------------

grid_search = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1,
    verbose=1,
)

grid_search.fit(X_train, y_train)


print()
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best CV score: {grid_search.best_score_:.4f}")


# --------------------------------------------------
# Best model
# --------------------------------------------------

best_model = grid_search.best_estimator_


# --------------------------------------------------
# Evaluation
# --------------------------------------------------

y_pred = best_model.predict(X_test)

test_accuracy = accuracy_score(
    y_test,
    y_pred,
)

print()
print("=" * 80)
print("TEST SET PERFORMANCE")
print("=" * 80)

print(f"Test Accuracy: {test_accuracy:.4f}")
print()

print(classification_report(y_test, y_pred))


# --------------------------------------------------
# Save complete pipeline
# --------------------------------------------------

joblib.dump(
    best_model,
    MODEL_PATH,
)

print("=" * 80)
print("MODEL TRAINING COMPLETE")
print("=" * 80)

print(f"Model saved to: {MODEL_PATH}")
print(f"Best parameters: {grid_search.best_params_}")
print(f"Test accuracy: {test_accuracy:.4f}")
