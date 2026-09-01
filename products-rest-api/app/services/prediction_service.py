import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path(__file__).parent.parent.parent / "artifacts" / "tuned_churn_model.pkl"


model = joblib.load(MODEL_PATH)


def predict(data: dict):
    # The saved model is a full scikit-learn Pipeline
    # (ColumnTransformer -> OneHotEncoder + RandomForestClassifier), so it does
    # its own encoding. Hand it the raw feature row in the exact column order it
    # was trained on -- no manual get_dummies / reindex.
    #
    # The previous version ran pd.get_dummies(drop_first=True) on a single row:
    # with one row every categorical has a single value, drop_first removes it,
    # so zero dummy columns were produced and reindex filled every encoded
    # feature with 0. The model then saw an all-zero vector and always returned
    # prediction 0 / probability 0.5.
    df = pd.DataFrame([data])[list(model.feature_names_in_)]

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0].max()

    return {
        "prediction": int(prediction),
        "probability": float(probability),
    }
