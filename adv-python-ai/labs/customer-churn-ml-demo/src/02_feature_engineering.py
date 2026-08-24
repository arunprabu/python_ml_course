"""
Feature Engineering Script for Customer Churn Dataset

This script reads customer_churn_cleaned.csv, creates derived features capturing
customer behavior patterns and risk indicators, and saves the feature-enriched
dataset to customer_churn_featured.csv.

Feature Categories:
1. Customer value metrics
2. Engagement indicators
3. Support risk features
4. Interaction features
5. Tenure and lifecycle features

Author: Training Demo
Date: November 2025
"""

import pandas as pd
import numpy as np
import os

def load_cleaned_data(filepath):
    """Load the cleaned customer churn dataset."""
    print(f"Loading cleaned data from: {filepath}")
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} records with {len(df.columns)} columns")
    return df

def create_customer_value_features(df):
    """Create customer value and revenue features."""
    print("\n1. CREATING CUSTOMER VALUE FEATURES")
    print("-" * 60)
    
    df_featured = df.copy()
    
    # Monthly value ratio (ARPU)
    df_featured['monthly_value_ratio'] = df_featured['total_charges'] / df_featured['tenure_months']
    df_featured['monthly_value_ratio'] = df_featured['monthly_value_ratio'].replace([np.inf, -np.inf], 0)
    print("✓ Created 'monthly_value_ratio' (ARPU)")
    
    # Charge efficiency (cost per feature)
    df_featured['charge_per_feature'] = df_featured['monthly_charges'] / df_featured['features_used']
    df_featured['charge_per_feature'] = df_featured['charge_per_feature'].replace([np.inf, -np.inf], 0)
    print("✓ Created 'charge_per_feature'")
    
    # Lifetime value proxy (only for non-churned customers)
    df_featured['customer_lifetime_value'] = df_featured.apply(
        lambda row: row['total_charges'] if row['churned'] == 0 else 0, axis=1
    )
    print("✓ Created 'customer_lifetime_value'")
    
    # Value tier based on total charges
    df_featured['value_tier'] = pd.cut(
        df_featured['total_charges'],
        bins=[0, 500, 1500, 3000, np.inf],
        labels=['Low', 'Medium', 'High', 'Premium']
    )
    print("✓ Created 'value_tier'")
    
    return df_featured

def create_engagement_features(df):
    """Create engagement and usage pattern features."""
    print("\n2. CREATING ENGAGEMENT FEATURES")
    print("-" * 60)
    
    df_featured = df.copy()
    
    # Engagement velocity (engagement per month)
    df_featured['engagement_velocity'] = df_featured['engagement_score'] / df_featured['tenure_months']
    df_featured['engagement_velocity'] = df_featured['engagement_velocity'].replace([np.inf, -np.inf], 0)
    print("✓ Created 'engagement_velocity'")
    
    # Login intensity (average daily logins)
    df_featured['login_intensity'] = df_featured['login_frequency_monthly'] / 30
    print("✓ Created 'login_intensity'")
    
    # Data per login
    df_featured['data_per_login'] = df_featured['data_consumption_gb'] / df_featured['login_frequency_monthly']
    df_featured['data_per_login'] = df_featured['data_per_login'].replace([np.inf, -np.inf], 0)
    print("✓ Created 'data_per_login'")
    
    # Activity recency category
    df_featured['activity_recency_category'] = pd.cut(
        df_featured['days_since_last_activity'],
        bins=[-1, 7, 14, 30, np.inf],
        labels=['Active', 'Moderate', 'At_Risk', 'Dormant']
    )
    print("✓ Created 'activity_recency_category'")
    
    # Features utilization rate
    df_featured['features_utilization_rate'] = df_featured['features_used'] / 10  # Assuming max 10 features
    print("✓ Created 'features_utilization_rate'")
    
    # Data consumption per tenure
    df_featured['data_per_tenure'] = df_featured['data_consumption_gb'] / df_featured['tenure_months']
    print("✓ Created 'data_per_tenure'")
    
    return df_featured

def create_support_risk_features(df):
    """Create support and satisfaction risk features."""
    print("\n3. CREATING SUPPORT RISK FEATURES")
    print("-" * 60)
    
    df_featured = df.copy()
    
    # Support rate (annualized)
    df_featured['support_rate_annual'] = (df_featured['support_tickets'] / df_featured['tenure_months']) * 12
    print("✓ Created 'support_rate_annual'")
    
    # Resolution burden (total resolution time)
    df_featured['resolution_burden'] = df_featured['avg_resolution_hours'] * df_featured['support_tickets']
    print("✓ Created 'resolution_burden'")
    
    # Satisfaction gap (distance from perfect score)
    df_featured['satisfaction_gap'] = 5 - df_featured['satisfaction_score']
    print("✓ Created 'satisfaction_gap'")
    
    # Billing risk flag
    df_featured['billing_risk_flag'] = (df_featured['billing_issues_count'] > 0).astype(int)
    print("✓ Created 'billing_risk_flag'")
    
    # Complaint ratio
    df_featured['complaint_ratio'] = (
        (df_featured['billing_issues_count'] + df_featured['plan_changes']) / df_featured['tenure_months']
    )
    df_featured['complaint_ratio'] = df_featured['complaint_ratio'].replace([np.inf, -np.inf], 0)
    print("✓ Created 'complaint_ratio'")
    
    # Support satisfaction ratio
    df_featured['support_satisfaction_ratio'] = (
        df_featured['satisfaction_score'] / (df_featured['support_tickets'] + 1)
    )
    print("✓ Created 'support_satisfaction_ratio'")
    
    # NPS category
    df_featured['nps_category'] = pd.cut(
        df_featured['nps_score'],
        bins=[-1, 6, 8, 10],
        labels=['Detractor', 'Passive', 'Promoter']
    )
    print("✓ Created 'nps_category'")
    
    return df_featured

def create_interaction_features(df):
    """Create interaction and mismatch features."""
    print("\n4. CREATING INTERACTION FEATURES")
    print("-" * 60)
    
    df_featured = df.copy()
    
    # Plan tenure fit
    def plan_tenure_fit(row):
        if row['subscription_plan'] == 'Premium' and row['tenure_months'] < 6:
            return 1  # Risky: Premium but new
        elif row['subscription_plan'] == 'Basic' and row['tenure_months'] > 36:
            return 1  # Risky: Basic but long tenure (undermonetized)
        else:
            return 0
    
    df_featured['plan_tenure_mismatch'] = df_featured.apply(plan_tenure_fit, axis=1)
    print("✓ Created 'plan_tenure_mismatch'")
    
    # Usage plan mismatch
    def usage_plan_mismatch(row):
        if row['subscription_plan'] == 'Basic' and row['data_consumption_gb'] > 40:
            return 1  # High usage on basic plan
        elif row['subscription_plan'] == 'Premium' and row['data_consumption_gb'] < 20:
            return 1  # Low usage on premium plan
        else:
            return 0
    
    df_featured['usage_plan_mismatch'] = df_featured.apply(usage_plan_mismatch, axis=1)
    print("✓ Created 'usage_plan_mismatch'")
    
    # Payment stability
    df_featured['payment_stability'] = 1 / (df_featured['billing_issues_count'] + 1)
    print("✓ Created 'payment_stability'")
    
    # NPS satisfaction alignment
    df_featured['nps_satisfaction_alignment'] = abs((df_featured['nps_score'] / 2) - df_featured['satisfaction_score'])
    print("✓ Created 'nps_satisfaction_alignment'")
    
    # Contract value match (monthly charges vs contract type)
    def contract_value_match(row):
        if row['contract_type'] == 'Annual' and row['monthly_charges'] < 40:
            return 1  # Low value annual contract
        elif row['contract_type'] == 'Monthly' and row['monthly_charges'] > 70:
            return 1  # High value monthly (retention risk)
        else:
            return 0
    
    df_featured['contract_value_risk'] = df_featured.apply(contract_value_match, axis=1)
    print("✓ Created 'contract_value_risk'")
    
    return df_featured

def create_tenure_lifecycle_features(df):
    """Create tenure and customer lifecycle features."""
    print("\n5. CREATING TENURE AND LIFECYCLE FEATURES")
    print("-" * 60)
    
    df_featured = df.copy()
    
    # Lifecycle stage
    df_featured['lifecycle_stage'] = pd.cut(
        df_featured['tenure_months'],
        bins=[0, 6, 12, 24, 48, np.inf],
        labels=['New', 'Trial_End', 'Early', 'Mature', 'Veteran']
    )
    print("✓ Created 'lifecycle_stage'")
    
    # Contract tenure ratio
    contract_months = {'Monthly': 1, 'Annual': 12}
    df_featured['contract_tenure_ratio'] = df_featured.apply(
        lambda row: row['tenure_months'] / contract_months.get(row['contract_type'], 1),
        axis=1
    )
    print("✓ Created 'contract_tenure_ratio'")
    
    # Tenure category (simple bins)
    df_featured['tenure_category'] = pd.cut(
        df_featured['tenure_months'],
        bins=[0, 12, 24, 36, np.inf],
        labels=['0-1yr', '1-2yr', '2-3yr', '3yr+']
    )
    print("✓ Created 'tenure_category'")
    
    # Growth rate (engagement growth over tenure)
    df_featured['engagement_growth_rate'] = df_featured['engagement_score'] / (df_featured['tenure_months'] + 1)
    print("✓ Created 'engagement_growth_rate'")
    
    # Tenure stability score (tenure normalized by age)
    df_featured['tenure_stability'] = df_featured['tenure_months'] / (df_featured['age'] * 12)
    print("✓ Created 'tenure_stability'")
    
    return df_featured

def validate_features(df):
    """Validate engineered features."""
    print("\n6. VALIDATING ENGINEERED FEATURES")
    print("-" * 60)
    
    # Check for infinite values in numeric columns
    inf_cols = []
    for col in df.select_dtypes(include=[np.number]).columns:
        if np.isinf(df[col]).any():
            inf_cols.append(col)
    
    if inf_cols:
        print(f"⚠ Found infinite values in: {inf_cols}")
        # Replace inf with 0
        df = df.replace([np.inf, -np.inf], 0)
        print("  ✓ Replaced infinite values with 0")
    else:
        print("✓ No infinite values found")
    
    # Check for NaN values
    nan_count = df.isnull().sum().sum()
    if nan_count > 0:
        print(f"⚠ Found {nan_count} NaN values")
        
        # Fill NaN for numeric columns only
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            if df[col].isnull().any():
                df[col] = df[col].fillna(0)
        
        # For categorical columns, fill with mode or drop
        categorical_cols = df.select_dtypes(include=['category', 'object']).columns
        for col in categorical_cols:
            if df[col].isnull().any():
                # Skip customer_id and churned
                if col not in ['customer_id', 'churned']:
                    # Get mode, if exists use it, otherwise use first category
                    mode_val = df[col].mode()
                    if len(mode_val) > 0:
                        df[col] = df[col].fillna(mode_val[0])
                    else:
                        # For categorical created by pd.cut, use first category
                        if hasattr(df[col], 'cat'):
                            df[col] = df[col].cat.add_categories(['Unknown']).fillna('Unknown')
        
        print("  ✓ Filled NaN values (0 for numeric, mode for categorical)")
    else:
        print("✓ No NaN values found")
    
    # Check feature correlations with target (numeric columns only)
    print("\nTop 15 features correlated with churn:")
    numeric_df = df.select_dtypes(include=[np.number])
    if 'churned' in numeric_df.columns:
        correlations = numeric_df.corr()['churned'].sort_values(ascending=False)
        top_features = correlations[1:16]  # Exclude 'churned' itself
        for i, (feature, corr) in enumerate(top_features.items(), 1):
            print(f"  {i}. {feature}: {corr:.4f}")
    else:
        print("  ⚠ 'churned' column not found in numeric columns")
    
    return df

def save_feature_documentation(df, output_path):
    """Save feature documentation."""
    print("\nGenerating feature documentation...")
    
    # Create feature catalog
    features = []
    
    # Original features
    original_features = [
        'customer_id', 'age', 'gender', 'tenure_months', 'subscription_plan',
        'monthly_charges', 'total_charges', 'contract_type', 'payment_method',
        'login_frequency_monthly', 'features_used', 'data_consumption_gb',
        'engagement_score', 'days_since_last_activity', 'billing_issues_count',
        'plan_changes', 'support_tickets', 'avg_resolution_hours',
        'satisfaction_score', 'nps_score', 'churned'
    ]
    
    for feature in df.columns:
        if feature in original_features:
            features.append({
                'feature': feature,
                'type': 'Original',
                'data_type': str(df[feature].dtype),
                'missing': df[feature].isnull().sum(),
                'unique': df[feature].nunique()
            })
        else:
            features.append({
                'feature': feature,
                'type': 'Engineered',
                'data_type': str(df[feature].dtype),
                'missing': df[feature].isnull().sum(),
                'unique': df[feature].nunique()
            })
    
    feature_doc = pd.DataFrame(features)
    doc_path = os.path.join(os.path.dirname(output_path), 'feature_documentation.csv')
    feature_doc.to_csv(doc_path, index=False)
    print(f"  Saved documentation to: {doc_path}")
    
    # Print summary
    print(f"\nFeature Summary:")
    print(f"  - Original features: {len([f for f in features if f['type'] == 'Original'])}")
    print(f"  - Engineered features: {len([f for f in features if f['type'] == 'Engineered'])}")
    print(f"  - Total features: {len(features)}")

def main():
    """Main execution function."""
    print("="*80)
    print("CUSTOMER CHURN FEATURE ENGINEERING")
    print("="*80)
    
    # Paths
    base_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(os.path.dirname(base_path), 'data')
    input_file = os.path.join(data_path, 'customer_churn_cleaned.csv')
    output_file = os.path.join(data_path, 'customer_churn_featured.csv')
    
    # Load cleaned data
    df = load_cleaned_data(input_file)
    
    print(f"\nStarting feature engineering...")
    print(f"Initial features: {len(df.columns)}")
    
    # Feature engineering pipeline
    df = create_customer_value_features(df)
    df = create_engagement_features(df)
    df = create_support_risk_features(df)
    df = create_interaction_features(df)
    df = create_tenure_lifecycle_features(df)
    
    # Validate features
    df = validate_features(df)
    
    print(f"\nFinal features: {len(df.columns)}")
    print(f"New features created: {len(df.columns) - 21}")  # 21 original features
    
    # Save feature documentation
    save_feature_documentation(df, output_file)
    
    # Save featured data
    print(f"\nSaving featured data to: {output_file}")
    df.to_csv(output_file, index=False)
    print(f"✓ Saved {len(df)} records with {len(df.columns)} features")
    
    # Summary
    print("\n" + "="*80)
    print("FEATURE ENGINEERING COMPLETE")
    print("="*80)
    print(f"Records: {len(df)}")
    print(f"Total features: {len(df.columns)}")
    print(f"Ready for model training!")
    print("="*80)

if __name__ == "__main__":
    main()
