import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

# Create models directory if it doesn't exist
os.makedirs('models', exist_ok=True)

# Load featured data
df = pd.read_csv('data/customer_churn_featured.csv')

# Prepare features and target
X = df.drop(['customer_id', 'churned'], axis=1)
X = pd.get_dummies(X, drop_first=True)
y = df['churned']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define parameter grid for hyperparameter tuning
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15],
    'min_samples_split': [2, 5, 10]
}

# Perform grid search with cross-validation
print("=" * 80)
print("HYPERPARAMETER TUNING WITH GRID SEARCH")
print("=" * 80)
print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")
print(f"Number of features: {X_train.shape[1]}")
print(f"\nParameter grid combinations: {len(param_grid['n_estimators']) * len(param_grid['max_depth']) * len(param_grid['min_samples_split'])}")
print("\nStarting grid search...\n")

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42), 
    param_grid, 
    cv=5, 
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)
grid_search.fit(X_train, y_train)

print(f"\n✓ Best parameters: {grid_search.best_params_}")
print(f"✓ Best cross-validation score: {grid_search.best_score_:.4f}")

# Train final model with best parameters
best_model = grid_search.best_estimator_

# Evaluate on test set
y_pred = best_model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 80)
print("TEST SET PERFORMANCE")
print("=" * 80)
print(f"Test Accuracy: {test_accuracy:.4f}\n")
print(classification_report(y_test, y_pred))

# Save the tuned model
model_path = 'models/tuned_churn_model.pkl'
joblib.dump(best_model, model_path)

print("=" * 80)
print("HYPERPARAMETER TUNING COMPLETE")
print("=" * 80)
print(f"✓ Tuned model saved to '{model_path}'")
print(f"✓ Best parameters: {grid_search.best_params_}")
print(f"✓ Test accuracy: {test_accuracy:.4f}")