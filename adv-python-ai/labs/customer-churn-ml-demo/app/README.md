# Customer Churn Prediction - Streamlit App

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Navigate to project directory
cd customer-churn-ml-demo

# Install deployment requirements
pip install -r requirements.txt
```

### 2. Run the App

```bash
# From the project root directory
streamlit run app/streamlit_app.py

# Alternatively, use the provided script
./scripts/run_app.sh
```

The app will open automatically in your browser at `http://localhost:8501`

---

## 📱 Features

### 🎯 Interactive Prediction Interface

- **Manual Input**: Enter customer details using intuitive form controls
- **Sample Customer**: Load pre-existing customers from the dataset
- **CSV Upload**: Batch predict multiple customers (coming soon)

### 📊 Visual Analytics

- **Churn Probability Gauge**: Visual indicator of churn risk (0-100%)
- **Risk Classification**: Color-coded HIGH/LOW risk predictions
- **Feature Importance**: See which factors influence predictions most
- **Customer Profile Summary**: Quick overview of key metrics

### 💡 Actionable Insights

- **Risk Factors**: Automatically detected warning signs
- **Recommendations**: Tailored retention strategies based on risk level
- **Performance Metrics**: Model transparency and confidence scores

---

## 🎮 How to Use

### Method 1: Manual Input

1. Select "Manual Input" in the sidebar
2. Fill in customer information across different sections:
   - Demographics (age, gender, tenure)
   - Subscription details (plan, charges, contract)
   - Usage metrics (logins, features, data consumption)
   - Support & satisfaction (tickets, scores)
3. Click "🔮 Predict Churn"
4. View results and recommendations

### Method 2: Load Sample Customer

1. Select "Load Sample Customer" in the sidebar
2. Choose a customer ID from the dropdown
3. Click "🔮 Predict Churn"
4. Compare prediction with actual churn status

---

## 📐 App Architecture

```
streamlit_app.py
├── load_model()              # Cached model loading
├── load_sample_data()        # Load reference data
├── create_feature_dict()     # Feature engineering
├── prepare_features()        # Encode for model
├── plot_probability()        # Gauge visualization
├── plot_importance()         # Feature importance chart
└── main()                    # App orchestration
```

---

## 🎨 User Interface Sections

### Sidebar (Input)

- Input method selection
- Demographics expander
- Subscription details expander
- Usage metrics expander
- Support & satisfaction expander
- Predict button

### Main Area (Output)

- Prediction result (HIGH/LOW RISK)
- Churn probability gauge
- Recommended actions
- Customer profile summary
- Risk factors detected
- Feature importance chart
- Detailed features (expandable)

---

## 🔧 Configuration

### Custom Styling

The app uses custom CSS for:

- Color-coded prediction boxes (red for high risk, green for low risk)
- Professional metric cards
- Responsive layout
- Consistent branding

### Model Requirements

- Trained model must be saved at: `models/tuned_churn_model.pkl`
- Must be a scikit-learn model with `predict_proba()` method
- Feature names must match training data

---

## 📊 Example Scenarios

### High Risk Customer

- Low satisfaction score (< 3.0)
- Inactive (> 14 days since last activity)
- High support tickets (> 3)
- Low engagement (< 5 logins/month)
- **Result**: 70-90% churn probability

### Low Risk Customer

- High satisfaction (> 4.0)
- Active (< 3 days since last activity)
- Minimal support needs (0-1 tickets)
- High engagement (> 20 logins/month)
- **Result**: 10-30% churn probability

---

## 🚀 Production Deployment

### Local Development

```bash
streamlit run app/streamlit_app.py
```

### Streamlit Cloud

1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Set app path: `app/streamlit_app.py`
4. Deploy

### Docker (Optional)

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements-deploy.txt
EXPOSE 8501
CMD ["streamlit", "run", "app/streamlit_app.py", "--server.address", "0.0.0.0"]
```

---

## 🛠️ Troubleshooting

### Model Not Found

**Error**: "Model not found at models/tuned_churn_model.pkl"
**Solution**: Train the model first by running:

```bash
python src/05_hyperparam_tuning.py
```

### Import Errors

**Error**: "ModuleNotFoundError: No module named 'streamlit'"
**Solution**: Install dependencies:

```bash
pip install -r requirements-deploy.txt
```

### Feature Mismatch

**Error**: Features don't match training data
**Solution**: Ensure feature engineering matches training pipeline

---

## 📈 Performance Tips

### For Better Performance

- Model loading is cached (`@st.cache_resource`)
- Sample data is cached (`@st.cache_data`)
- Use `use_container_width=True` for responsive charts
- Minimize reloads by organizing code efficiently

### For Production

- Consider using a reverse proxy (nginx)
- Enable HTTPS
- Set up monitoring and logging
- Implement rate limiting
- Add authentication if needed

---

## 🎯 Next Steps

### Enhancements to Consider

1. **Batch Predictions**: Upload CSV with multiple customers
2. **Model Explainability**: Add SHAP values for individual predictions
3. **Historical Tracking**: Store predictions and track accuracy over time
4. **A/B Testing**: Compare multiple models
5. **Feedback Loop**: Allow users to report prediction accuracy
6. **Export Reports**: Generate PDF reports of predictions

### Integration Options

- Connect to CRM system for real-time data
- Add webhook notifications for high-risk customers
- Integrate with email marketing for automated campaigns
- Build REST API wrapper (FastAPI) for programmatic access

---

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Plotly Charts](https://plotly.com/python/)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)

---

## 📝 License & Credits

Built for customer churn prediction demonstration.
Uses Random Forest model trained on customer subscription data.
