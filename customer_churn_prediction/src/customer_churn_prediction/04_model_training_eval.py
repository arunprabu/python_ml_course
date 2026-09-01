import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load featured data
df = pd.read_csv("./data/customer_churn_featured.csv")

# Prepare data
X = df.drop(["customer_id", "churned"], axis=1)
# Convert categorical to numeric (one-hot encoding)
X = pd.get_dummies(X, drop_first=True)
y = df["churned"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# 7. PREDICT churn for a brand-new customer

new_customer = pd.DataFrame(
    {
        "age": [70],
        "gender": ["Female"],
        "tenure_months": [8],
        "subscription_plan": ["Standard"],
        "monthly_charges": [49.99],
        "total_charges": [399.92],
        "contract_type": ["Monthly"],
        "payment_method": ["Bank Transfer"],
        "login_frequency_monthly": [6],
        "features_used": [3],
        "data_consumption_gb": [12.5],
        "engagement_score": [40.0],
        "days_since_last_activity": [10],
        "billing_issues_count": [1],
        "plan_changes": [1],
        "support_tickets": [1],
        "avg_resolution_hours": [10.0],
        "satisfaction_score": [3.0],
        "nps_score": [5.0],
        "monthly_value_ratio": [49.99],
        "charge_per_feature": [16.66],
        "customer_lifetime_value": [399.92],
        "value_tier": ["Medium"],
        "engagement_velocity": [5.0],
        "login_intensity": [0.75],
        "data_per_login": [2.08],
        "activity_recency_category": ["Moderate"],
        "features_utilization_rate": [0.3],
        "data_per_tenure": [1.56],
        "support_rate_annual": [3.0],
        "resolution_burden": [10.0],
        "satisfaction_gap": [2.0],
        "billing_risk_flag": [1],
        "complaint_ratio": [0.125],
        "support_satisfaction_ratio": [0.67],
        "nps_category": ["Passive"],
        "plan_tenure_mismatch": [0],
        "usage_plan_mismatch": [0],
        "payment_stability": [0.5],
        "nps_satisfaction_alignment": [0.5],
        "contract_value_risk": [1],
        "lifecycle_stage": ["New"],
        "contract_tenure_ratio": [8.0],
        "tenure_category": ["0-1yr"],
        "engagement_growth_rate": [5.0],
        "tenure_stability": [0.02],
    }
)

# One-hot encode the same way as the training data, then make sure the
# columns match X exactly (same names, same order) before predicting
new_customer = pd.get_dummies(new_customer, drop_first=True)
new_customer = new_customer.reindex(columns=X.columns, fill_value=0)

predicted_churn = model.predict(new_customer)[0]
churn_probability = model.predict_proba(new_customer)[0][1]

print(f"\nPredicted churn: {'Yes' if predicted_churn == 1 else 'No'}")
print(f"Churn probability: {churn_probability:.1%}")
