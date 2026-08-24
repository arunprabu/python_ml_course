# Comprehensive Machine Learning Guide

## Table of Contents

1. [What is Machine Learning?](#what-is-machine-learning)
2. [Types of Machine Learning](#types-of-machine-learning)
3. [Key Concepts](#key-concepts)
4. [Algorithms](#algorithms)
5. [Model Evaluation](#model-evaluation)
6. [Best Practices](#best-practices)

---

## What is Machine Learning?

Machine Learning (ML) is a subset of Artificial Intelligence that enables systems to **learn patterns from data** and make decisions without being explicitly programmed.

### Core Principle

```
Data + Algorithm = Model → Predictions
```

### ML vs Traditional Programming

| Traditional Programming | Machine Learning      |
| ----------------------- | --------------------- |
| Input: Data + Rules     | Input: Data + Output  |
| Output: Answers         | Output: Rules (Model) |

---

## Types of Machine Learning

### 1. Supervised Learning

Learning from **labeled data** where both input and expected output are provided.

```python
# Example: Predicting house prices
X = [[1500, 3], [2000, 4], [1200, 2]]  # Features: [sqft, bedrooms]
y = [300000, 450000, 250000]            # Labels: prices

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)
prediction = model.predict([[1800, 3]])
```

**Use Cases:**

- Spam detection
- Image classification
- Price prediction
- Medical diagnosis

**Subcategories:**

- **Classification**: Predicting discrete categories (spam/not spam)
- **Regression**: Predicting continuous values (price, temperature)

---

### 2. Unsupervised Learning

Learning from **unlabeled data** to discover hidden patterns.

```python
# Example: Customer segmentation
from sklearn.cluster import KMeans

X = [[25, 50000], [45, 80000], [35, 60000], [50, 90000]]
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
labels = kmeans.labels_  # Cluster assignments
```

**Use Cases:**

- Customer segmentation
- Anomaly detection
- Dimensionality reduction
- Market basket analysis

**Subcategories:**

- **Clustering**: Grouping similar data points
- **Dimensionality Reduction**: Reducing features while preserving information
- **Association**: Finding relationships between variables

---

### 3. Semi-Supervised Learning

Combines **small amounts of labeled data** with large amounts of unlabeled data.

**Use Cases:**

- Web content classification
- Speech recognition
- Medical image analysis (limited expert labels)

---

### 4. Reinforcement Learning

Learning through **trial and error** with rewards and penalties.

```python
# Conceptual example
# Agent takes action → Environment gives reward → Agent learns

# Q-Learning update rule:
# Q(s,a) = Q(s,a) + α[R + γ*max(Q(s',a')) - Q(s,a)]
```

**Key Components:**

- **Agent**: The learner/decision maker
- **Environment**: What the agent interacts with
- **State**: Current situation
- **Action**: Possible moves
- **Reward**: Feedback signal

**Use Cases:**

- Game playing (AlphaGo, Chess)
- Robotics
- Autonomous vehicles
- Resource management

---

## Key Concepts

### Features and Labels

```python
# Features (X): Input variables used for prediction
# Labels (y): Output variable we want to predict

features = ['age', 'income', 'education']  # Independent variables
label = 'purchased'                         # Dependent variable
```

### Training, Validation, and Test Sets

```python
from sklearn.model_selection import train_test_split

# Split data: 70% train, 15% validation, 15% test
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5)
```

| Set        | Purpose               | Typical Size |
| ---------- | --------------------- | ------------ |
| Training   | Model learns patterns | 60-80%       |
| Validation | Hyperparameter tuning | 10-20%       |
| Test       | Final evaluation      | 10-20%       |

### Overfitting vs Underfitting

```
Underfitting          Good Fit           Overfitting
(High Bias)                              (High Variance)
    ___                  /\                  /\/\
   /                    /  \                /    \
  /                    /    \              /      \

- Too simple          - Just right        - Too complex
- Poor on train       - Good on both      - Great on train
- Poor on test        - Good on test      - Poor on test
```

### Bias-Variance Tradeoff

```
Total Error = Bias² + Variance + Irreducible Error

High Bias: Model too simple, misses patterns
High Variance: Model too complex, captures noise
Goal: Find the sweet spot
```

### Feature Engineering

```python
# Common techniques:

# 1. Normalization (0-1 range)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)

# 2. Standardization (mean=0, std=1)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)

# 3. One-Hot Encoding (categorical → numerical)
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X_categorical)

# 4. Feature Selection
from sklearn.feature_selection import SelectKBest
selector = SelectKBest(k=5)
X_selected = selector.fit_transform(X, y)
```

---

## Algorithms

### Supervised Learning Algorithms

#### 1. Linear Regression

Predicts continuous values using a linear relationship.

```python
from sklearn.linear_model import LinearRegression

# y = mx + b (simple) or y = w₁x₁ + w₂x₂ + ... + b (multiple)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

**Pros:** Simple, interpretable, fast
**Cons:** Assumes linear relationship, sensitive to outliers

---

#### 2. Logistic Regression

Binary/multi-class classification using sigmoid function.

```python
from sklearn.linear_model import LogisticRegression

# Uses sigmoid: σ(z) = 1 / (1 + e^(-z))
model = LogisticRegression()
model.fit(X_train, y_train)
probabilities = model.predict_proba(X_test)
```

**Pros:** Probabilistic output, interpretable
**Cons:** Linear decision boundary, limited to classification

---

#### 3. Decision Trees

Tree-like model of decisions based on feature values.

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, y_train)

# Visualize the tree
from sklearn.tree import plot_tree
plot_tree(model, feature_names=feature_names)
```

**Pros:** Interpretable, handles non-linear data, no scaling needed
**Cons:** Prone to overfitting, unstable

---

#### 4. Random Forest

Ensemble of decision trees using bagging.

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,    # Number of trees
    max_depth=10,        # Max tree depth
    random_state=42
)
model.fit(X_train, y_train)

# Feature importance
importances = model.feature_importances_
```

**Pros:** Robust, handles overfitting, feature importance
**Cons:** Less interpretable, computationally expensive

---

#### 5. Gradient Boosting (XGBoost, LightGBM)

Sequential ensemble that corrects previous errors.

```python
from sklearn.ensemble import GradientBoostingClassifier
# Or use XGBoost for better performance
import xgboost as xgb

model = xgb.XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=6
)
model.fit(X_train, y_train)
```

**Pros:** High accuracy, handles imbalanced data
**Cons:** Prone to overfitting, slower training

---

#### 6. Support Vector Machines (SVM)

Finds optimal hyperplane to separate classes.

```python
from sklearn.svm import SVC

model = SVC(
    kernel='rbf',    # 'linear', 'poly', 'rbf', 'sigmoid'
    C=1.0,           # Regularization
    gamma='scale'    # Kernel coefficient
)
model.fit(X_train, y_train)
```

**Pros:** Effective in high dimensions, memory efficient
**Cons:** Slow on large datasets, requires scaling

---

#### 7. K-Nearest Neighbors (KNN)

Classifies based on majority vote of k nearest neighbors.

```python
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(
    n_neighbors=5,
    weights='distance',  # 'uniform' or 'distance'
    metric='euclidean'
)
model.fit(X_train, y_train)
```

**Pros:** Simple, no training phase, naturally handles multi-class
**Cons:** Slow predictions, sensitive to scale and noise

---

#### 8. Naive Bayes

Probabilistic classifier based on Bayes' theorem.

```python
from sklearn.naive_bayes import GaussianNB, MultinomialNB

# For continuous data
model = GaussianNB()

# For text/count data
model = MultinomialNB()

model.fit(X_train, y_train)
```

**Pros:** Fast, works well with small data, good for text
**Cons:** Assumes feature independence

---

### Unsupervised Learning Algorithms

#### 1. K-Means Clustering

Partitions data into k clusters based on centroids.

```python
from sklearn.cluster import KMeans

model = KMeans(
    n_clusters=3,
    init='k-means++',
    n_init=10,
    random_state=42
)
model.fit(X)
labels = model.labels_
centroids = model.cluster_centers_

# Finding optimal k (Elbow method)
inertias = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)
```

**Pros:** Simple, scalable
**Cons:** Must specify k, sensitive to initialization

---

#### 2. Hierarchical Clustering

Builds tree of clusters (dendrogram).

```python
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

model = AgglomerativeClustering(
    n_clusters=3,
    linkage='ward'  # 'ward', 'complete', 'average', 'single'
)
labels = model.fit_predict(X)

# Visualize dendrogram
Z = linkage(X, method='ward')
dendrogram(Z)
```

**Pros:** No need to specify k, visual interpretation
**Cons:** Computationally expensive, doesn't scale well

---

#### 3. DBSCAN

Density-based clustering that finds arbitrary shapes.

```python
from sklearn.cluster import DBSCAN

model = DBSCAN(
    eps=0.5,         # Maximum distance between points
    min_samples=5    # Minimum points to form cluster
)
labels = model.fit_predict(X)
# -1 indicates noise/outliers
```

**Pros:** Finds arbitrary shapes, handles noise/outliers
**Cons:** Sensitive to parameters, struggles with varying densities

---

#### 4. Principal Component Analysis (PCA)

Dimensionality reduction by finding principal components.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)  # or n_components=0.95 for 95% variance
X_reduced = pca.fit_transform(X)

# Explained variance
explained_variance = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance)
```

**Pros:** Reduces dimensions, removes multicollinearity
**Cons:** Loses interpretability, assumes linear relationships

---

#### 5. t-SNE

Non-linear dimensionality reduction for visualization.

```python
from sklearn.manifold import TSNE

tsne = TSNE(
    n_components=2,
    perplexity=30,
    learning_rate=200,
    random_state=42
)
X_embedded = tsne.fit_transform(X)
```

**Pros:** Excellent for visualization, captures non-linear structure
**Cons:** Non-deterministic, slow, not for new data

---

### Neural Networks / Deep Learning

#### Basic Neural Network

```python
from sklearn.neural_network import MLPClassifier

model = MLPClassifier(
    hidden_layer_sizes=(100, 50),  # Two hidden layers
    activation='relu',              # 'relu', 'tanh', 'logistic'
    solver='adam',
    max_iter=500
)
model.fit(X_train, y_train)
```

#### Deep Learning with TensorFlow/Keras

```python
import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(n_features,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(n_classes, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(X_train, y_train, epochs=50, validation_split=0.2)
```

**Common Architectures:**
| Architecture | Use Case |
|-------------|----------|
| CNN (Convolutional) | Images, spatial data |
| RNN/LSTM | Sequential data, time series |
| Transformer | NLP, language models |
| GAN | Image generation |
| Autoencoder | Anomaly detection, compression |

---

## Model Evaluation

### Classification Metrics

```python
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_auc_score
)

# Confusion Matrix
#                 Predicted
#              |  Pos  |  Neg  |
#    Actual Pos|  TP   |  FN   |
#    Actual Neg|  FP   |  TN   |

y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Precision: {precision_score(y_test, y_pred)}")
print(f"Recall: {recall_score(y_test, y_pred)}")
print(f"F1 Score: {f1_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))
```

| Metric    | Formula               | When to Use         |
| --------- | --------------------- | ------------------- |
| Accuracy  | (TP+TN)/(TP+TN+FP+FN) | Balanced classes    |
| Precision | TP/(TP+FP)            | Cost of FP is high  |
| Recall    | TP/(TP+FN)            | Cost of FN is high  |
| F1 Score  | 2*(P*R)/(P+R)         | Balance P & R       |
| AUC-ROC   | Area under ROC        | Overall performance |

---

### Regression Metrics

```python
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
```

| Metric | Formula           | Interpretation           |
| ------ | ----------------- | ------------------------ |
| MAE    | Σ\|y-ŷ\|/n        | Average error magnitude  |
| MSE    | Σ(y-ŷ)²/n         | Penalizes large errors   |
| RMSE   | √MSE              | Same units as target     |
| R²     | 1 - SS_res/SS_tot | Variance explained (0-1) |

---

### Cross-Validation

```python
from sklearn.model_selection import cross_val_score, KFold

# K-Fold Cross-Validation
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')

print(f"Mean: {scores.mean():.4f} (+/- {scores.std()*2:.4f})")

# Stratified K-Fold (for imbalanced data)
from sklearn.model_selection import StratifiedKFold
skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
```

---

### Hyperparameter Tuning

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

# Grid Search
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [5, 10, 15],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
    estimator=RandomForestClassifier(),
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid_search.fit(X_train, y_train)

print(f"Best params: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_}")

# Random Search (faster for large param spaces)
from scipy.stats import randint, uniform

param_dist = {
    'n_estimators': randint(50, 500),
    'max_depth': randint(3, 20),
    'min_samples_split': randint(2, 20)
}

random_search = RandomizedSearchCV(
    estimator=RandomForestClassifier(),
    param_distributions=param_dist,
    n_iter=100,
    cv=5,
    random_state=42
)
```

---

## Best Practices

### 1. Data Preprocessing Checklist

```python
# 1. Handle missing values
df.fillna(df.mean(), inplace=True)  # or dropna, interpolate

# 2. Remove duplicates
df.drop_duplicates(inplace=True)

# 3. Handle outliers
Q1, Q3 = df['col'].quantile([0.25, 0.75])
IQR = Q3 - Q1
df = df[(df['col'] >= Q1-1.5*IQR) & (df['col'] <= Q3+1.5*IQR)]

# 4. Encode categorical variables
df = pd.get_dummies(df, columns=['categorical_col'])

# 5. Scale numerical features
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### 2. Algorithm Selection Guide

```
Start Here
    │
    ├── Is the data labeled?
    │   ├── Yes → Supervised Learning
    │   │   ├── Predicting categories? → Classification
    │   │   │   ├── <100K samples? → Try SVM, Logistic Regression
    │   │   │   └── >100K samples? → Try Random Forest, XGBoost
    │   │   └── Predicting numbers? → Regression
    │   │       ├── Linear relationship? → Linear Regression
    │   │       └── Non-linear? → Random Forest, Gradient Boosting
    │   │
    │   └── No → Unsupervised Learning
    │       ├── Finding groups? → Clustering
    │       │   ├── Know number of groups? → K-Means
    │       │   └── Don't know? → DBSCAN, Hierarchical
    │       └── Reducing dimensions? → PCA, t-SNE
    │
    └── Learning from feedback? → Reinforcement Learning
```

### 3. Common Pitfalls to Avoid

| Pitfall                            | Solution                             |
| ---------------------------------- | ------------------------------------ |
| Data leakage                       | Split before any preprocessing       |
| Not scaling features               | Use StandardScaler/MinMaxScaler      |
| Ignoring class imbalance           | Use SMOTE, class weights             |
| Overfitting                        | Use regularization, cross-validation |
| Using accuracy for imbalanced data | Use F1, AUC-ROC instead              |
| Not setting random seeds           | Set random_state for reproducibility |

### 4. Model Deployment Considerations

```python
# Save model
import joblib
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Load model
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# Create prediction pipeline
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier())
])
pipeline.fit(X_train, y_train)
joblib.dump(pipeline, 'full_pipeline.pkl')
```

---

## Quick Reference: Sklearn API Pattern

```python
from sklearn.some_module import SomeModel

# 1. Create model instance
model = SomeModel(hyperparameter=value)

# 2. Fit model to training data
model.fit(X_train, y_train)

# 3. Make predictions
predictions = model.predict(X_test)

# 4. Evaluate
score = model.score(X_test, y_test)

# 5. Access learned parameters
params = model.get_params()
```

---

## Resources for Further Learning

- **Books:** "Hands-On Machine Learning" by Aurélien Géron
- **Courses:** Andrew Ng's Machine Learning (Coursera)
- **Documentation:** scikit-learn.org, tensorflow.org
- **Practice:** Kaggle competitions

---

_Last updated: 2024_
