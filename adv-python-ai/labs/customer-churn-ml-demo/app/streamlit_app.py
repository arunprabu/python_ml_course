"""
Customer Churn Prediction - Streamlit Demo App

This interactive app demonstrates the customer churn prediction model.
Users can input customer features and get real-time churn predictions with explanations.
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from pathlib import Path
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem !important;
        font-weight: bold !important;
        color: #1f77b4 !important;
        text-align: center !important;
        margin-bottom: 0.5rem !important;
        line-height: 1.2 !important;
    }
    .sub-header {
        font-size: 1.2rem !important;
        color: #666 !important;
        text-align: center !important;
        margin-bottom: 2rem !important;
    }
    .prediction-box {
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        margin: 1rem 0;
    }
    .churn-yes {
        background-color: #ffebee;
        color: #c62828;
        border: 2px solid #c62828;
    }
    .churn-no {
        background-color: #e8f5e9;
        color: #2e7d32;
        border: 2px solid #2e7d32;
    }
    .metric-card {
        background-color: #f5f5f5;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_model():
    """Load the trained model"""
    model_path = Path(__file__).parent.parent / "models" / "tuned_churn_model.pkl"
    if not model_path.exists():
        st.error(f"Model not found at {model_path}. Please train the model first.")
        st.stop()
    return joblib.load(model_path)


@st.cache_data
def load_sample_data():
    """Load sample data for reference"""
    data_path = Path(__file__).parent.parent / "data" / "customer_churn_featured.csv"
    if data_path.exists():
        return pd.read_csv(data_path)
    return None


def create_feature_dict(
    age, gender, tenure_months, subscription_plan, monthly_charges,
    contract_type, payment_method, login_frequency_monthly, features_used,
    data_consumption_gb, days_since_last_activity, billing_issues_count,
    plan_changes, support_tickets, avg_resolution_hours, satisfaction_score,
    nps_score
):
    """Create feature dictionary from user inputs"""
    
    # Calculate derived features (matching the training data)
    total_charges = monthly_charges * tenure_months
    engagement_score = min(100, (login_frequency_monthly / 30 * 50) + (features_used / 10 * 50))
    monthly_value_ratio = monthly_charges
    charge_per_feature = monthly_charges / features_used if features_used > 0 else 0
    customer_lifetime_value = total_charges if contract_type != "Monthly" else 0
    
    # Value tier
    if monthly_charges > 60:
        value_tier = "High"
    elif monthly_charges > 30:
        value_tier = "Medium"
    else:
        value_tier = "Low"
    
    # Engagement velocity
    engagement_velocity = login_frequency_monthly / 7
    
    # Login intensity
    login_intensity = login_frequency_monthly / 30
    
    # Data per login
    data_per_login = data_consumption_gb / login_frequency_monthly if login_frequency_monthly > 0 else 0
    
    # Activity recency category
    if days_since_last_activity <= 3:
        activity_recency_category = "Active"
    elif days_since_last_activity <= 7:
        activity_recency_category = "Recent"
    else:
        activity_recency_category = "At_Risk"
    
    # Features utilization rate
    features_utilization_rate = features_used / 10
    
    # Data per tenure
    data_per_tenure = data_consumption_gb / tenure_months if tenure_months > 0 else 0
    
    # Support rate annual
    support_rate_annual = (support_tickets / tenure_months) * 12 if tenure_months > 0 else 0
    
    # Resolution burden
    resolution_burden = avg_resolution_hours * support_tickets
    
    # Satisfaction gap
    satisfaction_gap = 5.0 - satisfaction_score
    
    # Billing risk flag
    billing_risk_flag = 1 if billing_issues_count > 0 else 0
    
    # Complaint ratio
    complaint_ratio = support_tickets / tenure_months if tenure_months > 0 else 0
    
    # Support satisfaction ratio
    support_satisfaction_ratio = satisfaction_score / support_tickets if support_tickets > 0 else satisfaction_score
    
    # NPS category
    if nps_score >= 9:
        nps_category = "Promoter"
    elif nps_score >= 7:
        nps_category = "Passive"
    else:
        nps_category = "Detractor"
    
    # Plan tenure mismatch
    plan_tenure_mismatch = 1 if (subscription_plan == "Basic" and tenure_months > 24) else 0
    
    # Usage plan mismatch
    usage_plan_mismatch = 1 if (subscription_plan == "Basic" and features_used > 5) else 0
    
    # Payment stability
    if payment_method == "Credit Card":
        payment_stability = 1.0
    elif payment_method == "Bank Transfer":
        payment_stability = 0.8
    else:
        payment_stability = 0.5
    
    # NPS satisfaction alignment
    nps_satisfaction_alignment = abs(nps_score / 2 - satisfaction_score) / 5
    
    # Contract value risk
    contract_value_risk = 1 if (contract_type == "Monthly" and monthly_charges > 50) else 0
    
    # Lifecycle stage
    if tenure_months < 6:
        lifecycle_stage = "New"
    elif tenure_months < 12:
        lifecycle_stage = "Early"
    elif tenure_months < 24:
        lifecycle_stage = "Growing"
    else:
        lifecycle_stage = "Mature"
    
    # Contract tenure ratio
    if contract_type == "Monthly":
        contract_tenure_ratio = 1.0
    elif contract_type == "Annual":
        contract_tenure_ratio = 12.0
    else:
        contract_tenure_ratio = 24.0
    
    contract_tenure_ratio = tenure_months / contract_tenure_ratio if contract_tenure_ratio > 0 else 0
    
    # Tenure category
    if tenure_months < 12:
        tenure_category = "0-1yr"
    elif tenure_months < 24:
        tenure_category = "1-2yr"
    elif tenure_months < 36:
        tenure_category = "2-3yr"
    else:
        tenure_category = "3yr+"
    
    # Engagement growth rate
    engagement_growth_rate = engagement_score / tenure_months if tenure_months > 0 else 0
    
    # Tenure stability
    tenure_stability = min(1.0, tenure_months / 60)
    
    features = {
        'age': age,
        'gender': gender,
        'tenure_months': tenure_months,
        'subscription_plan': subscription_plan,
        'monthly_charges': monthly_charges,
        'total_charges': total_charges,
        'contract_type': contract_type,
        'payment_method': payment_method,
        'login_frequency_monthly': login_frequency_monthly,
        'features_used': features_used,
        'data_consumption_gb': data_consumption_gb,
        'engagement_score': engagement_score,
        'days_since_last_activity': days_since_last_activity,
        'billing_issues_count': billing_issues_count,
        'plan_changes': plan_changes,
        'support_tickets': support_tickets,
        'avg_resolution_hours': avg_resolution_hours,
        'satisfaction_score': satisfaction_score,
        'nps_score': nps_score,
        'monthly_value_ratio': monthly_value_ratio,
        'charge_per_feature': charge_per_feature,
        'customer_lifetime_value': customer_lifetime_value,
        'value_tier': value_tier,
        'engagement_velocity': engagement_velocity,
        'login_intensity': login_intensity,
        'data_per_login': data_per_login,
        'activity_recency_category': activity_recency_category,
        'features_utilization_rate': features_utilization_rate,
        'data_per_tenure': data_per_tenure,
        'support_rate_annual': support_rate_annual,
        'resolution_burden': resolution_burden,
        'satisfaction_gap': satisfaction_gap,
        'billing_risk_flag': billing_risk_flag,
        'complaint_ratio': complaint_ratio,
        'support_satisfaction_ratio': support_satisfaction_ratio,
        'nps_category': nps_category,
        'plan_tenure_mismatch': plan_tenure_mismatch,
        'usage_plan_mismatch': usage_plan_mismatch,
        'payment_stability': payment_stability,
        'nps_satisfaction_alignment': nps_satisfaction_alignment,
        'contract_value_risk': contract_value_risk,
        'lifecycle_stage': lifecycle_stage,
        'contract_tenure_ratio': contract_tenure_ratio,
        'tenure_category': tenure_category,
        'engagement_growth_rate': engagement_growth_rate,
        'tenure_stability': tenure_stability
    }
    
    return features


def prepare_features_for_prediction(features_dict, model):
    """Prepare features in the correct format for the model"""
    # Create a dataframe with the features
    df = pd.DataFrame([features_dict])
    
    # Apply one-hot encoding (same as training)
    df_encoded = pd.get_dummies(df, drop_first=True)
    
    # Get the feature names the model was trained on
    model_features = model.feature_names_in_
    
    # Add missing columns with 0s
    for col in model_features:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    
    # Ensure column order matches training
    df_encoded = df_encoded[model_features]
    
    return df_encoded


def plot_prediction_probability(probability):
    """Create a gauge chart for churn probability"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=probability * 100,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Churn Probability (%)", 'font': {'size': 24}},
        delta={'reference': 50, 'increasing': {'color': "red"}},
        gauge={
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 30], 'color': '#e8f5e9'},
                {'range': [30, 70], 'color': '#fff9c4'},
                {'range': [70, 100], 'color': '#ffebee'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 50
            }
        }
    ))
    
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    return fig


def plot_feature_importance(model, features_df, top_n=10):
    """Plot top N most important features"""
    feature_importance = pd.DataFrame({
        'feature': model.feature_names_in_,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False).head(top_n)
    
    fig = px.bar(
        feature_importance,
        x='importance',
        y='feature',
        orientation='h',
        title=f'Top {top_n} Most Important Features',
        labels={'importance': 'Importance Score', 'feature': 'Feature'},
        color='importance',
        color_continuous_scale='Blues'
    )
    
    fig.update_layout(
        height=400,
        showlegend=False,
        yaxis={'categoryorder': 'total ascending'}
    )
    
    return fig


def main():
    # Header
    st.markdown('<p class="main-header">🎯 Customer Churn Predictor</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">Predict customer churn risk using machine learning</p>',
        unsafe_allow_html=True
    )
    
    # Load model
    try:
        model = load_model()
        st.sidebar.success("✅ Model loaded successfully!")
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()
    
    # Load sample data
    sample_data = load_sample_data()
    
    # Sidebar - Input method selection
    st.sidebar.header("📥 Input Method")
    input_method = st.sidebar.radio(
        "Choose how to input customer data:",
        ["Manual Input", "Load Sample Customer", "Upload CSV"]
    )
    
    # Initialize default values
    default_values = {
        'age': 35,
        'gender': 'Male',
        'tenure_months': 12,
        'subscription_plan': 'Premium',
        'monthly_charges': 50.0,
        'contract_type': 'Monthly',
        'payment_method': 'Credit Card',
        'login_frequency_monthly': 15,
        'features_used': 5,
        'data_consumption_gb': 25.0,
        'days_since_last_activity': 5,
        'billing_issues_count': 0,
        'plan_changes': 0,
        'support_tickets': 1,
        'avg_resolution_hours': 12.0,
        'satisfaction_score': 4.0,
        'nps_score': 8
    }
    
    # Handle different input methods
    if input_method == "Load Sample Customer" and sample_data is not None:
        st.sidebar.subheader("Select a sample customer")
        customer_ids = sample_data['customer_id'].tolist()
        selected_customer_id = st.sidebar.selectbox("Customer ID", customer_ids)
        
        if selected_customer_id:
            customer_data = sample_data[sample_data['customer_id'] == selected_customer_id].iloc[0]
            default_values = {
                'age': int(customer_data['age']),
                'gender': customer_data['gender'],
                'tenure_months': int(customer_data['tenure_months']),
                'subscription_plan': customer_data['subscription_plan'],
                'monthly_charges': float(customer_data['monthly_charges']),
                'contract_type': customer_data['contract_type'],
                'payment_method': customer_data['payment_method'],
                'login_frequency_monthly': int(customer_data['login_frequency_monthly']),
                'features_used': int(customer_data['features_used']),
                'data_consumption_gb': float(customer_data['data_consumption_gb']),
                'days_since_last_activity': int(customer_data['days_since_last_activity']),
                'billing_issues_count': int(customer_data['billing_issues_count']),
                'plan_changes': int(customer_data['plan_changes']),
                'support_tickets': int(customer_data['support_tickets']),
                'avg_resolution_hours': float(customer_data['avg_resolution_hours']),
                'satisfaction_score': float(customer_data['satisfaction_score']),
                'nps_score': int(customer_data['nps_score'])
            }
            
            actual_churn = customer_data['churned']
            st.sidebar.info(f"Actual churn status: {'YES' if actual_churn == 1 else 'NO'}")
    
    # Main input form
    st.sidebar.header("👤 Customer Information")
    
    with st.sidebar.expander("📊 Demographics", expanded=True):
        age = st.slider("Age", 18, 80, default_values['age'])
        gender = st.selectbox("Gender", ["Male", "Female"], 
                             index=0 if default_values['gender'] == "Male" else 1)
        tenure_months = st.number_input("Tenure (months)", 1, 120, default_values['tenure_months'])
    
    with st.sidebar.expander("💳 Subscription Details", expanded=True):
        subscription_plan = st.selectbox(
            "Subscription Plan",
            ["Basic", "Standard", "Premium"],
            index=["Basic", "Standard", "Premium"].index(default_values['subscription_plan'])
        )
        monthly_charges = st.number_input("Monthly Charges ($)", 10.0, 200.0, default_values['monthly_charges'])
        contract_type = st.selectbox(
            "Contract Type",
            ["Monthly", "Annual", "Two-Year"],
            index=["Monthly", "Annual", "Two-Year"].index(default_values['contract_type'])
        )
        payment_method = st.selectbox(
            "Payment Method",
            ["Credit Card", "Bank Transfer", "Digital Wallet"],
            index=["Credit Card", "Bank Transfer", "Digital Wallet"].index(default_values['payment_method'])
        )
    
    with st.sidebar.expander("📈 Usage Metrics", expanded=True):
        login_frequency_monthly = st.number_input(
            "Login Frequency (per month)", 0, 100, default_values['login_frequency_monthly']
        )
        features_used = st.slider("Features Used", 1, 10, default_values['features_used'])
        data_consumption_gb = st.number_input(
            "Data Consumption (GB/month)", 0.0, 200.0, default_values['data_consumption_gb']
        )
        days_since_last_activity = st.number_input(
            "Days Since Last Activity", 0, 60, default_values['days_since_last_activity']
        )
    
    with st.sidebar.expander("🔧 Support & Satisfaction", expanded=True):
        billing_issues_count = st.number_input(
            "Billing Issues", 0, 10, default_values['billing_issues_count']
        )
        plan_changes = st.number_input("Plan Changes", 0, 10, default_values['plan_changes'])
        support_tickets = st.number_input(
            "Support Tickets", 0, 20, default_values['support_tickets']
        )
        avg_resolution_hours = st.number_input(
            "Avg Resolution Time (hours)", 0.0, 100.0, default_values['avg_resolution_hours']
        )
        satisfaction_score = st.slider(
            "Satisfaction Score", 1.0, 5.0, default_values['satisfaction_score'], 0.1
        )
        nps_score = st.slider("NPS Score", 0, 10, default_values['nps_score'])
    
    # Predict button
    predict_button = st.sidebar.button("🔮 Predict Churn", type="primary", use_container_width=True)
    
    # Main content area
    if predict_button:
        with st.spinner("Analyzing customer data..."):
            # Create features
            features = create_feature_dict(
                age, gender, tenure_months, subscription_plan, monthly_charges,
                contract_type, payment_method, login_frequency_monthly, features_used,
                data_consumption_gb, days_since_last_activity, billing_issues_count,
                plan_changes, support_tickets, avg_resolution_hours, satisfaction_score,
                nps_score
            )
            
            # Prepare for prediction
            features_df = prepare_features_for_prediction(features, model)
            
            # Make prediction
            prediction = model.predict(features_df)[0]
            probability = model.predict_proba(features_df)[0]
            churn_probability = probability[1]
            
            # Display results
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.subheader("🎯 Prediction Result")
                
                if prediction == 1:
                    st.markdown(
                        f'<div class="prediction-box churn-yes">⚠️ HIGH RISK - Customer Likely to Churn</div>',
                        unsafe_allow_html=True
                    )
                    st.error(f"**Churn Probability: {churn_probability*100:.1f}%**")
                    st.markdown("### 🚨 Recommended Actions:")
                    st.markdown("""
                    - 📞 Immediate outreach by retention team
                    - 🎁 Offer personalized retention incentives
                    - 💬 Schedule customer satisfaction call
                    - 🔍 Investigate pain points and complaints
                    - 💰 Consider pricing adjustments or upgrades
                    """)
                else:
                    st.markdown(
                        f'<div class="prediction-box churn-no">✅ LOW RISK - Customer Likely to Stay</div>',
                        unsafe_allow_html=True
                    )
                    st.success(f"**Retention Probability: {(1-churn_probability)*100:.1f}%**")
                    st.markdown("### 💡 Recommended Actions:")
                    st.markdown("""
                    - 🌟 Continue providing excellent service
                    - 📈 Look for upsell opportunities
                    - 🤝 Build loyalty through engagement programs
                    - 📧 Share new features and updates
                    - 🎯 Consider referral incentives
                    """)
                
                # Probability gauge
                st.plotly_chart(plot_prediction_probability(churn_probability), use_container_width=True)
            
            with col2:
                st.subheader("📊 Customer Profile Summary")
                
                # Key metrics
                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("Tenure", f"{tenure_months} months")
                    st.metric("Monthly Charges", f"${monthly_charges:.2f}")
                    st.metric("Satisfaction", f"{satisfaction_score:.1f}/5.0")
                
                with col_b:
                    st.metric("Login Frequency", f"{login_frequency_monthly}/month")
                    st.metric("Support Tickets", support_tickets)
                    st.metric("NPS Score", f"{nps_score}/10")
                
                # Risk factors
                st.markdown("### ⚠️ Risk Factors Detected:")
                risk_factors = []
                
                if days_since_last_activity > 14:
                    risk_factors.append(f"❌ Inactive for {days_since_last_activity} days")
                if satisfaction_score < 3.0:
                    risk_factors.append("❌ Low satisfaction score")
                if support_tickets > 3:
                    risk_factors.append(f"❌ High support tickets ({support_tickets})")
                if billing_issues_count > 0:
                    risk_factors.append(f"❌ Billing issues ({billing_issues_count})")
                if login_frequency_monthly < 5:
                    risk_factors.append("❌ Low engagement")
                if nps_score < 7:
                    risk_factors.append("❌ Low NPS (Detractor)")
                
                if risk_factors:
                    for factor in risk_factors:
                        st.markdown(f"- {factor}")
                else:
                    st.success("✅ No significant risk factors detected")
            
            # Feature importance
            st.subheader("🔍 Model Feature Importance")
            st.plotly_chart(plot_feature_importance(model, features_df), use_container_width=True)
            
            # Detailed features (expandable)
            with st.expander("📋 View All Computed Features"):
                features_display = pd.DataFrame([features]).T
                features_display.columns = ['Value']
                st.dataframe(features_display, use_container_width=True)
    
    else:
        # Welcome message when no prediction yet
        st.info("👈 Configure customer details in the sidebar and click **Predict Churn** to see results")
        
        # Show model info
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 🤖 Model Info")
            st.markdown(f"""
            - **Algorithm**: Random Forest
            - **Features**: {len(model.feature_names_in_)}
            - **Trees**: {model.n_estimators}
            """)
        
        with col2:
            st.markdown("### 📈 Performance")
            st.markdown("""
            - **Accuracy**: See training notebook
            - **Precision**: Optimized for recall
            - **Validation**: 5-fold CV
            """)
        
        with col3:
            st.markdown("### 💡 How It Works")
            st.markdown("""
            1. Enter customer details
            2. Model analyzes patterns
            3. Get churn prediction
            4. View recommendations
            """)
        
        # Sample data preview
        if sample_data is not None:
            st.subheader("📊 Sample Customer Data")
            st.dataframe(sample_data.head(10), use_container_width=True)


if __name__ == "__main__":
    main()
