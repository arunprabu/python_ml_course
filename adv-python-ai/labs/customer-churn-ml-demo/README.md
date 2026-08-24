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
├── src/                                     # Python Scripts (Pipeline)
│   ├── 01_clean_data.py                    # Data cleaning pipeline
│   ├── 02_feature_engineering.py           # Feature engineering pipeline
│   ├── 03_exploratory_data_analysis.py     # EDA and visualization generation
│   ├── 04_model_training_eval.py           # Model training and evaluation
│   └── 05_hyperparam_tuning.py             # Hyperparameter optimization
│
├── notebooks/                               # Jupyter Notebooks (Interactive Learning)
│   ├── 01_clean_data.ipynb                 # Data cleaning tutorial
│   ├── 02_feature_engineering.ipynb        # Feature engineering tutorial
│   ├── 03_exploratory_data_analysis.ipynb  # EDA tutorial
│   ├── 04_model_training_eval.ipynb        # Model training tutorial
│   └── 05_hyperparam_tuning.ipynb          # Hyperparameter tuning tutorial
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
│   └── churn_model.pkl                     # Serialized trained model
│
├── visualizations/                          # Generated plots and charts
│   └── *.png                               # EDA visualizations
│
├── requirements.txt                         # Python dependencies
└── README.md                                # This file
```

---

## 🔄 Pipeline Process

The project offers **two ways to work**: **Python Scripts** (for automated pipeline) or **Jupyter Notebooks** (for interactive learning).

### Pipeline Stages

The complete pipeline consists of **five stages** that can be run sequentially:

#### Stage 1: Data Cleaning

**Script**: `src/01_clean_data.py` | **Notebook**: `notebooks/01_clean_data.ipynb`

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

**Script**: `src/02_feature_engineering.py` | **Notebook**: `notebooks/02_feature_engineering.ipynb`

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

**Script**: `src/03_exploratory_data_analysis.py` | **Notebook**: `notebooks/03_exploratory_data_analysis.ipynb`

Analyzes data patterns and generates visualizations.

**Analyses Performed**:

- Churn distribution and class balance
- Feature correlation analysis
- Top features correlated with churn
- Distribution plots for key metrics
- Categorical variable analysis

**Outputs**: PNG visualizations saved to `visualizations/` folder

#### Stage 4: Model Training & Evaluation

**Script**: `src/04_model_training_eval.py` | **Notebook**: `notebooks/04_model_training_eval.ipynb`

Trains and evaluates machine learning models.

**Models Trained**:

- Random Forest Classifier (primary model)
- Additional models for comparison (Logistic Regression, etc.)

**Evaluation Metrics**:

- Accuracy, Precision, Recall, F1-Score
- Confusion Matrix
- ROC-AUC Score
- Feature Importance Analysis

**Outputs**: Trained model saved to `models/churn_model.pkl`

#### Stage 5: Hyperparameter Tuning

**Script**: `src/05_hyperparam_tuning.py` | **Notebook**: `notebooks/05_hyperparam_tuning.ipynb`

Optimizes model performance through hyperparameter tuning.

**Techniques**:

- Grid Search CV
- Randomized Search CV
- Cross-validation for model selection

**Outputs**: Best model parameters and improved model

---

## 🚀 Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)

### Required Libraries

Install all dependencies using the provided requirements file:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt
```

**Core Dependencies** (automatically installed):

- `pandas>=2.2.0` - Data manipulation
- `numpy>=1.26.0` - Numerical operations
- `scikit-learn>=1.5.0` - Machine learning
- `matplotlib>=3.9.0` - Plotting
- `seaborn>=0.13.0` - Statistical visualizations
- `plotly>=5.24.0` - Interactive charts
- `joblib>=1.4.0` - Model serialization
- `streamlit>=1.39.0` - Web application framework

### Verify Installation

```bash
python --version        # Should show Python 3.12+
pip list                # Show all installed packages
```

**Optional Dependencies**: See `requirements.txt` for additional packages like XGBoost, LightGBM, SHAP, etc.

---

## ▶️ How to Run

### Option 1: Python Scripts (Automated Pipeline)

Navigate to the project directory and run the pipeline scripts in order:

```bash
# Navigate to project directory
cd customer-churn-ml-demo

# Run the complete pipeline
python src/01_clean_data.py
python src/02_feature_engineering.py
python src/03_exploratory_data_analysis.py
python src/04_model_training_eval.py
python src/05_hyperparam_tuning.py
```

### Option 2: Jupyter Notebooks (Interactive Learning)

Open and run notebooks sequentially for detailed explanations:

```bash
# Start Jupyter
jupyter notebook

# Or use VS Code with Jupyter extension
# Open: notebooks/01_clean_data.ipynb
```

**Notebook Execution Order**:

1. `01_clean_data.ipynb` - Data cleaning
2. `02_feature_engineering.ipynb` - Feature creation
3. `03_exploratory_data_analysis.ipynb` - Data exploration
4. `04_model_training_eval.ipynb` - Model training
5. `05_hyperparam_tuning.ipynb` - Model optimization

### Option 3: Streamlit Web Application

Launch the interactive prediction app:

```bash
# Method 1: Using Streamlit directly
streamlit run app/streamlit_app.py

# Method 2: Using the provided script
./scripts/run_app.sh
```

The app will open at `http://localhost:8501` with features:

- 🎯 Interactive customer churn prediction
- 📊 Visual risk assessment gauges
- 💡 Actionable retention recommendations
- 📈 Feature importance analysis

**Note**: Run the complete pipeline first to generate the required model file (`models/churn_model.pkl`).

### Detailed Step-by-Step Instructions

#### Step 1: Data Cleaning

```bash
python src/01_clean_data.py
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
python src/03_exploratory_data_analysis.py
```

**What it does**:

- Reads `data/customer_churn_featured.csv`
- Generates visualizations and statistical analysis
- Saves plots to `visualizations/` folder

**Duration**: ~2-3 seconds

#### Step 4: Model Training

```bash
python src/04_model_training_eval.py
```

**What it does**:

- Trains Random Forest classifier
- Evaluates model performance
- Saves trained model to `models/churn_model.pkl`

**Duration**: ~3-5 seconds

#### Step 5: Hyperparameter Tuning

```bash
python src/05_hyperparam_tuning.py
```

**What it does**:

- Performs grid search for optimal parameters
- Cross-validates model performance
- Updates model with best parameters

**Duration**: ~10-30 seconds (depending on search space)

#### Step 2: Feature Engineering

```bash
python src/02_feature_engineering.py
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
python /path/to/customer-churn-ml-demo/src/01_clean_data.py

# Or change directory first
cd /path/to/customer-churn-ml-demo
python src/01_clean_data.py
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

#### 5. `models/churn_model.pkl`

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
streamlit run app/streamlit_app.py
```

**Features**:

- Interactive customer prediction interface
- Visual risk assessment
- Feature importance display
- Retention recommendations

### 2. Explore Data with Notebooks

Open the interactive notebooks for detailed exploration:

- `notebooks/03_exploratory_data_analysis.ipynb` - Comprehensive EDA
- `notebooks/04_model_training_eval.ipynb` - Model insights
- `notebooks/05_hyperparam_tuning.ipynb` - Optimization analysis

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
model = joblib.load('models/churn_model.pkl')

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
    model = joblib.load('models/churn_model.pkl')

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

✅ **Interactive Development**

- Jupyter notebooks for exploration
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

1. **Add new features**: Implement additional feature engineering logic in `src/02_feature_engineering.py`
2. **Try new models**: Add algorithms in `src/04_model_training_eval.py`
3. **Enhance visualizations**: Extend EDA in `src/03_exploratory_data_analysis.py`
4. **Improve the app**: Add features to `app/streamlit_app.py`
5. **Create tutorials**: Add notebooks to `notebooks/` folder
6. **Add data sources**: Integrate customer feedback, web analytics, etc.
7. **Implement AutoML**: Add automated model selection pipelines
8. **Build APIs**: Create REST/GraphQL endpoints for predictions

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
2. **Verify installation**: Ensure all dependencies are installed (`pip list`)
3. **Check paths**: Verify file paths are correct and data files exist
4. **Python version**: Ensure Python 3.12+ is being used
5. **Documentation**: Read `app/README.md` for Streamlit app help
6. **Notebooks**: Use Jupyter notebooks for step-by-step debugging

**Common Issues**:

- **Model not found**: Run `python src/04_model_training_eval.py` to generate model
- **Import errors**: Run `pip install -r requirements.txt`
- **File not found**: Ensure you're running from the project root directory

---

**Happy Learning! 🚀**
