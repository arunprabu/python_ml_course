# Machine Learning Model Cheat Sheet

| Category           | Model / Algorithm               | Python class                    | What it does                             | Good use case                        |
| ------------------ | ------------------------------- | ------------------------------- | ---------------------------------------- | ------------------------------------ |
| **Classification** | Logistic Regression             | `LogisticRegression`            | Predicts classes                         | Spam / not spam                      |
| Classification     | K-Nearest Neighbors             | `KNeighborsClassifier`          | Classifies based on nearby examples      | Small datasets                       |
| Classification     | Decision Tree                   | `DecisionTreeClassifier`        | Uses decision rules                      | Loan approval                        |
| Classification     | Random Forest                   | `RandomForestClassifier`        | Combines many decision trees             | General-purpose classification       |
| Classification     | Extra Trees                     | `ExtraTreesClassifier`          | Randomized tree ensemble                 | Tabular data                         |
| Classification     | Gradient Boosting               | `GradientBoostingClassifier`    | Builds trees sequentially                | Structured/tabular data              |
| Classification     | Random Forest                   | `RandomForestClassifier`        | Ensemble of trees                        | Fraud/churn                          |
| Classification     | Support Vector Machine          | `SVC`                           | Finds class boundaries                   | Small/medium datasets                |
| Classification     | Naive Bayes                     | `GaussianNB`                    | Probabilistic classification             | Simple classification                |
| Classification     | Multinomial Naive Bayes         | `MultinomialNB`                 | Probability-based classifier             | Text/spam                            |
| Classification     | Linear Discriminant Analysis    | `LinearDiscriminantAnalysis`    | Separates classes                        | Classification with numeric features |
| Classification     | Quadratic Discriminant Analysis | `QuadraticDiscriminantAnalysis` | Nonlinear class separation               | Small datasets                       |
| Classification     | Neural Network                  | `MLPClassifier`                 | Learns complex patterns                  | Nonlinear classification             |
| Classification     | XGBoost                         | `XGBClassifier`                 | Boosted decision trees                   | High-performance tabular ML          |
| Classification     | LightGBM                        | `LGBMClassifier`                | Fast gradient boosting                   | Large tabular data                   |
| Classification     | CatBoost                        | `CatBoostClassifier`            | Boosting with strong categorical support | Categorical data                     |

# Regression

Regression means predicting a numerical value.

| Category       | Model / Algorithm         | Python class                              | What it does                          | Good use case                   |
| -------------- | ------------------------- | ----------------------------------------- | ------------------------------------- | ------------------------------- |
| **Regression** | Linear Regression         | `LinearRegression`                        | Fits a straight-line relationship     | House prices                    |
| Regression     | Ridge Regression          | `Ridge`                                   | Linear regression + regularization    | Many correlated features        |
| Regression     | Lasso Regression          | `Lasso`                                   | Linear regression + feature selection | High-dimensional data           |
| Regression     | Elastic Net               | `ElasticNet`                              | Ridge + Lasso combination             | Many features                   |
| Regression     | Polynomial Regression     | `PolynomialFeatures` + `LinearRegression` | Captures curved relationships         | Nonlinear numeric relationships |
| Regression     | Decision Tree             | `DecisionTreeRegressor`                   | Tree-based prediction                 | Tabular data                    |
| Regression     | Random Forest             | `RandomForestRegressor`                   | Many regression trees                 | General-purpose regression      |
| Regression     | Extra Trees               | `ExtraTreesRegressor`                     | Randomized tree ensemble              | Tabular data                    |
| Regression     | Gradient Boosting         | `GradientBoostingRegressor`               | Sequentially improves trees           | Structured data                 |
| Regression     | Random Forest             | `RandomForestRegressor`                   | Ensemble of trees                     | Price/sales prediction          |
| Regression     | Support Vector Regression | `SVR`                                     | SVM for numerical prediction          | Small/medium datasets           |
| Regression     | KNN Regression            | `KNeighborsRegressor`                     | Uses nearby observations              | Small datasets                  |
| Regression     | XGBoost                   | `XGBRegressor`                            | Boosted trees                         | High-performance tabular data   |
| Regression     | LightGBM                  | `LGBMRegressor`                           | Fast boosted trees                    | Large datasets                  |
| Regression     | CatBoost                  | `CatBoostRegressor`                       | Categorical-friendly boosting         | Business/tabular data           |
| Regression     | Neural Network            | `MLPRegressor`                            | Learns complex relationships          | Complex nonlinear problems      |

# Clustering

Clustering is different because you don't have a target y.

For example:

```
    Customer data
     	 ↓
      K-Means
     	 ↓
┌────────┼────────────────┐
↓        ↓                ↓
Group 1  Group 2       Group 3
```

| Category       | Model / Algorithm        | Python class              | Good use case                 |
| -------------- | ------------------------ | ------------------------- | ----------------------------- |
| **Clustering** | K-Means                  | `KMeans`                  | Customer segmentation         |
| Clustering     | Mini-Batch K-Means       | `MiniBatchKMeans`         | Very large datasets           |
| Clustering     | DBSCAN                   | `DBSCAN`                  | Spatial/density-based groups  |
| Clustering     | HDBSCAN                  | `HDBSCAN`                 | Clusters with varying density |
| Clustering     | Agglomerative Clustering | `AgglomerativeClustering` | Hierarchical groups           |
| Clustering     | Spectral Clustering      | `SpectralClustering`      | Complex cluster shapes        |
| Clustering     | Gaussian Mixture         | `GaussianMixture`         | Probabilistic clustering      |
| Clustering     | Birch                    | `Birch`                   | Large datasets                |

# Anomaly / Outlier Detection

These models try to answer:

"Which observations look unusual?"

| Category              | Model / Algorithm    | Python class         | Good use case               |
| --------------------- | -------------------- | -------------------- | --------------------------- |
| **Anomaly Detection** | Isolation Forest     | `IsolationForest`    | Fraud detection             |
| Anomaly Detection     | One-Class SVM        | `OneClassSVM`        | Detect unusual observations |
| Anomaly Detection     | Local Outlier Factor | `LocalOutlierFactor` | Local outliers              |
| Anomaly Detection     | Elliptic Envelope    | `EllipticEnvelope`   | Gaussian-like data          |
| Anomaly Detection     | Autoencoder          | Neural network       | Complex anomaly detection   |

# Dimensionality Reduction

Suppose you have:

```
	500 features
		↓
	   PCA
		↓
	20 features
```

The goal is to reduce the number of features while retaining useful information.

| Category                     | Model / Algorithm | Python class                | Good use case                            |
| ---------------------------- | ----------------- | --------------------------- | ---------------------------------------- |
| **Dimensionality Reduction** | PCA               | `PCA`                       | Reduce many features                     |
| Dimensionality Reduction     | Kernel PCA        | `KernelPCA`                 | Nonlinear dimensionality reduction       |
| Dimensionality Reduction     | Truncated SVD     | `TruncatedSVD`              | Text / sparse matrices                   |
| Dimensionality Reduction     | NMF               | `NMF`                       | Non-negative data                        |
| Dimensionality Reduction     | ICA               | `FastICA`                   | Separate independent signals             |
| Dimensionality Reduction     | LDA               | `LatentDirichletAllocation` | Topic modeling                           |
| Dimensionality Reduction     | t-SNE             | `TSNE`                      | Visualization                            |
| Dimensionality Reduction     | UMAP              | `UMAP`                      | Visualization / dimensionality reduction |

Note: LDA can mean two completely different things:

LinearDiscriminantAnalysis → classification
LatentDirichletAllocation → topic modeling

# Time-Series Models

When your data depends heavily on time, you may use specialized approaches.

| Category        | Model / Algorithm     | Common implementation  | Good use case                             |
| --------------- | --------------------- | ---------------------- | ----------------------------------------- |
| **Time Series** | AR                    | `AutoReg`              | Predict future values                     |
| Time Series     | ARIMA                 | `ARIMA`                | Forecasting                               |
| Time Series     | SARIMA                | `SARIMAX`              | Seasonal forecasting                      |
| Time Series     | Exponential Smoothing | `ExponentialSmoothing` | Sales forecasting                         |
| Time Series     | Prophet               | `Prophet`              | Business forecasting                      |
| Time Series     | LSTM                  | TensorFlow/PyTorch     | Complex sequences                         |
| Time Series     | GRU                   | TensorFlow/PyTorch     | Sequential data                           |
| Time Series     | Temporal CNN          | TensorFlow/PyTorch     | Time-dependent patterns                   |
| Time Series     | XGBoost               | `XGBRegressor`         | Forecasting with engineered time features |

# Recommendation Systems

Used when you want to answer:

"What should I recommend to this user?"

| Category           | Model / Algorithm              | Typical approach       | Good use case                  |
| ------------------ | ------------------------------ | ---------------------- | ------------------------------ |
| **Recommendation** | Collaborative Filtering        | User-item interactions | Netflix-style recommendations  |
| Recommendation     | Matrix Factorization           | SVD / ALS              | Product recommendations        |
| Recommendation     | Content-Based Filtering        | Similarity             | Similar products               |
| Recommendation     | Nearest Neighbors              | `NearestNeighbors`     | Similar items/users            |
| Recommendation     | Neural Collaborative Filtering | Neural network         | Large recommendation systems   |
| Recommendation     | Deep Learning Recommender      | TensorFlow/PyTorch     | Complex recommendation systems |

# Association Rule Learning

Used to discover:

"What things tend to occur together?"

Example:
Customers who buy:

```
	Bread + Butter
		  ↓
	   often buy
          ↓
		Milk

```

| Category        | Model / Algorithm | Common implementation   | Good use case          |
| --------------- | ----------------- | ----------------------- | ---------------------- |
| **Association** | Apriori           | `mlxtend`               | Market basket analysis |
| Association     | FP-Growth         | `mlxtend`               | Frequent itemsets      |
| Association     | Eclat             | Various implementations | Item relationships     |

# Semi-Supervised Learning

You have some labeled data + lots of unlabeled data.

```
100,000 records
       ↓
  5,000 labeled
 95,000 unlabeled
       ↓
Semi-supervised learning

```

| Category            | Model / Algorithm | Typical implementation   |
| ------------------- | ----------------- | ------------------------ |
| **Semi-Supervised** | Self Training     | `SelfTrainingClassifier` |
| Semi-Supervised     | Label Propagation | `LabelPropagation`       |
| Semi-Supervised     | Label Spreading   | `LabelSpreading`         |

# Ensemble Learning

This is a particularly important category because you'll see it everywhere.

Instead of relying on one model, combine multiple models.

| Technique             | Example              | Idea                             |
| --------------------- | -------------------- | -------------------------------- |
| **Bagging**           | Random Forest        | Train many models independently  |
| **Boosting**          | XGBoost              | Train models sequentially        |
| **Gradient Boosting** | LightGBM             | Sequentially improve predictions |
| **Stacking**          | `StackingClassifier` | Combine different model types    |
| **Voting**            | `VotingClassifier`   | Let several models vote          |
| **Blending**          | Custom ensemble      | Combine predictions              |

# The complete mental map

This is the part I'd recommend memorizing:

```
                            MACHINE LEARNING
                                   │
          ┌────────────────────────┼────────────────┐
          │                        │                │
     SUPERVISED               UNSUPERVISED         OTHER
          │                        │
      ┌───┴───┐                ┌───┴─────┐
      │       │                │         │
Classification Regression  Clustering  Anomaly
      │       │
      │       │
 Classes    Numbers
   ↓           ↓
Spam?       Price?
Yes/No      ₹50 lakh


        UNSUPERVISED / OTHER
               │
       ┌───────┼─────────┐
       ↓       ↓         ↓
 Clustering  PCA    Anomaly Detection
              │
              ↓
       Dimensionality
         Reduction


        SPECIALIZED
            │
     ┌──────┼───────────┐
     ↓      ↓           ↓
Time Series Recommendation Association

```

If you're learning ML, focus on these first

Don't try to learn every algorithm at once. I'd recommend this progression:

| Priority | Learn                            | Why                            |
| -------: | -------------------------------- | ------------------------------ |
|     ⭐ 1 | `LinearRegression`               | Understand regression          |
|     ⭐ 2 | `LogisticRegression`             | Understand classification      |
|     ⭐ 3 | `DecisionTreeClassifier`         | Understand trees               |
|     ⭐ 4 | `RandomForestClassifier`         | Understand ensembles           |
|     ⭐ 5 | `RandomForestRegressor`          | Tree-based regression          |
|     ⭐ 6 | `KMeans`                         | Understand clustering          |
|     ⭐ 7 | `SVC` / `SVR`                    | Understand SVM                 |
|     ⭐ 8 | `KNeighborsClassifier`           | Understand distance-based ML   |
|     ⭐ 9 | `XGBClassifier` / `XGBRegressor` | Learn boosting                 |
|    ⭐ 10 | `PCA`                            | Learn dimensionality reduction |
|    ⭐ 11 | `IsolationForest`                | Learn anomaly detection        |
|    ⭐ 12 | `DBSCAN`                         | Learn density-based clustering |
|    ⭐ 13 | Neural Networks                  | Move toward deep learning      |

One very important rule

Don't choose a model based only on the algorithm name.

First identify the problem:

```
What do I want to predict?
          │
          ├── Category → Classification
          │
          ├── Number → Regression
          │
          ├── Groups → Clustering
          │
          ├── Unusual points → Anomaly Detection
          │
          ├── Future values → Time Series
          │
          ├── Fewer features → Dimensionality Reduction
          │
          └── What should I recommend? → Recommendation

```

Then choose candidate models within that category and compare them using the right evaluation metric.
