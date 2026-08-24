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
    echo "   uv run python src/customer_churn_prediction/05_hyperparam_tuning.py"
    echo ""
    read -p "Do you want to continue anyway? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ Error: uv not found. Install it first:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Make sure dependencies are installed
echo "📦 Syncing dependencies..."
uv sync
echo ""

# Launch the app
echo "🚀 Launching Streamlit app..."
echo ""
echo "   The app will open in your browser at:"
echo "   http://localhost:8501"
echo ""
echo "   Press Ctrl+C to stop the server"
echo ""

uv run streamlit run app/streamlit_app.py
