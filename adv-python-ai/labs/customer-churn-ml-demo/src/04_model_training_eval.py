import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load featured data
df = pd.read_csv('data/customer_churn_featured.csv')

# Prepare data
X = df.drop(['customer_id', 'churned'], axis=1)
# Convert categorical to numeric (one-hot encoding)
X = pd.get_dummies(X, drop_first=True)
y = df['churned']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))