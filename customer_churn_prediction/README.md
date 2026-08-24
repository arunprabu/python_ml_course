# Customer Churn ML Demo

A comprehensive machine learning pipeline for predicting customer churn in subscription-based services. This project demonstrates a complete data science workflow from raw data cleaning to feature engineering, preparing data for predictive modeling.

## 📋 Table of Contents

- [Overview](#overview)
- [Use Case](#use-case)
- [Dataset Description](#dataset-description)
- [Project Structure](#project-structure)
- [Pipeline Process](#pipeline-process)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Output Files](#output-files)
- [Feature Engineering Details](#feature-engineering-details)
- [Next Steps](#next-steps)
- [MLflow Experiment Tracking](#mlflow-experiment-tracking)

---

## 🎯 Overview

This project implements a **customer churn prediction pipeline** for a subscription-based business. Customer churn refers to when customers cancel their subscriptions or stop using a service. Understanding and predicting churn is critical for businesses to:

- Identify at-risk customers before they leave
- Implement targeted retention strategies
- Reduce revenue loss
- Improve customer lifetime value (CLV)

The pipeline processes raw customer data through systematic cleaning and feature engineering stages to create a machine learning-ready dataset.

---

## 💼 Use Case

### Business Problem

A subscription-based company (e.g., SaaS, streaming service, telecom) wants to:

1. **Predict which customers are likely to churn** (cancel their subscription)
2. **Understand the factors** that contribute to customer churn
3. **Take proactive measures** to retain high-value customers

### Solution Approach

This pipeline prepares customer data by:

- Cleaning messy real-world data (missing values, duplicates, inconsistencies)
- Engineering meaningful features that capture customer behavior patterns
- Creating risk indicators and engagement metrics
- Preparing data for machine learning models (e.g., Logistic Regression, Random Forest, XGBoost)

---

## 📊 Dataset Description

### Source Data

**File**: `data/customer_churn_raw.csv`  
**Records**: 107 customers (including 1 header row = 106 data rows)  
**Features**: 21 original columns

### Data Fields

| Category                   | Fields                                                                                                               | Description                                                                   |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Identifiers**            | `customer_id`                                                                                                        | Unique customer identifier                                                    |
| **Demographics**           | `age`, `gender`                                                                                                      | Customer demographic information                                              |
| **Subscription**           | `subscription_plan`, `tenure_months`, `contract_type`                                                                | Plan type (Basic/Standard/Premium), length of subscription, contract duration |
| **Financial**              | `monthly_charges`, `total_charges`, `payment_method`                                                                 | Revenue metrics and payment details                                           |
| **Usage & Engagement**     | `login_frequency_monthly`, `features_used`, `data_consumption_gb`, `engagement_score`, `days_since_last_activity`    | Customer activity and engagement patterns                                     |
| **Support & Satisfaction** | `billing_issues_count`, `plan_changes`, `support_tickets`, `avg_resolution_hours`, `satisfaction_score`, `nps_score` | Customer service and satisfaction metrics                                     |
| **Target Variable**        | `churned`                                                                                                            | Binary indicator (0 = Active, 1 = Churned)                                    |

### Data Quality Issues

The raw dataset intentionally contains real-world data quality problems:

- **Missing values** in multiple columns (age, gender, charges, scores)
- **Duplicate customer records**
- **Inconsistent formatting** (e.g., "Male" vs "male", "Credit Card" vs "CC")
- **Currency symbols** in numeric fields (e.g., "$29.99")
- **Outliers** (e.g., age = 150, negative charges, tenure = -10)
- **Invalid ranges** (e.g., satisfaction_score = 10.5, nps_score = -1)

---

## 📁 Project Structure

```
customer-churn-ml-demo/
│
├── data/                                    # Data directory
│   ├── customer_churn_raw.csv              # Raw input data (with quality issues)
│   ├── customer_churn_cleaned.csv          # Cleaned data (after pipeline step 1)
│   ├── customer_churn_featured.csv         # Feature-engineered data (after pipeline step 2)
│   ├── cleaning_summary.csv                # Summary of cleaning operations
│   └── feature_documentation.csv           # Catalog of all features
│
├── src/customer_churn_prediction/           # Python Scripts (Pipeline)
│   ├── 01_clean_data.py                    # Data cleaning pipeline
│   ├── 02_feature_engineering.py           # Feature engineering pipeline
│   ├── 03_exploratory_data_analysis.py     # EDA and visualization generation
│   ├── 04_model_training_eval.py           # Model training and evaluation
│   ├── 05_hyperparam_tuning.py             # Hyperparameter optimization
│   └── 06_mlflow_tracking.py               # Experiment tracking with MLflow
│
├── app/                                     # Streamlit Web Application
│   ├── streamlit_app.py                    # Main app file
│   ├── README.md                           # App documentation
│   └── QUICKSTART.md                       # Quick start guide
│
├── scripts/                                 # Utility scripts
│   └── run_app.sh                          # Launch Streamlit app
│
├── models/                                  # Trained ML models (generated)
│   └── tuned_churn_model.pkl                # Serialized trained model
│
├── visualizations/                          # Generated plots and charts
│   └── *.png                               # EDA visualizations
│
├── mlflow.db                                # MLflow run history (generated)
├── mlruns/                                  # MLflow logged models (generated)
│
├── pyproject.toml                           # Project metadata and dependencies
├── uv.lock                                  # Exact pinned versions (do not edit by hand)
└── README.md                                # This file
```

---

## 🔄 Pipeline Process

The project runs as a **Python script pipeline**.

### Pipeline Stages

The complete pipeline consists of **six stages** that can be run sequentially:

#### Stage 1: Data Cleaning

**Script**: `src/customer_churn_prediction/01_clean_data.py`

Transforms raw, messy data into a clean, validated dataset.

**Operations (in order)**:

1. **Remove Duplicates**: Identifies and removes duplicate customer records based on `customer_id`
2. **Clean Categorical Variables**: Standardizes values (e.g., "M" → "Male", "CC" → "Credit Card")
3. **Correct Data Types**: Removes currency symbols, converts strings to numeric types
4. **Handle Missing Values**: Imputes missing data (median for numeric, mode for categorical)
5. **Fix Outliers & Validate Ranges**: Clips values to valid ranges (age: 18-100, scores: 0-10)
6. **Finalize Data Types**: Converts to final int/float types after all cleaning
7. **Validate Final Data**: Ensures no missing values, duplicates, or invalid ranges remain

**Key Features**:

- Comprehensive data quality reports before and after cleaning
- Detailed logging of all cleaning operations
- Automatic validation checks
- Summary statistics saved to `cleaning_summary.csv`

#### Stage 2: Feature Engineering

**Script**: `src/customer_churn_prediction/02_feature_engineering.py`

Creates derived features that capture customer behavior patterns and risk indicators.

**Feature Categories**:

1. **Customer Value Metrics**
   - `monthly_value_ratio`: Average revenue per user (ARPU)
   - `charge_per_feature`: Cost efficiency
   - `customer_lifetime_value`: Total value for active customers
   - `value_tier`: Customer value segmentation

2. **Engagement Indicators**
   - `engagement_velocity`: Engagement per month
   - `login_intensity`: Average daily logins
   - `data_per_login`: Data consumption patterns
   - `activity_recency_category`: Customer activity status
   - `features_utilization_rate`: Feature adoption rate

3. **Support Risk Features**
   - `support_rate_annual`: Annualized support ticket rate
   - `resolution_burden`: Total time spent on support
   - `satisfaction_gap`: Distance from perfect score
   - `billing_risk_flag`: Billing issues indicator
   - `nps_category`: Net Promoter Score classification

4. **Interaction Features**
   - `plan_tenure_mismatch`: Plan-tenure fit indicator
   - `usage_plan_mismatch`: Usage-plan alignment
   - `payment_stability`: Payment reliability metric
   - `contract_value_risk`: Contract-value alignment

5. **Tenure & Lifecycle Features**
   - `lifecycle_stage`: Customer maturity stage
   - `contract_tenure_ratio`: Contract renewal cycles
   - `engagement_growth_rate`: Engagement trend
   - `tenure_stability`: Long-term stability metric

**Total Features Created**: ~35 new derived features

#### Stage 3: Exploratory Data Analysis (EDA)

**Script**: `src/customer_churn_prediction/03_exploratory_data_analysis.py`

Analyzes data patterns and generates visualizations.

**Analyses Performed**:

- Churn distribution and class balance
- Feature correlation analysis
- Top features correlated with churn
- Distribution plots for key metrics
- Categorical variable analysis

**Outputs**: PNG visualizations saved to `visualizations/` folder

#### Stage 4: Model Training & Evaluation

**Script**: `src/customer_churn_prediction/04_model_training_eval.py`

Trains and evaluates machine learning models.

**Models Trained**:

- Random Forest Classifier (primary model)
- Additional models for comparison (Logistic Regression, etc.)

**Evaluation Metrics**:

- Accuracy, Precision, Recall, F1-Score
- Confusion Matrix
- ROC-AUC Score
- Feature Importance Analysis

**Outputs**: Evaluation metrics printed to the console (the model itself is saved in Stage 5, after tuning)

#### Stage 5: Hyperparameter Tuning

**Script**: `src/customer_churn_prediction/05_hyperparam_tuning.py`

Optimizes model performance through hyperparameter tuning.

**Techniques**:

- Grid Search CV
- Randomized Search CV
- Cross-validation for model selection

**Outputs**: Best model parameters, and the tuned model saved to `models/tuned_churn_model.pkl`

#### Stage 6: Experiment Tracking with MLflow

**Script**: `src/customer_churn_prediction/06_mlflow_tracking.py`

Trains several models and records every run so you can compare them later in a
web dashboard instead of scrolling back through terminal output.

**What gets logged per run**:

- Parameters (`n_estimators`, `max_depth`)
- Metrics (accuracy, precision, recall, f1)
- The trained model itself

**Outputs**: Run history in `mlflow.db`, models in `mlruns/`, viewable with `mlflow ui`

See [MLflow Experiment Tracking](#mlflow-experiment-tracking) at the bottom of this
file for full instructions.

---

## 🚀 Installation

### Prerequisites

- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/) (Python package and project manager)

Install uv if you don't have it:

```bash
# On macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh
# On Windows (PowerShell):
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Required Libraries

Install all dependencies with a single command:

```bash
uv sync
```

That's it. `uv sync` reads `pyproject.toml`, creates the `.venv` folder for you, and installs
the exact versions recorded in `uv.lock` — so everyone in the class gets an identical setup.
You never need to activate the virtual environment manually; just prefix commands with `uv run`.

**Core Dependencies** (installed automatically):

- `pandas` - Data manipulation
- `numpy` - Numerical operations
- `scikit-learn` - Machine learning
- `matplotlib` - Plotting
- `seaborn` - Statistical visualizations
- `plotly` - Interactive charts
- `joblib` - Model serialization
- `streamlit` - Web application framework
- `mlflow` - Experiment tracking

Exact versions are pinned in `uv.lock`. To see what is installed:

```bash
uv pip list
```

### Verify Installation

```bash
uv run python --version    # Should show Python 3.13+
uv pip list                # Show all installed packages
```

### Adding a New Package

```bash
uv add xgboost             # Installs it and records it in pyproject.toml + uv.lock
uv remove xgboost          # Removes it again
```

---

## ▶️ How to Run

### Option 1: Python Scripts (Automated Pipeline)

Navigate to the project directory and run the pipeline scripts in order:

```bash
# Navigate to project directory
cd customer-churn-ml-demo

# Run the complete pipeline
uv run python src/customer_churn_prediction/01_clean_data.py
uv run python src/customer_churn_prediction/02_feature_engineering.py
uv run python src/customer_churn_prediction/03_exploratory_data_analysis.py
uv run python src/customer_churn_prediction/04_model_training_eval.py
uv run python src/customer_churn_prediction/05_hyperparam_tuning.py
uv run python src/customer_churn_prediction/06_mlflow_tracking.py
```

### Option 2: Streamlit Web Application

Launch the interactive prediction app:

```bash
# Method 1: Using Streamlit directly
uv run streamlit run app/streamlit_app.py

# Method 2: Using the provided script
./scripts/run_app.sh
```

The app will open at `http://localhost:8501` with features:

- 🎯 Interactive customer churn prediction
- 📊 Visual risk assessment gauges
- 💡 Actionable retention recommendations
- 📈 Feature importance analysis

**Note**: Run the complete pipeline first to generate the required model file (`models/tuned_churn_model.pkl`).

### Detailed Step-by-Step Instructions

#### Step 1: Data Cleaning

```bash
uv run python src/customer_churn_prediction/01_clean_data.py
```

**What it does**:

- Reads `data/customer_churn_raw.csv`
- Performs all cleaning operations
- Saves cleaned data to `data/customer_churn_cleaned.csv`
- Generates `data/cleaning_summary.csv`

**Expected Output**:

```
================================================================================
CUSTOMER CHURN DATA CLEANING
================================================================================
Loading raw data from: .../data/customer_churn_raw.csv
Loaded 106 records

============================================================
Initial Data Quality Report
============================================================
Total Records: 106
Total Columns: 21
Missing Values:
  - gender: 6 (5.66%)
  - subscription_plan: 5 (4.72%)
  ...
Duplicates:
  - Duplicate customer_ids: 2
...

1. REMOVING DUPLICATES
------------------------------------------------------------
✓ Removed 2 duplicate records
  Records remaining: 104

2. CLEANING CATEGORICAL VARIABLES
------------------------------------------------------------
✓ Standardized gender values: ['Female', 'Male']
✓ Standardized payment_method values: ['Bank Transfer', 'Credit Card', 'PayPal']
...

✓ ALL VALIDATION CHECKS PASSED

================================================================================
CLEANING COMPLETE
================================================================================
```

**Duration**: ~1-2 seconds

#### Step 3: Exploratory Data Analysis

```bash
uv run python src/customer_churn_prediction/03_exploratory_data_analysis.py
```

**What it does**:

- Reads `data/customer_churn_featured.csv`
- Generates visualizations and statistical analysis
- Saves plots to `visualizations/` folder

**Duration**: ~2-3 seconds

#### Step 4: Model Training

```bash
uv run python src/customer_churn_prediction/04_model_training_eval.py
```

**What it does**:

- Trains Random Forest classifier
- Evaluates model performance
- Prints metrics to the console (the model isn't saved yet — that happens in Step 5)

**Duration**: ~3-5 seconds

#### Step 5: Hyperparameter Tuning

```bash
uv run python src/customer_churn_prediction/05_hyperparam_tuning.py
```

**What it does**:

- Performs grid search for optimal parameters
- Cross-validates model performance
- Saves the tuned model to `models/tuned_churn_model.pkl`

**Duration**: ~10-30 seconds (depending on search space)

#### Step 6: MLflow Experiment Tracking

```bash
uv run python src/customer_churn_prediction/06_mlflow_tracking.py
```

**What it does**:

- Trains 3 Random Forest models with different settings
- Logs parameters, metrics, and models to MLflow
- Prints a side-by-side comparison of all runs

**Duration**: ~10-20 seconds

Full instructions (including how to open the dashboard) are in the
[MLflow Experiment Tracking](#mlflow-experiment-tracking) section at the bottom.

#### Step 2: Feature Engineering

```bash
uv run python src/customer_churn_prediction/02_feature_engineering.py
```

**What it does**:

- Reads `data/customer_churn_cleaned.csv`
- Creates 35+ derived features
- Validates all features (handles inf/NaN)
- Saves featured data to `data/customer_churn_featured.csv`
- Generates `data/feature_documentation.csv`

**Expected Output**:

```
================================================================================
CUSTOMER CHURN FEATURE ENGINEERING
================================================================================
Loading cleaned data from: .../data/customer_churn_cleaned.csv
Loaded 104 records with 21 columns

1. CREATING CUSTOMER VALUE FEATURES
------------------------------------------------------------
✓ Created 'monthly_value_ratio' (ARPU)
✓ Created 'charge_per_feature'
✓ Created 'customer_lifetime_value'
✓ Created 'value_tier'

2. CREATING ENGAGEMENT FEATURES
------------------------------------------------------------
✓ Created 'engagement_velocity'
...

Top 15 features correlated with churn:
  1. days_since_last_activity: 0.8234
  2. billing_issues_count: 0.7456
  ...

================================================================================
FEATURE ENGINEERING COMPLETE
================================================================================
Records: 104
Total features: 56
Ready for model training!
```

**Duration**: ~2-3 seconds

### Running from Different Locations

If running from a different directory:

```bash
# Using absolute paths
python /path/to/customer-churn-ml-demo/src/customer_churn_prediction/01_clean_data.py

# Or change directory first
cd /path/to/customer-churn-ml-demo
uv run python src/customer_churn_prediction/01_clean_data.py
```

---

## 📤 Output Files

After running the complete pipeline, you will find:

### Data Files

#### 1. `customer_churn_cleaned.csv`

Clean, validated dataset ready for analysis.

- **Records**: 104 (2 duplicates removed)
- **Features**: 21 (original columns)
- **Quality**: No missing values, no duplicates, all ranges validated

#### 2. `customer_churn_featured.csv`

Machine learning-ready dataset with engineered features.

- **Records**: 104
- **Features**: ~56 (21 original + 35 engineered)
- **Ready for**: Model training, exploratory analysis, predictions

#### 3. `cleaning_summary.csv`

Summary statistics of the cleaning process.

| Metric                 | Value |
| ---------------------- | ----- |
| Initial Records        | 106   |
| Final Records          | 104   |
| Records Removed        | 2     |
| Initial Missing Values | ~45   |
| Final Missing Values   | 0     |

#### 4. `feature_documentation.csv`

Catalog of all features with metadata.

| Feature             | Type       | Data Type | Missing | Unique |
| ------------------- | ---------- | --------- | ------- | ------ |
| customer_id         | Original   | object    | 0       | 104    |
| monthly_value_ratio | Engineered | float64   | 0       | 104    |
| ...                 | ...        | ...       | ...     | ...    |

### Model Files

#### 5. `models/tuned_churn_model.pkl`

Serialized trained Random Forest model.

- **Algorithm**: Random Forest Classifier
- **Input Features**: ~56 features (after encoding)
- **Output**: Churn probability (0-1)
- **Usage**: Load with `joblib.load()` for predictions

### Visualization Files

#### 6. `visualizations/*.png`

Generated plots from EDA:

- Churn distribution charts
- Correlation heatmaps
- Feature importance plots
- Distribution histograms

---

## 🔧 Feature Engineering Details

### Why Feature Engineering?

Raw data often doesn't capture complex patterns. Feature engineering creates meaningful combinations and transformations that help ML models learn better.

### Example Features

**1. Engagement Velocity**

```python
engagement_velocity = engagement_score / tenure_months
```

_Interpretation_: Higher values indicate rapidly engaged customers; lower values may indicate declining interest.

**2. Plan-Tenure Mismatch**

```python
# Risk flag for customers on wrong plan
if premium plan AND tenure < 6 months:
    plan_tenure_mismatch = 1  # Risky: May have been oversold
```

**3. NPS Category**

```python
# Net Promoter Score classification
0-6:  Detractor  (likely to churn)
7-8:  Passive    (neutral)
9-10: Promoter   (advocates)
```

### Feature Validation

The pipeline automatically:

- Replaces infinite values (from division by zero) with 0
- Fills NaN values (numeric: 0, categorical: mode)
- Computes correlation with churn target
- Generates feature documentation

---

## 🔮 Next Steps

After completing the pipeline, you can:

### 1. Use the Streamlit App

```bash
uv run streamlit run app/streamlit_app.py
```

**Features**:

- Interactive customer prediction interface
- Visual risk assessment
- Feature importance display
- Retention recommendations

### 2. Explore Data with the Pipeline Scripts

Re-run the analysis stages for detailed exploration:

- `src/customer_churn_prediction/03_exploratory_data_analysis.py` - Comprehensive EDA
- `src/customer_churn_prediction/04_model_training_eval.py` - Model insights
- `src/customer_churn_prediction/05_hyperparam_tuning.py` - Optimization analysis

### 3. Extend the Pipeline

Add new capabilities:

- Implement additional ML algorithms (XGBoost, Neural Networks)
- Add SHAP for model explainability
- Create custom feature engineering rules
- Build REST API for predictions
- Deploy to cloud (AWS, Azure, GCP)

### 4. Advanced Analysis

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load featured data
df = pd.read_csv('data/customer_churn_featured.csv')

# Visualize churn distribution
df['churned'].value_counts().plot(kind='bar')
plt.title('Churn Distribution')
plt.show()

# Correlation heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), cmap='coolwarm', center=0)
plt.show()
```

### 5. Load and Use Trained Model

```python
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('models/tuned_churn_model.pkl')

# Load new customer data
new_customers = pd.read_csv('data/customer_churn_featured.csv')

# Make predictions
X = new_customers.drop(['customer_id', 'churned'], axis=1)
X = pd.get_dummies(X, drop_first=True)  # One-hot encode categoricals

predictions = model.predict(X)
probabilities = model.predict_proba(X)[:, 1]

# Show high-risk customers
new_customers['churn_probability'] = probabilities
high_risk = new_customers[probabilities > 0.7]
print(f"High-risk customers: {len(high_risk)}")
```

### 6. Batch Predictions

Create a prediction pipeline for new data:

```python
def predict_churn_batch(customer_data_path):
    """Predict churn for a batch of customers"""
    import joblib
    import pandas as pd

    # Load model
    model = joblib.load('models/tuned_churn_model.pkl')

    # Load and prepare data
    df = pd.read_csv(customer_data_path)
    X = df.drop(['customer_id', 'churned'], axis=1, errors='ignore')
    X = pd.get_dummies(X, drop_first=True)

    # Predict
    predictions = model.predict_proba(X)[:, 1]

    # Add to dataframe
    df['churn_risk'] = predictions
    df['risk_category'] = pd.cut(predictions,
                                   bins=[0, 0.3, 0.7, 1.0],
                                   labels=['Low', 'Medium', 'High'])

    return df

# Use it
results = predict_churn_batch('data/customer_churn_featured.csv')
print(results[['customer_id', 'churn_risk', 'risk_category']].head())
```

---

## 📚 Learning Objectives

This project demonstrates:

✅ **Complete ML Pipeline**

- End-to-end workflow from raw data to deployed model
- Sequential processing stages
- Reproducible data science workflow

✅ **Data Cleaning Best Practices**

- Handling missing values
- Removing duplicates
- Standardizing categorical variables
- Validating data quality

✅ **Feature Engineering Techniques**

- Creating ratio and interaction features
- Binning continuous variables
- Engineering domain-specific metrics
- Feature validation

✅ **Machine Learning Development**

- Model training and evaluation
- Hyperparameter tuning
- Feature importance analysis
- Model serialization and deployment
- Experiment tracking with MLflow

✅ **Interactive Development**

- Python scripts for automation
- Web application for end-users
- Visualization and reporting

✅ **Python Programming**

- Pandas data manipulation
- NumPy numerical operations
- Scikit-learn ML workflows
- Streamlit web development
- Modular code organization

✅ **Best Practices**

- Virtual environment management
- Requirements management
- Project structure organization
- Documentation and logging

---

## 🤝 Contributing

To extend this project:

1. **Add new features**: Implement additional feature engineering logic in `src/customer_churn_prediction/02_feature_engineering.py`
2. **Try new models**: Add algorithms in `src/customer_churn_prediction/04_model_training_eval.py`
3. **Enhance visualizations**: Extend EDA in `src/customer_churn_prediction/03_exploratory_data_analysis.py`
4. **Improve the app**: Add features to `app/streamlit_app.py`
5. **Add data sources**: Integrate customer feedback, web analytics, etc.
6. **Implement AutoML**: Add automated model selection pipelines
7. **Build APIs**: Create REST/GraphQL endpoints for predictions

---

## 📝 License

This is a training/demonstration project for educational purposes.

---

## 👤 Author

**AI/ML Trainer**  
Date: November 2025

---

## 📞 Support

For questions or issues:

1. **Check the output**: Review console output for detailed error messages
2. **Verify installation**: Ensure all dependencies are installed (`uv pip list`)
3. **Check paths**: Verify file paths are correct and data files exist
4. **Python version**: Ensure Python 3.13+ is being used
5. **Documentation**: Read `app/README.md` for Streamlit app help

**Common Issues**:

- **Model not found**: Run `uv run python src/customer_churn_prediction/05_hyperparam_tuning.py` to generate `models/tuned_churn_model.pkl`
- **Import errors**: Run `uv sync` to install missing dependencies
- **File not found**: Ensure you're running from the project root directory

---

## 📊 MLflow Experiment Tracking

**Script**: `src/customer_churn_prediction/06_mlflow_tracking.py`

### The Problem

In examples 4 and 5 we trained models and printed the scores to the screen.
Once you close the terminal, those numbers are gone. If you try 10 different
settings, you have no record of which one worked best.

### The Solution

**MLflow** records every training run — the settings you used, the scores you got,
and the trained model itself — and shows them all in a web dashboard so you can
compare runs side by side.

### Step 1: Install MLflow

MLflow is already listed in `pyproject.toml`, so this installs it:

```bash
uv sync
```

To confirm it is installed:

```bash
uv run mlflow --version
```

### Step 2: Run the Tracking Script

Make sure you have already run steps 1 and 2 of the pipeline so that
`data/customer_churn_featured.csv` exists, then:

```bash
uv run python src/customer_churn_prediction/06_mlflow_tracking.py
```

**Expected Output**:

```
================================================================================
MLFLOW EXPERIMENT TRACKING
================================================================================
Training samples: 80
Test samples: 20
Runs to log: 3

Run 1: {'n_estimators': 50, 'max_depth': 3}
        accuracy=1.0000  f1=1.0000
Run 2: {'n_estimators': 100, 'max_depth': 5}
        accuracy=1.0000  f1=1.0000
Run 3: {'n_estimators': 200, 'max_depth': 10}
        accuracy=1.0000  f1=1.0000

================================================================================
COMPARISON OF ALL RUNS (best first)
================================================================================
 n_estimators  max_depth  accuracy  precision  recall  f1
           50          3       1.0        1.0     1.0 1.0
          100          5       1.0        1.0     1.0 1.0
          200         10       1.0        1.0     1.0 1.0

✓ Best run: n_estimators=50, max_depth=3 -> accuracy=1.0000

================================================================================
TRACKING COMPLETE
================================================================================
✓ Run details saved to 'mlflow.db', trained models saved in 'mlruns/'
```

> **Note**: Accuracy is 1.0 for every run because this is a small teaching dataset
> (only 104 rows) with very strong churn signals. On a real dataset you would see
> the scores differ between runs — that difference is exactly what MLflow is for.

### Step 3: Open the MLflow Dashboard

```bash
uv run mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Then open **http://localhost:5000** in your browser. Press `Ctrl+C` in the terminal
to stop the dashboard.

In the dashboard you can:

- Click the **customer_churn** experiment on the left to see all 3 runs
- See parameters and metrics as columns in one table
- Tick two or more runs and click **Compare** to see them side by side
- Click a run, then the **Artifacts** tab, to download the saved model

If port 5000 is already in use (common on macOS, where AirPlay uses it):

```bash
uv run mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5001
```

### The Three Things MLflow Logs

Everything happens inside a `with mlflow.start_run():` block — anything logged
inside that block belongs to that one run.

| What           | Code                                   | Example                         |
| -------------- | -------------------------------------- | ------------------------------- |
| **Parameters** | `mlflow.log_params(params)`            | `n_estimators=100, max_depth=5` |
| **Metrics**    | `mlflow.log_metrics(metrics)`          | `accuracy=0.95, f1=0.94`        |
| **Model**      | `mlflow.sklearn.log_model(model, ...)` | The trained Random Forest       |

Minimal version of the pattern:

```python
import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db")   # where to store runs
mlflow.set_experiment("customer_churn")          # a folder to group runs

with mlflow.start_run(run_name="my_first_run"):
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.sklearn.log_model(model, name="model")
```

### Generated Files

| File / Folder | Contents                                          |
| ------------- | ------------------------------------------------- |
| `mlflow.db`   | SQLite database with run history, params, metrics |
| `mlruns/`     | The saved model files for each run                |

Both are safe to delete — running the script again recreates them. They are
listed in `.gitignore` so they are not committed.

### Try It Yourself

1. Add a fourth setting to the `experiments` list in `src/customer_churn_prediction/06_mlflow_tracking.py`
   (for example `{"n_estimators": 300, "max_depth": 20}`), re-run the script, and
   watch the new run appear in the dashboard.
2. Log an extra metric, such as training accuracy, and compare it to test accuracy.
3. Change `test_size=0.2` to `test_size=0.3`, re-run, and use **Compare** to see
   what changed.

### Common Issues

- **`ModuleNotFoundError: No module named 'mlflow'`** → run `uv sync`
- **Port 5000 already in use** → add `--port 5001` to the `mlflow ui` command
- **Dashboard is empty** → make sure you passed `--backend-store-uri sqlite:///mlflow.db`
  and that you are running the command from the project root folder
- **`FileNotFoundError: data/customer_churn_featured.csv`** → run steps 1 and 2 first

---

**Happy Learning! 🚀**
