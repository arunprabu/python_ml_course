# Comprehensive Scikit-Learn Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Installation & Setup](#installation--setup)
3. [Core API Pattern](#core-api-pattern)
4. [Data Loading & Datasets](#data-loading--datasets)
5. [Data Preprocessing](#data-preprocessing)
6. [Supervised Learning Examples](#supervised-learning-examples)
7. [Unsupervised Learning Examples](#unsupervised-learning-examples)
8. [Model Selection & Evaluation](#model-selection--evaluation)
9. [Pipelines](#pipelines)
10. [Model Persistence](#model-persistence)

---

## Introduction

Scikit-learn is the most popular Python library for machine learning. It provides:

- Simple and efficient tools for data analysis
- Consistent API across all algorithms
- Built on NumPy, SciPy, and Matplotlib

### Key Design Principles

- **Consistency**: All objects share a consistent interface
- **Inspection**: All parameters are exposed as public attributes
- **Non-proliferation**: Limited object hierarchy
- **Composition**: Many tasks can be expressed as pipelines
- **Sensible Defaults**: Most parameters have reasonable default values

---

## Installation & Setup

```bash
# Install scikit-learn
pip install scikit-learn

# Install with common dependencies
pip install scikit-learn numpy pandas matplotlib seaborn
```

```python
# Standard imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

# Check version
import sklearn
print(sklearn.__version__)
```

---

## Core API Pattern

Every scikit-learn estimator follows the same pattern:

```python
from sklearn.module import EstimatorClass

# 1. Instantiate with hyperparameters
estimator = EstimatorClass(param1=value1, param2=value2)

# 2. Fit to data
estimator.fit(X_train, y_train)  # Supervised
estimator.fit(X)                  # Unsupervised

# 3. Transform or Predict
X_new = estimator.transform(X)    # Transformers
y_pred = estimator.predict(X)     # Predictors
y_prob = estimator.predict_proba(X)  # Classification probabilities

# 4. Fit and Transform in one step
X_new = estimator.fit_transform(X)

# 5. Evaluate
score = estimator.score(X_test, y_test)

# 6. Access learned attributes (end with underscore)
estimator.coef_          # Learned coefficients
estimator.feature_importances_  # Feature importance
estimator.labels_        # Cluster labels
```

### Estimator Types

| Type        | Methods                               | Example                 |
| ----------- | ------------------------------------- | ----------------------- |
| Estimator   | `fit()`                               | All models              |
| Predictor   | `predict()`, `score()`                | Classifiers, Regressors |
| Transformer | `transform()`, `fit_transform()`      | Scalers, PCA            |
| Model       | `predict()`, `score()`, `transform()` | Some have all           |

---

## Data Loading & Datasets

### Built-in Toy Datasets

```python
from sklearn import datasets

# Classification datasets
iris = datasets.load_iris()          # 150 samples, 4 features, 3 classes
digits = datasets.load_digits()      # 1797 samples, 64 features, 10 classes
wine = datasets.load_wine()          # 178 samples, 13 features, 3 classes
breast_cancer = datasets.load_breast_cancer()  # 569 samples, 30 features, 2 classes

# Regression datasets
boston = datasets.load_boston()      # 506 samples, 13 features (deprecated)
diabetes = datasets.load_diabetes()  # 442 samples, 10 features
california = datasets.fetch_california_housing()  # 20640 samples

# Accessing data
X = iris.data           # Feature matrix (numpy array)
y = iris.target         # Target vector
feature_names = iris.feature_names
target_names = iris.target_names

print(f"Shape: {X.shape}")
print(f"Features: {feature_names}")
print(f"Classes: {target_names}")
```

### Generated Datasets

```python
from sklearn.datasets import (
    make_classification,
    make_regression,
    make_blobs,
    make_moons,
    make_circles
)

# Classification with customizable parameters
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    n_classes=2,
    random_state=42
)

# Regression
X, y = make_regression(
    n_samples=1000,
    n_features=10,
    noise=0.1,
    random_state=42
)

# Clustering - Gaussian blobs
X, y = make_blobs(
    n_samples=300,
    centers=3,
    cluster_std=0.5,
    random_state=42
)

# Non-linear shapes for clustering
X, y = make_moons(n_samples=200, noise=0.1)
X, y = make_circles(n_samples=200, noise=0.1, factor=0.5)
```

### Loading External Data

```python
import pandas as pd
from sklearn.model_selection import train_test_split

# From CSV
df = pd.read_csv('data.csv')
X = df.drop('target', axis=1).values
y = df['target'].values

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y  # Maintain class distribution
)
```

---

## Data Preprocessing

### Handling Missing Values

```python
from sklearn.impute import SimpleImputer, KNNImputer

# Simple imputation
imputer = SimpleImputer(strategy='mean')  # 'median', 'most_frequent', 'constant'
X_imputed = imputer.fit_transform(X)

# KNN imputation
knn_imputer = KNNImputer(n_neighbors=5)
X_imputed = knn_imputer.fit_transform(X)

# Example
X = np.array([[1, 2, np.nan],
              [3, np.nan, 4],
              [5, 6, 7]])

imputer = SimpleImputer(strategy='mean')
print(imputer.fit_transform(X))
# [[1.  2.  5.5]
#  [3.  4.  4. ]
#  [5.  6.  7. ]]
```

### Feature Scaling

```python
from sklearn.preprocessing import (
    StandardScaler,
    MinMaxScaler,
    RobustScaler,
    Normalizer
)

# Standardization: mean=0, std=1
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Use same transformation!

# Min-Max Scaling: [0, 1] range
scaler = MinMaxScaler(feature_range=(0, 1))
X_scaled = scaler.fit_transform(X)

# Robust Scaler: Uses median and IQR, robust to outliers
scaler = RobustScaler()
X_scaled = scaler.fit_transform(X)

# Normalizer: Unit norm (L1 or L2)
normalizer = Normalizer(norm='l2')
X_normalized = normalizer.fit_transform(X)

# Example comparison
from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)

print("Original:", X[:3, 0])
print("Standard:", StandardScaler().fit_transform(X)[:3, 0])
print("MinMax:", MinMaxScaler().fit_transform(X)[:3, 0])
```

### Encoding Categorical Variables

```python
from sklearn.preprocessing import (
    LabelEncoder,
    OrdinalEncoder,
    OneHotEncoder
)

# Label Encoding: For target variable
le = LabelEncoder()
y_encoded = le.fit_transform(['cat', 'dog', 'bird', 'cat'])
print(y_encoded)  # [1, 2, 0, 1]
print(le.inverse_transform([0, 1, 2]))  # ['bird', 'cat', 'dog']

# Ordinal Encoding: For ordinal features
oe = OrdinalEncoder(categories=[['low', 'medium', 'high']])
X_encoded = oe.fit_transform([['low'], ['high'], ['medium']])
print(X_encoded)  # [[0.], [2.], [1.]]

# One-Hot Encoding: For nominal features
ohe = OneHotEncoder(sparse_output=False, drop='first')  # drop to avoid multicollinearity
X = [['red'], ['blue'], ['green'], ['red']]
X_encoded = ohe.fit_transform(X)
print(X_encoded)
# [[0. 1.]
#  [1. 0.]
#  [0. 0.]
#  [0. 1.]]
```

### Feature Transformation

```python
from sklearn.preprocessing import (
    PolynomialFeatures,
    FunctionTransformer,
    PowerTransformer
)

# Polynomial Features
poly = PolynomialFeatures(degree=2, include_bias=False)
X = np.array([[2, 3]])
X_poly = poly.fit_transform(X)
print(X_poly)  # [[2. 3. 4. 6. 9.]] -> [x1, x2, x1², x1*x2, x2²]

# Custom transformation
log_transformer = FunctionTransformer(np.log1p)  # log(1+x)
X_log = log_transformer.fit_transform(X)

# Power Transformer (for normalizing skewed data)
pt = PowerTransformer(method='yeo-johnson')
X_transformed = pt.fit_transform(X)
```

### Feature Selection

```python
from sklearn.feature_selection import (
    SelectKBest,
    SelectPercentile,
    RFE,
    SelectFromModel,
    chi2,
    f_classif,
    mutual_info_classif
)
from sklearn.ensemble import RandomForestClassifier

# Select K Best features
selector = SelectKBest(score_func=f_classif, k=5)
X_selected = selector.fit_transform(X, y)
selected_features = selector.get_support(indices=True)

# Select top percentile
selector = SelectPercentile(score_func=chi2, percentile=50)
X_selected = selector.fit_transform(X, y)

# Recursive Feature Elimination
rfe = RFE(estimator=RandomForestClassifier(), n_features_to_select=5)
X_selected = rfe.fit_transform(X, y)
print(rfe.ranking_)  # Feature rankings

# Select from model (based on importance)
selector = SelectFromModel(RandomForestClassifier(), threshold='median')
X_selected = selector.fit_transform(X, y)
```

---

## Supervised Learning Examples

### Linear Regression

```python
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Generate data
X, y = make_regression(n_samples=200, n_features=1, noise=20, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate
print(f"Coefficient: {model.coef_[0]:.4f}")
print(f"Intercept: {model.intercept_:.4f}")
print(f"R² Score: {r2_score(y_test, y_pred):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")

# Visualization
plt.scatter(X_test, y_test, alpha=0.5, label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.legend()
plt.title('Linear Regression')
plt.show()
```

### Ridge and Lasso Regression

```python
from sklearn.linear_model import Ridge, Lasso, ElasticNet

# Ridge (L2 regularization)
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)

# Lasso (L1 regularization - can zero out coefficients)
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

# ElasticNet (L1 + L2)
elastic = ElasticNet(alpha=0.1, l1_ratio=0.5)  # l1_ratio: mix of L1/L2
elastic.fit(X_train, y_train)

# Compare coefficients
print(f"Ridge coefficients: {ridge.coef_}")
print(f"Lasso coefficients: {lasso.coef_}")
print(f"ElasticNet coefficients: {elastic.coef_}")
```

### Logistic Regression

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load data
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(
    C=1.0,              # Inverse of regularization strength
    penalty='l2',       # 'l1', 'l2', 'elasticnet', 'none'
    solver='lbfgs',     # 'newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'
    max_iter=200,
    multi_class='auto'  # 'auto', 'ovr', 'multinomial'
)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)  # Probability for each class

# Evaluate
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=load_iris().target_names))

# Coefficients
print(f"\nCoefficients shape: {model.coef_.shape}")
print(f"Classes: {model.classes_}")
```

### Decision Tree

```python
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, plot_tree
from sklearn.datasets import load_iris

# Load data
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train classifier
clf = DecisionTreeClassifier(
    criterion='gini',      # 'gini' or 'entropy'
    max_depth=4,           # Maximum depth of tree
    min_samples_split=2,   # Min samples to split node
    min_samples_leaf=1,    # Min samples in leaf
    max_features=None,     # Number of features to consider
    random_state=42
)
clf.fit(X_train, y_train)

# Predictions and evaluation
y_pred = clf.predict(X_test)
print(f"Accuracy: {clf.score(X_test, y_test):.4f}")

# Feature importance
feature_importance = pd.DataFrame({
    'feature': load_iris().feature_names,
    'importance': clf.feature_importances_
}).sort_values('importance', ascending=False)
print(feature_importance)

# Visualize tree
plt.figure(figsize=(20, 10))
plot_tree(clf,
          feature_names=load_iris().feature_names,
          class_names=load_iris().target_names,
          filled=True,
          rounded=True)
plt.title('Decision Tree')
plt.show()
```

### Random Forest

```python
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

# Train model
rf = RandomForestClassifier(
    n_estimators=100,      # Number of trees
    criterion='gini',
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    max_features='sqrt',   # 'sqrt', 'log2', None, int, float
    bootstrap=True,        # Whether to use bootstrap samples
    oob_score=True,        # Use out-of-bag samples for scoring
    n_jobs=-1,             # Use all CPU cores
    random_state=42
)
rf.fit(X_train, y_train)

# Predictions
y_pred = rf.predict(X_test)
print(f"Accuracy: {rf.score(X_test, y_test):.4f}")
print(f"OOB Score: {rf.oob_score_:.4f}")

# Feature importance
importances = rf.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(10, 6))
plt.title("Feature Importances")
plt.bar(range(X.shape[1]), importances[indices])
plt.xticks(range(X.shape[1]), np.array(load_iris().feature_names)[indices], rotation=45)
plt.tight_layout()
plt.show()
```

### Gradient Boosting

```python
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor

# Train model
gb = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,     # Shrinks contribution of each tree
    max_depth=3,
    subsample=0.8,         # Fraction of samples for each tree
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=42
)
gb.fit(X_train, y_train)

# Staged predictions (see performance at each stage)
staged_scores = []
for i, y_pred in enumerate(gb.staged_predict(X_test)):
    staged_scores.append(accuracy_score(y_test, y_pred))

plt.plot(range(1, 101), staged_scores)
plt.xlabel('Number of Trees')
plt.ylabel('Accuracy')
plt.title('Gradient Boosting: Staged Performance')
plt.show()
```

### Support Vector Machine (SVM)

```python
from sklearn.svm import SVC, SVR
from sklearn.preprocessing import StandardScaler

# SVM requires scaling!
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train classifier
svm = SVC(
    C=1.0,                 # Regularization parameter
    kernel='rbf',          # 'linear', 'poly', 'rbf', 'sigmoid'
    gamma='scale',         # Kernel coefficient
    degree=3,              # Degree for poly kernel
    probability=True,      # Enable probability estimates
    random_state=42
)
svm.fit(X_train_scaled, y_train)

# Predictions
y_pred = svm.predict(X_test_scaled)
y_proba = svm.predict_proba(X_test_scaled)  # Only if probability=True

print(f"Accuracy: {svm.score(X_test_scaled, y_test):.4f}")
print(f"Support vectors per class: {svm.n_support_}")

# Decision function (distance to hyperplane)
decision = svm.decision_function(X_test_scaled)
```

### K-Nearest Neighbors

```python
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor

# Train model
knn = KNeighborsClassifier(
    n_neighbors=5,
    weights='uniform',     # 'uniform' or 'distance'
    algorithm='auto',      # 'auto', 'ball_tree', 'kd_tree', 'brute'
    metric='minkowski',    # Distance metric
    p=2                    # Power parameter (1=manhattan, 2=euclidean)
)
knn.fit(X_train_scaled, y_train)

# Predictions
y_pred = knn.predict(X_test_scaled)
print(f"Accuracy: {knn.score(X_test_scaled, y_test):.4f}")

# Find k nearest neighbors
distances, indices = knn.kneighbors(X_test_scaled[:1])
print(f"Nearest neighbors indices: {indices}")
print(f"Distances: {distances}")

# Finding optimal K
k_range = range(1, 31)
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    scores.append(knn.score(X_test_scaled, y_test))

plt.plot(k_range, scores)
plt.xlabel('K')
plt.ylabel('Accuracy')
plt.title('KNN: Finding Optimal K')
plt.show()
```

### Naive Bayes

```python
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

# Gaussian Naive Bayes (continuous features)
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)
print(f"GaussianNB Accuracy: {gnb.score(X_test, y_test):.4f}")

# For text classification (word counts)
from sklearn.feature_extraction.text import CountVectorizer

texts = ["hello world", "world of python", "hello python"]
labels = [0, 1, 0]

vectorizer = CountVectorizer()
X_counts = vectorizer.fit_transform(texts)

mnb = MultinomialNB()
mnb.fit(X_counts, labels)

# Predict new text
new_text = vectorizer.transform(["hello python world"])
prediction = mnb.predict(new_text)
```

### Neural Network (Multi-layer Perceptron)

```python
from sklearn.neural_network import MLPClassifier, MLPRegressor

# Train model
mlp = MLPClassifier(
    hidden_layer_sizes=(100, 50),  # Two hidden layers
    activation='relu',      # 'identity', 'logistic', 'tanh', 'relu'
    solver='adam',          # 'lbfgs', 'sgd', 'adam'
    alpha=0.0001,          # L2 regularization
    batch_size='auto',
    learning_rate='adaptive',  # 'constant', 'invscaling', 'adaptive'
    learning_rate_init=0.001,
    max_iter=500,
    early_stopping=True,
    validation_fraction=0.1,
    random_state=42
)
mlp.fit(X_train_scaled, y_train)

# Predictions
y_pred = mlp.predict(X_test_scaled)
print(f"Accuracy: {mlp.score(X_test_scaled, y_test):.4f}")
print(f"Number of iterations: {mlp.n_iter_}")
print(f"Loss: {mlp.loss_:.4f}")

# Plot loss curve
plt.plot(mlp.loss_curve_)
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.title('MLP Training Loss')
plt.show()
```

---

## Unsupervised Learning Examples

### K-Means Clustering

```python
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

# Generate data
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=42)

# Train model
kmeans = KMeans(
    n_clusters=4,
    init='k-means++',      # 'k-means++' or 'random'
    n_init=10,             # Number of initializations
    max_iter=300,
    tol=1e-4,
    random_state=42
)
kmeans.fit(X)

# Results
labels = kmeans.labels_           # Cluster assignments
centroids = kmeans.cluster_centers_
inertia = kmeans.inertia_         # Sum of squared distances to centroids

print(f"Cluster labels: {np.unique(labels)}")
print(f"Silhouette Score: {silhouette_score(X, labels):.4f}")

# Elbow Method for optimal K
inertias = []
silhouettes = []
K_range = range(2, 11)

for k in K_range:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X)
    inertias.append(km.inertia_)
    silhouettes.append(silhouette_score(X, km.labels_))

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(K_range, inertias, 'bo-')
axes[0].set_xlabel('K')
axes[0].set_ylabel('Inertia')
axes[0].set_title('Elbow Method')

axes[1].plot(K_range, silhouettes, 'ro-')
axes[1].set_xlabel('K')
axes[1].set_ylabel('Silhouette Score')
axes[1].set_title('Silhouette Analysis')
plt.show()

# Visualize clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200)
plt.title('K-Means Clustering')
plt.show()
```

### Hierarchical Clustering

```python
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Train model
agg = AgglomerativeClustering(
    n_clusters=4,
    metric='euclidean',
    linkage='ward'         # 'ward', 'complete', 'average', 'single'
)
labels = agg.fit_predict(X)

print(f"Cluster labels: {np.unique(labels)}")

# Create dendrogram
Z = linkage(X, method='ward')
plt.figure(figsize=(12, 6))
dendrogram(Z, truncate_mode='level', p=5)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample index')
plt.ylabel('Distance')
plt.show()
```

### DBSCAN

```python
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons

# Generate non-linear data
X, y_true = make_moons(n_samples=200, noise=0.05, random_state=42)

# Train model
dbscan = DBSCAN(
    eps=0.2,               # Maximum distance between points in cluster
    min_samples=5,         # Minimum points to form a cluster
    metric='euclidean'
)
labels = dbscan.fit_predict(X)

# Results
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)

print(f"Number of clusters: {n_clusters}")
print(f"Number of noise points: {n_noise}")

# Visualize
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.title(f'DBSCAN: {n_clusters} clusters, {n_noise} noise points')
plt.show()
```

### Principal Component Analysis (PCA)

```python
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits

# Load high-dimensional data
digits = load_digits()
X = digits.data
y = digits.target
print(f"Original shape: {X.shape}")  # (1797, 64)

# Fit PCA
pca = PCA(n_components=0.95)  # Keep 95% variance
X_reduced = pca.fit_transform(X)

print(f"Reduced shape: {X_reduced.shape}")
print(f"Number of components: {pca.n_components_}")
print(f"Explained variance ratio: {pca.explained_variance_ratio_.sum():.4f}")

# Plot explained variance
pca_full = PCA()
pca_full.fit(X)
cumsum = np.cumsum(pca_full.explained_variance_ratio_)

plt.plot(cumsum)
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.axhline(y=0.95, color='r', linestyle='--', label='95% variance')
plt.legend()
plt.title('PCA: Explained Variance')
plt.show()

# Visualize in 2D
pca_2d = PCA(n_components=2)
X_2d = pca_2d.fit_transform(X)

plt.scatter(X_2d[:, 0], X_2d[:, 1], c=y, cmap='tab10', alpha=0.5)
plt.colorbar()
plt.title('Digits Dataset: PCA 2D Projection')
plt.show()
```

### t-SNE

```python
from sklearn.manifold import TSNE

# t-SNE for visualization
tsne = TSNE(
    n_components=2,
    perplexity=30,         # Balance between local and global structure
    learning_rate='auto',
    n_iter=1000,
    random_state=42
)
X_tsne = tsne.fit_transform(X)

plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='tab10', alpha=0.5)
plt.colorbar(scatter)
plt.title('Digits Dataset: t-SNE Visualization')
plt.show()
```

---

## Model Selection & Evaluation

### Train-Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,         # 20% for testing
    random_state=42,       # Reproducibility
    stratify=y,            # Maintain class distribution
    shuffle=True
)
```

### Cross-Validation

```python
from sklearn.model_selection import (
    cross_val_score,
    cross_val_predict,
    KFold,
    StratifiedKFold,
    LeaveOneOut
)

# Basic cross-validation
scores = cross_val_score(
    estimator=RandomForestClassifier(),
    X=X, y=y,
    cv=5,                  # Number of folds
    scoring='accuracy',    # Scoring metric
    n_jobs=-1
)
print(f"CV Scores: {scores}")
print(f"Mean: {scores.mean():.4f} (+/- {scores.std()*2:.4f})")

# Get predictions from cross-validation
y_pred_cv = cross_val_predict(RandomForestClassifier(), X, y, cv=5)

# Custom cross-validation
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
for train_idx, val_idx in kfold.split(X):
    X_train_fold, X_val_fold = X[train_idx], X[val_idx]
    y_train_fold, y_val_fold = y[train_idx], y[val_idx]
    # Train and evaluate...

# Stratified K-Fold (for imbalanced data)
skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skfold)
```

### Classification Metrics

```python
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_auc_score,
    roc_curve,
    precision_recall_curve
)

# Basic metrics
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]  # For binary

print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred, average='weighted'):.4f}")
print(f"Recall: {recall_score(y_test, y_pred, average='weighted'):.4f}")
print(f"F1: {f1_score(y_test, y_pred, average='weighted'):.4f}")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Detailed report
print(classification_report(y_test, y_pred))

# ROC Curve (binary classification)
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
auc = roc_auc_score(y_test, y_proba)

plt.plot(fpr, tpr, label=f'ROC Curve (AUC = {auc:.4f})')
plt.plot([0, 1], [0, 1], 'k--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()

# Precision-Recall Curve
precision, recall, thresholds = precision_recall_curve(y_test, y_proba)
plt.plot(recall, precision)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.show()
```

### Regression Metrics

```python
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    mean_absolute_percentage_error
)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred)

print(f"MAE: {mae:.4f}")
print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²: {r2:.4f}")
print(f"MAPE: {mape:.4f}")
```

### Hyperparameter Tuning

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from scipy.stats import randint, uniform

# Grid Search - exhaustive search
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=1,
    return_train_score=True
)
grid_search.fit(X_train, y_train)

print(f"Best parameters: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_:.4f}")
best_model = grid_search.best_estimator_

# Random Search - faster for large param spaces
param_dist = {
    'n_estimators': randint(50, 500),
    'max_depth': randint(3, 20),
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 10),
    'max_features': uniform(0.1, 0.9)
}

random_search = RandomizedSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_distributions=param_dist,
    n_iter=100,            # Number of random combinations
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    random_state=42
)
random_search.fit(X_train, y_train)

print(f"Best parameters: {random_search.best_params_}")
print(f"Best score: {random_search.best_score_:.4f}")

# View all results
results_df = pd.DataFrame(grid_search.cv_results_)
print(results_df[['params', 'mean_test_score', 'std_test_score']].head(10))
```

---

## Pipelines

### Basic Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC

# Create pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=10)),
    ('classifier', SVC(kernel='rbf'))
])

# Fit and predict
pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)
score = pipe.score(X_test, y_test)

print(f"Pipeline accuracy: {score:.4f}")

# Access individual steps
scaler = pipe.named_steps['scaler']
print(f"Scaler mean: {scaler.mean_[:5]}")
```

### Column Transformer for Mixed Data

```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

# Example with mixed data types
numeric_features = ['age', 'income']
categorical_features = ['gender', 'occupation']

# Preprocessing for numeric data
numeric_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Preprocessing for categorical data
categorical_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combine transformers
preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numeric_features),
    ('cat', categorical_transformer, categorical_features)
])

# Full pipeline
full_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier())
])

# Use the pipeline
full_pipeline.fit(X_train, y_train)
y_pred = full_pipeline.predict(X_test)
```

### Pipeline with Grid Search

```python
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA()),
    ('classifier', SVC())
])

# Parameter names: step__parameter
param_grid = {
    'pca__n_components': [5, 10, 15],
    'classifier__C': [0.1, 1, 10],
    'classifier__kernel': ['linear', 'rbf']
}

grid_search = GridSearchCV(pipe, param_grid, cv=5)
grid_search.fit(X_train, y_train)

print(f"Best parameters: {grid_search.best_params_}")
```

### Feature Union

```python
from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest

# Combine multiple feature extraction methods
combined_features = FeatureUnion([
    ('pca', PCA(n_components=5)),
    ('select_best', SelectKBest(k=5))
])

# Use in pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('features', combined_features),
    ('classifier', RandomForestClassifier())
])

pipe.fit(X_train, y_train)
```

---

## Model Persistence

### Save and Load Models

```python
import joblib
import pickle

# Method 1: joblib (recommended for large numpy arrays)
joblib.dump(model, 'model.joblib')
loaded_model = joblib.load('model.joblib')

# Method 2: pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Save entire pipeline
joblib.dump(full_pipeline, 'pipeline.joblib')

# Verify loaded model works
y_pred = loaded_model.predict(X_test)
print(f"Loaded model accuracy: {accuracy_score(y_test, y_pred):.4f}")
```

### Save with Compression

```python
# Compress large models
joblib.dump(model, 'model.joblib.gz', compress=3)
loaded_model = joblib.load('model.joblib.gz')
```

---

## Quick Reference Cheat Sheet

### Import Patterns

```python
# Data
from sklearn.datasets import load_iris, make_classification
from sklearn.model_selection import train_test_split

# Preprocessing
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

# Models
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA

# Evaluation
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_val_score, GridSearchCV

# Pipeline
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
```

### Common Scoring Parameters

| Task           | Scoring String                                            |
| -------------- | --------------------------------------------------------- |
| Classification | 'accuracy', 'precision', 'recall', 'f1', 'roc_auc'        |
| Regression     | 'r2', 'neg_mean_squared_error', 'neg_mean_absolute_error' |
| Clustering     | 'silhouette_score'                                        |

### Useful Attributes (end with `_`)

| Attribute              | Model Type    | Description          |
| ---------------------- | ------------- | -------------------- |
| `coef_`                | Linear models | Coefficients         |
| `intercept_`           | Linear models | Intercept            |
| `feature_importances_` | Tree models   | Feature importance   |
| `classes_`             | Classifiers   | Class labels         |
| `n_iter_`              | Iterative     | Number of iterations |
| `labels_`              | Clustering    | Cluster labels       |
| `cluster_centers_`     | K-Means       | Centroids            |
| `components_`          | PCA           | Principal components |

---

_Last updated: 2024_
