"""
train_model.py
---------------
Trains a REAL machine learning model on the studentInfo.csv dataset
(OULAD - Open University Learning Analytics Dataset).

Target: final_result -> one of: Pass, Fail, Withdrawn, Distinction
(multi-class classification, kept as-is per project decision).

Run this once to produce risk_model.pkl, which app.py/model.py
will load at runtime.

Usage:
    python train_model.py
"""

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score

DATA_PATH = "../data/studentInfo.csv"
MODEL_PATH = "risk_model.pkl"

CATEGORICAL_FEATURES = [
    "code_module", "code_presentation", "gender", "region",
    "highest_education", "imd_band", "age_band", "disability",
]
NUMERIC_FEATURES = ["num_of_prev_attempts", "studied_credits"]
TARGET = "final_result"


def main():
    df = pd.read_csv(DATA_PATH)

    X = df[CATEGORICAL_FEATURES + NUMERIC_FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    preprocessor = ColumnTransformer(transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES),
        ("num", "passthrough", NUMERIC_FEATURES),
    ])

    pipeline = Pipeline(steps=[
        ("preprocess", preprocessor),
        ("classifier", RandomForestClassifier(
            n_estimators=200, max_depth=12, random_state=42, n_jobs=-1
        )),
    ])

    print("Training model on", len(X_train), "students...")
    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    print("\nAccuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    joblib.dump(pipeline, MODEL_PATH)
    print(f"\nModel saved to {MODEL_PATH}")


if __name__ == "__main__":
    main()
