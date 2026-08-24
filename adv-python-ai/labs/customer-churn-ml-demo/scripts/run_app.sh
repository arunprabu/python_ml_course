#!/bin/bash

# Customer Churn Prediction - Streamlit App Launcher
# This script checks dependencies and launches the Streamlit app

echo "=================================================="
echo "  Customer Churn Prediction - Streamlit App"
echo "=================================================="
echo ""

# Check if we're in the correct directory
if [ ! -f "app/streamlit_app.py" ]; then
    echo "❌ Error: Please run this script from the customer-churn-ml-demo directory"
    echo "   cd customer-churn-ml-demo"
    echo "   ./scripts/run_app.sh"
    exit 1
fi

# Check if model exists
if [ ! -f "models/tuned_churn_model.pkl" ]; then
    echo "⚠️  Warning: Model file not found!"
    echo "   Please train the model first by running:"
    echo "   python src/05_hyperparam_tuning.py"
    echo ""
    read -p "Do you want to continue anyway? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "📦 Streamlit not found. Installing dependencies..."
    pip install -r requirements-deploy.txt
    echo ""
fi

# Launch the app
echo "🚀 Launching Streamlit app..."
echo ""
echo "   The app will open in your browser at:"
echo "   http://localhost:8501"
echo ""
echo "   Press Ctrl+C to stop the server"
echo ""

streamlit run app/streamlit_app.py
