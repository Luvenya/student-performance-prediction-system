"""
model.py
--------
Loads the REAL trained ML model (risk_model.pkl, produced by
train_model.py) and predicts a student's final_result.

Dataset: OULAD (studentInfo.csv)
Target (multi-class, kept as-is): Pass | Fail | Withdrawn | Distinction

Run `python train_model.py` once before using this if risk_model.pkl
doesn't exist yet.
"""

import os
import joblib
import pandas as pd

MODEL_PATH = os.path.join(os.path.dirname(__file__), "risk_model.pkl")
_model = None


def _load_model():
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(
                "risk_model.pkl not found. Run 'python train_model.py' first."
            )
        _model = joblib.load(MODEL_PATH)
    return _model


def predict_final_result(student: dict) -> str:
    """
    Takes a dict with the OULAD feature columns and returns the
    predicted class: "Pass" | "Fail" | "Withdrawn" | "Distinction"
    """
    model = _load_model()

    row = pd.DataFrame([{
        "code_module": student["code_module"],
        "code_presentation": student["code_presentation"],
        "gender": student["gender"],
        "region": student["region"],
        "highest_education": student["highest_education"],
        "imd_band": student["imd_band"],
        "age_band": student["age_band"],
        "disability": student["disability"],
        "num_of_prev_attempts": student["num_of_prev_attempts"],
        "studied_credits": student["studied_credits"],
    }])

    prediction = model.predict(row)[0]
    return prediction


def predict_batch(df: pd.DataFrame) -> pd.Series:
    """
    Predicts final_result for an entire DataFrame at once (fast,
    vectorized) instead of row-by-row. Used to pre-compute predictions
    for all 32k+ students once at server startup.
    """
    model = _load_model()
    features = df[[
        "code_module", "code_presentation", "gender", "region",
        "highest_education", "imd_band", "age_band", "disability",
        "num_of_prev_attempts", "studied_credits",
    ]]
    return model.predict(features)


def risk_label_from_result(result: str) -> str:
    """
    Maps the 4-class prediction to a risk badge color for the
    dashboard UI (display purposes only - the underlying prediction
    stays multi-class, per project decision).
    """
    mapping = {
        "Fail": "High",
        "Withdrawn": "High",
        "Pass": "Medium",
        "Distinction": "Low",
    }
    return mapping.get(result, "Medium")
