"""
Data Cleaning Script for Customer Churn Dataset

This script reads customer_churn_raw.csv, systematically cleans all data quality issues,
and saves the cleaned dataset to customer_churn_cleaned.csv.

Cleaning operations (in order):
1. Remove duplicate records
2. Clean categorical variables (standardize values)
3. Correct data types (convert $ symbols and strings to numeric)
4. Handle missing values (median/mode imputation)
5. Fix outliers and validate ranges
6. Finalize data types (convert to final int/float types)
7. Validate final data quality

Note: Data type correction MUST happen before missing value handling to ensure
numeric operations (like median) work properly on columns with currency symbols.
"""

import pandas as pd
import numpy as np
import os
import re

def load_raw_data(filepath):
    """Load the raw customer churn dataset."""
    print(f"Loading raw data from: {filepath}")
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} records")
    return df

def generate_quality_report(df, stage="Initial"):
    """Generate data quality report."""
    print(f"\n{'='*60}")
    print(f"{stage} Data Quality Report")
    print('='*60)
    
    print(f"Total Records: {len(df)}")
    print(f"Total Columns: {len(df.columns)}")
    
    print(f"\nMissing Values:")
    missing = df.isnull().sum()
    missing_pct = (missing / len(df) * 100).round(2)
    for col in missing[missing > 0].index:
        print(f"  - {col}: {missing[col]} ({missing_pct[col]}%)")
    print(f"  Total missing values: {df.isnull().sum().sum()}")
    
    print(f"\nDuplicates:")
    print(f"  - Duplicate rows (all columns): {df.duplicated().sum()}")
    print(f"  - Duplicate customer_ids: {df['customer_id'].duplicated().sum()}")
    
    print(f"\nData Types:")
    for col, dtype in df.dtypes.items():
        print(f"  - {col}: {dtype}")
    
    print('='*60)

def remove_duplicates(df):
    """Remove duplicate customer records."""
    print("\n1. REMOVING DUPLICATES")
    print("-" * 60)
    
    initial_count = len(df)
    
    # Clean customer_id first (remove whitespace)
    df['customer_id'] = df['customer_id'].astype(str).str.strip()
    
    # Identify duplicates
    duplicates = df[df['customer_id'].duplicated(keep=False)]
    if len(duplicates) > 0:
        print(f"Found {df['customer_id'].duplicated().sum()} duplicate customer_ids:")
        print(f"  Duplicate IDs: {sorted(duplicates['customer_id'].unique())}")
    
    # Remove duplicates, keeping first occurrence
    df_clean = df.drop_duplicates(subset=['customer_id'], keep='first')
    
    removed_count = initial_count - len(df_clean)
    print(f"✓ Removed {removed_count} duplicate records")
    print(f"  Records remaining: {len(df_clean)}")
    
    return df_clean

def clean_categorical_variables(df):
    """Standardize categorical variables."""
    print("\n2. CLEANING CATEGORICAL VARIABLES")
    print("-" * 60)
    
    df_clean = df.copy()
    
    # Gender standardization
    print("Cleaning 'gender'...")
    if 'gender' in df_clean.columns:
        # Strip whitespace and title case
        df_clean['gender'] = df_clean['gender'].astype(str).str.strip().str.title()
        
        # Map variations
        gender_map = {
            'M': 'Male',
            'F': 'Female',
            'Nan': np.nan
        }
        df_clean['gender'] = df_clean['gender'].replace(gender_map)
        
        unique_values = df_clean['gender'].dropna().unique()
        print(f"  ✓ Standardized gender values: {sorted(unique_values)}")
    
    # Payment method standardization
    print("Cleaning 'payment_method'...")
    if 'payment_method' in df_clean.columns:
        # Strip whitespace and normalize
        df_clean['payment_method'] = df_clean['payment_method'].astype(str).str.strip()
        df_clean['payment_method'] = df_clean['payment_method'].str.replace(r'\s+', ' ', regex=True)
        df_clean['payment_method'] = df_clean['payment_method'].str.title()
        
        # Map variations
        payment_map = {
            'Creditcard': 'Credit Card',
            'Cc': 'Credit Card',
            'Banktransfer': 'Bank Transfer',
            'Bt': 'Bank Transfer',
            'Paypal': 'PayPal',
            'Pay Pal': 'PayPal',
            'Nan': np.nan
        }
        df_clean['payment_method'] = df_clean['payment_method'].replace(payment_map)
        
        unique_values = df_clean['payment_method'].dropna().unique()
        print(f"  ✓ Standardized payment_method values: {sorted(unique_values)}")
    
    # Subscription plan standardization
    print("Cleaning 'subscription_plan'...")
    if 'subscription_plan' in df_clean.columns:
        # Strip whitespace and title case
        df_clean['subscription_plan'] = df_clean['subscription_plan'].astype(str).str.strip().str.title()
        
        # Map variations and fix typos
        plan_map = {
            'Premium+': 'Premium',
            'Basicc': 'Basic',
            'Std': 'Standard',
            'Nan': np.nan
        }
        df_clean['subscription_plan'] = df_clean['subscription_plan'].replace(plan_map)
        
        unique_values = df_clean['subscription_plan'].dropna().unique()
        print(f"  ✓ Standardized subscription_plan values: {sorted(unique_values)}")
    
    # Contract type standardization
    print("Cleaning 'contract_type'...")
    if 'contract_type' in df_clean.columns:
        df_clean['contract_type'] = df_clean['contract_type'].astype(str).str.strip().str.title()
        unique_values = df_clean['contract_type'].dropna().unique()
        print(f"  ✓ Standardized contract_type values: {sorted(unique_values)}")
    
    return df_clean

def handle_missing_values(df):
    """Handle missing values with appropriate strategies."""
    print("\n4. HANDLING MISSING VALUES")
    print("-" * 60)
    
    df_clean = df.copy()
    
    # Numerical columns - fill with median
    numerical_cols = ['age', 'tenure_months', 'monthly_charges', 'total_charges', 
                      'login_frequency_monthly', 'features_used', 'data_consumption_gb',
                      'engagement_score', 'days_since_last_activity', 'billing_issues_count',
                      'plan_changes', 'support_tickets', 'avg_resolution_hours',
                      'satisfaction_score', 'nps_score']
    
    print("Filling numerical columns with median:")
    for col in numerical_cols:
        if col in df_clean.columns:
            missing_count = df_clean[col].isnull().sum()
            if missing_count > 0:
                median_value = df_clean[col].median()
                df_clean[col] = df_clean[col].fillna(median_value)
                print(f"  - {col}: filled {missing_count} values with median ({median_value:.2f})")
    
    # Categorical columns - fill with mode
    categorical_cols = ['gender', 'subscription_plan', 'contract_type', 'payment_method']
    
    print("\nFilling categorical columns with mode:")
    for col in categorical_cols:
        if col in df_clean.columns:
            missing_count = df_clean[col].isnull().sum()
            if missing_count > 0:
                mode_value = df_clean[col].mode()[0] if len(df_clean[col].mode()) > 0 else 'Unknown'
                df_clean[col] = df_clean[col].fillna(mode_value)
                print(f"  - {col}: filled {missing_count} values with mode ('{mode_value}')")
    
    # Verify no missing values remain
    remaining_missing = df_clean.isnull().sum().sum()
    print(f"\n✓ Remaining missing values: {remaining_missing}")
    
    return df_clean

def correct_data_types(df):
    """Correct data types for all columns (MUST run before handling missing values)."""
    print("\n3. CORRECTING DATA TYPES")
    print("-" * 60)
    
    df_clean = df.copy()
    
    # Remove currency symbols and convert monetary columns first
    if 'monthly_charges' in df_clean.columns:
        print("Fixing 'monthly_charges' (removing $ symbols and converting to float)...")
        df_clean['monthly_charges'] = df_clean['monthly_charges'].astype(str).str.replace('$', '', regex=False)
        df_clean['monthly_charges'] = pd.to_numeric(df_clean['monthly_charges'], errors='coerce')
        print(f"  ✓ Converted to float")
    
    if 'total_charges' in df_clean.columns:
        print("Fixing 'total_charges' (converting to float)...")
        df_clean['total_charges'] = pd.to_numeric(df_clean['total_charges'], errors='coerce')
        print(f"  ✓ Converted to float")
    
    # Convert other numerical columns that might have issues
    numerical_cols_to_convert = ['age', 'tenure_months', 'login_frequency_monthly', 'features_used',
                                  'data_consumption_gb', 'engagement_score', 'days_since_last_activity',
                                  'billing_issues_count', 'plan_changes', 'support_tickets',
                                  'avg_resolution_hours', 'satisfaction_score', 'nps_score']
    
    print("\nConverting numerical columns to numeric types...")
    for col in numerical_cols_to_convert:
        if col in df_clean.columns:
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
    print(f"  ✓ Converted {len([c for c in numerical_cols_to_convert if c in df_clean.columns])} columns")
    
    # Clean string columns
    string_columns = ['customer_id', 'gender', 'subscription_plan', 'contract_type', 'payment_method']
    
    print("\nCleaning string columns...")
    for col in string_columns:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].astype(str).str.strip()
    print(f"  ✓ Cleaned {len([c for c in string_columns if c in df_clean.columns])} columns")
    
    return df_clean

def fix_outliers_and_validate_ranges(df):
    """Fix outliers and validate value ranges."""
    print("\n5. FIXING OUTLIERS AND VALIDATING RANGES")
    print("-" * 60)
    
    df_clean = df.copy()
    
    # Age: clip to 18-100
    print("Validating 'age' (range: 18-100)...")
    if 'age' in df_clean.columns:
        outliers = ((df_clean['age'] < 18) | (df_clean['age'] > 100)).sum()
        df_clean['age'] = df_clean['age'].clip(18, 100)
        print(f"  ✓ Fixed {outliers} outliers")
    
    # Tenure: must be >= 1
    print("Validating 'tenure_months' (minimum: 1)...")
    if 'tenure_months' in df_clean.columns:
        outliers = (df_clean['tenure_months'] < 1).sum()
        df_clean['tenure_months'] = df_clean['tenure_months'].clip(lower=1)
        print(f"  ✓ Fixed {outliers} outliers")
    
    # Monthly charges: must be positive
    print("Validating 'monthly_charges' (must be positive)...")
    if 'monthly_charges' in df_clean.columns:
        outliers = (df_clean['monthly_charges'] <= 0).sum()
        # Replace invalid with median
        median_val = df_clean[df_clean['monthly_charges'] > 0]['monthly_charges'].median()
        df_clean.loc[df_clean['monthly_charges'] <= 0, 'monthly_charges'] = median_val
        print(f"  ✓ Fixed {outliers} outliers (replaced with median: {median_val:.2f})")
    
    # Total charges: must be positive
    print("Validating 'total_charges' (must be positive)...")
    if 'total_charges' in df_clean.columns:
        outliers = (df_clean['total_charges'] <= 0).sum()
        # Calculate from monthly_charges * tenure_months if invalid
        mask = df_clean['total_charges'] <= 0
        df_clean.loc[mask, 'total_charges'] = (
            df_clean.loc[mask, 'monthly_charges'] * df_clean.loc[mask, 'tenure_months']
        )
        print(f"  ✓ Fixed {outliers} outliers (recalculated)")
    
    # Engagement score: 0-100
    print("Validating 'engagement_score' (range: 0-100)...")
    if 'engagement_score' in df_clean.columns:
        outliers = ((df_clean['engagement_score'] < 0) | (df_clean['engagement_score'] > 100)).sum()
        df_clean['engagement_score'] = df_clean['engagement_score'].clip(0, 100)
        print(f"  ✓ Fixed {outliers} outliers")
    
    # Satisfaction score: 1-5
    print("Validating 'satisfaction_score' (range: 1-5)...")
    if 'satisfaction_score' in df_clean.columns:
        outliers = ((df_clean['satisfaction_score'] < 1) | (df_clean['satisfaction_score'] > 5)).sum()
        df_clean['satisfaction_score'] = df_clean['satisfaction_score'].clip(1, 5)
        print(f"  ✓ Fixed {outliers} outliers")
    
    # NPS score: 0-10
    print("Validating 'nps_score' (range: 0-10)...")
    if 'nps_score' in df_clean.columns:
        outliers = ((df_clean['nps_score'] < 0) | (df_clean['nps_score'] > 10)).sum()
        df_clean['nps_score'] = df_clean['nps_score'].clip(0, 10)
        print(f"  ✓ Fixed {outliers} outliers")
    
    return df_clean

def finalize_data_types(df):
    """Finalize data types after all cleaning (convert to final int/float types)."""
    print("\n6. FINALIZING DATA TYPES")
    print("-" * 60)
    
    df_clean = df.copy()
    
    # Ensure integer columns (after missing values are filled)
    int_columns = ['age', 'tenure_months', 'login_frequency_monthly', 'features_used',
                   'days_since_last_activity', 'billing_issues_count', 'plan_changes',
                   'support_tickets', 'churned']
    
    print("Finalizing integer columns...")
    for col in int_columns:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].fillna(0).astype(int)
            print(f"  - {col}: int")
    
    # Ensure float columns
    float_columns = ['monthly_charges', 'total_charges', 'data_consumption_gb',
                     'engagement_score', 'avg_resolution_hours', 'satisfaction_score',
                     'nps_score']
    
    print("\nFinalizing float columns...")
    for col in float_columns:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].astype(float)
            print(f"  - {col}: float")
    
    return df_clean

def validate_final_data(df):
    """Perform final validation checks."""
    print("\n7. FINAL VALIDATION")
    print("-" * 60)
    
    issues_found = []
    
    # Check for missing values
    missing = df.isnull().sum().sum()
    if missing > 0:
        issues_found.append(f"Missing values found: {missing}")
    else:
        print("✓ No missing values")
    
    # Check for duplicates
    duplicates = df['customer_id'].duplicated().sum()
    if duplicates > 0:
        issues_found.append(f"Duplicate customer_ids found: {duplicates}")
    else:
        print("✓ No duplicate customer IDs")
    
    # Check value ranges
    if 'age' in df.columns:
        invalid_age = ((df['age'] < 18) | (df['age'] > 100)).sum()
        if invalid_age == 0:
            print("✓ Age values valid (18-100)")
        else:
            issues_found.append(f"Invalid age values: {invalid_age}")
    
    if 'engagement_score' in df.columns:
        invalid_engagement = ((df['engagement_score'] < 0) | (df['engagement_score'] > 100)).sum()
        if invalid_engagement == 0:
            print("✓ Engagement score valid (0-100)")
        else:
            issues_found.append(f"Invalid engagement scores: {invalid_engagement}")
    
    if 'satisfaction_score' in df.columns:
        invalid_satisfaction = ((df['satisfaction_score'] < 1) | (df['satisfaction_score'] > 5)).sum()
        if invalid_satisfaction == 0:
            print("✓ Satisfaction score valid (1-5)")
        else:
            issues_found.append(f"Invalid satisfaction scores: {invalid_satisfaction}")
    
    # Check for negative values in charges
    if 'monthly_charges' in df.columns:
        negative_charges = (df['monthly_charges'] <= 0).sum()
        if negative_charges == 0:
            print("✓ Monthly charges all positive")
        else:
            issues_found.append(f"Negative/zero monthly charges: {negative_charges}")
    
    if len(issues_found) > 0:
        print("\n⚠ ISSUES FOUND:")
        for issue in issues_found:
            print(f"  - {issue}")
        return False
    else:
        print("\n✓ ALL VALIDATION CHECKS PASSED")
        return True

def save_cleaning_summary(initial_df, cleaned_df, output_path):
    """Save a summary of the cleaning process."""
    print("\nGenerating cleaning summary...")
    
    summary = {
        'metric': [
            'Initial Records',
            'Final Records',
            'Records Removed',
            'Initial Missing Values',
            'Final Missing Values',
            'Initial Duplicates',
            'Final Duplicates',
            'Outliers Fixed'
        ],
        'value': [
            len(initial_df),
            len(cleaned_df),
            len(initial_df) - len(cleaned_df),
            initial_df.isnull().sum().sum(),
            cleaned_df.isnull().sum().sum(),
            initial_df['customer_id'].duplicated().sum(),
            cleaned_df['customer_id'].duplicated().sum(),
            'Multiple (age, charges, scores)'
        ]
    }
    
    summary_df = pd.DataFrame(summary)
    summary_path = os.path.join(os.path.dirname(output_path), 'cleaning_summary.csv')
    summary_df.to_csv(summary_path, index=False)
    print(f"  Saved summary to: {summary_path}")

def main():
    """Main execution function."""
    print("="*80)
    print("CUSTOMER CHURN DATA CLEANING")
    print("="*80)
    
    # Paths
    base_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(os.path.dirname(base_path), 'data')
    input_file = os.path.join(data_path, 'customer_churn_raw.csv')
    output_file = os.path.join(data_path, 'customer_churn_cleaned.csv')
    
    # Load raw data
    df_raw = load_raw_data(input_file)
    
    # Initial quality report
    generate_quality_report(df_raw, "Initial")
    
    # Store initial state for summary
    df_initial = df_raw.copy()
    
    # Cleaning pipeline (order is critical!)
    df_clean = remove_duplicates(df_raw)
    df_clean = clean_categorical_variables(df_clean)
    df_clean = correct_data_types(df_clean)  # MUST convert types before handling missing values
    df_clean = handle_missing_values(df_clean)
    df_clean = fix_outliers_and_validate_ranges(df_clean)
    df_clean = finalize_data_types(df_clean)
    
    # Final validation
    validation_passed = validate_final_data(df_clean)
    
    # Final quality report
    generate_quality_report(df_clean, "Final")
    
    # Save cleaned data
    print(f"\nSaving cleaned data to: {output_file}")
    df_clean.to_csv(output_file, index=False)
    print(f"✓ Saved {len(df_clean)} cleaned records")
    
    # Save cleaning summary
    save_cleaning_summary(df_initial, df_clean, output_file)
    
    # Summary
    print("\n" + "="*80)
    print("CLEANING COMPLETE")
    print("="*80)
    print(f"Records processed: {len(df_initial)} → {len(df_clean)}")
    print(f"Records removed: {len(df_initial) - len(df_clean)}")
    print(f"Data quality: {'✓ PASSED' if validation_passed else '✗ FAILED'}")
    print("="*80)

if __name__ == "__main__":
    main()
