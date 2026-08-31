from pathlib import Path

import joblib
import pandas as pd

MODEL_DIR = Path(__file__).resolve().parent.parent / "models"

_pipeline = joblib.load(MODEL_DIR / "model.pkl")
_label_encoder = joblib.load(MODEL_DIR / "label_encoder.pkl")

FEATURE_COLUMNS = [
    "sleep_duration",
    "heart_rate",
    "bmi",
    "calorie_expenditure",
    "step_count",
    "exercise_duration",
    "water_intake",
    "diet_type",
    "stress_level",
    "sleep_quality",
    "physical_activity_level",
    "smoking_alcohol",
    "gender",
]


def predict(input_dict: dict) -> dict:
    row = pd.DataFrame([input_dict], columns=FEATURE_COLUMNS)

    pred_encoded = _pipeline.predict(row)[0]
    pred_label = _label_encoder.inverse_transform([pred_encoded])[0]

    proba = _pipeline.predict_proba(row)[0]
    class_names = _label_encoder.inverse_transform(range(len(proba)))
    proba_dict = {name: float(p) for name, p in zip(class_names, proba)}

    return {
        "health_condition": pred_label,
        "probabilities": proba_dict,
    }