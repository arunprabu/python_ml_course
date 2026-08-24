# 🚀 Quick Start Guide - Streamlit App

## Your Streamlit App is Now Running! 🎉

### 📍 Access the App

Open your browser and navigate to:

- **Local URL**: http://localhost:8501
- **Network URL**: http://10.50.4.205:8501

---

## 🎯 How to Use the App

### Step 1: Choose Input Method (Sidebar)

Three options available:

1. **Manual Input** - Fill in customer details manually
2. **Load Sample Customer** - Select from existing customers
3. **Upload CSV** - Batch predictions (coming soon)

### Step 2: Enter Customer Information

Fill in the expandable sections:

- 📊 **Demographics**: Age, Gender, Tenure
- 💳 **Subscription Details**: Plan, Charges, Contract Type
- 📈 **Usage Metrics**: Logins, Features Used, Data Consumption
- 🔧 **Support & Satisfaction**: Tickets, Satisfaction Score, NPS

### Step 3: Get Prediction

Click the **🔮 Predict Churn** button

### Step 4: Review Results

The app will show:

- ✅/⚠️ Churn risk classification (HIGH/LOW)
- 📊 Churn probability gauge (0-100%)
- 💡 Recommended retention actions
- 📈 Customer profile summary
- ⚠️ Risk factors detected
- 🔍 Feature importance chart

---

## 🎮 Try These Example Scenarios

### High-Risk Customer Example

Try these values to see a high-risk prediction:

- Satisfaction Score: **2.0**
- Days Since Last Activity: **25**
- Support Tickets: **5**
- Login Frequency: **3** per month
- Billing Issues: **2**

**Expected Result**: 70-90% churn probability

### Low-Risk Customer Example

Try these values to see a low-risk prediction:

- Satisfaction Score: **4.5**
- Days Since Last Activity: **1**
- Support Tickets: **0**
- Login Frequency: **25** per month
- Billing Issues: **0**

**Expected Result**: 10-30% churn probability

---

## 🔄 Testing with Sample Data

### Option 1: Quick Test

1. In sidebar, select **"Load Sample Customer"**
2. Choose any Customer ID from dropdown
3. Click **Predict Churn**
4. Compare prediction with actual churn status (shown below customer selector)

### Option 2: Modify Sample

1. Load a sample customer
2. Modify one or more values
3. See how prediction changes
4. Understand which factors influence churn most

---

## 🛑 How to Stop the App

Press **Ctrl + C** in the terminal where the app is running

---

## 🔧 Features Demonstrated

### ✨ Interactive UI Components

- Sliders for numeric values
- Dropdowns for categorical choices
- Number inputs for precise values
- Expandable sections for organized input
- Color-coded results

### 📊 Visualizations

- **Gauge Chart**: Shows churn probability visually
- **Bar Chart**: Displays feature importance
- **Metrics Cards**: Key customer statistics
- **Data Table**: Detailed feature values

### 💡 Business Intelligence

- Automatic risk factor detection
- Tailored retention recommendations
- Customer lifecycle stage identification
- Engagement metrics analysis

---

## 🎨 UI Color Coding

- 🟢 **Green** = Low risk, customer likely to stay
- 🟡 **Yellow** = Moderate risk, monitor closely
- 🔴 **Red** = High risk, immediate action needed

---

## 📱 App Structure

```
┌─────────────────────────────────────────────┐
│  🎯 Customer Churn Predictor                │
│  Predict customer churn risk using ML      │
├─────────────────────────────────────────────┤
│                                             │
│  Sidebar (Left)          Main Area (Right) │
│  ├─ Input Method         ├─ Prediction     │
│  ├─ Demographics         ├─ Probability    │
│  ├─ Subscription         ├─ Actions        │
│  ├─ Usage Metrics        ├─ Profile        │
│  ├─ Support              ├─ Risk Factors   │
│  └─ [Predict Button]     └─ Feature Imp.   │
│                                             │
└─────────────────────────────────────────────┘
```

---

## 💻 Command Reference

### Run the App

```bash
cd customer-churn-ml-demo
streamlit run app/streamlit_app.py
```

### Quick Launch (using script)

```bash
cd customer-churn-ml-demo
./run_app.sh
```

### Install Dependencies

```bash
pip install -r requirements-deploy.txt
```

---

## 🎓 Learning Points

This app demonstrates:

1. **Model Deployment**: How to serve ML models via web interface
2. **Feature Engineering**: Real-time computation of derived features
3. **User Experience**: Making ML accessible to non-technical users
4. **Visualization**: Presenting predictions with context
5. **Business Value**: Translating predictions into actions

---

## 📚 Next Steps

### Explore the Code

- `app/streamlit_app.py` - Main application logic
- Feature engineering functions
- Prediction pipeline
- Visualization components

### Customize the App

- Modify the color scheme
- Add new visualizations
- Include additional metrics
- Connect to live data sources

### Deploy to Production

- Streamlit Cloud (free hosting)
- Docker container
- AWS/Azure/GCP
- Add authentication

---

## ❓ Troubleshooting

### Port Already in Use

```bash
streamlit run app/streamlit_app.py --server.port 8502
```

### Model Not Loading

Check that `models/tuned_churn_model.pkl` exists

### Missing Dependencies

```bash
pip install streamlit plotly joblib pandas scikit-learn
```

---

## 🎉 Enjoy Your Churn Prediction App!

The app is now running and ready to demo. Try different customer profiles and see how the model predicts churn risk in real-time!
