"""
app.py
------
Main backend server (Flask), running on the FULL OULAD dataset
(studentInfo.csv, ~32,593 students - no sampling, no data modified).

Predictions for ALL students are computed ONCE at server startup
(vectorized, fast) and kept in memory, so /students requests stay
fast even with 32k+ rows.

Endpoints:
  GET  /students              -> paginated list (supports ?page, ?per_page,
                                   ?search=<id>, ?risk=<Low|Medium|High>,
                                   ?region=<name>)
  GET  /students/<id>         -> full details + recommendation for one student
  GET  /meta                   -> total count + distinct regions (for filter UI)
  POST /predict                 -> predict result for arbitrary input data
  POST /recommend                -> generate a recommendation for arbitrary input

Run locally with:
  python app.py
Then open: http://127.0.0.1:5000/students
"""

import os
import pandas as pd
from flask import Flask, jsonify, request

from model import predict_batch, predict_final_result, risk_label_from_result
from llm_service import generate_recommendation
from prompt_engineering import StudentRiskProfile

app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response


DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "studentInfo.csv")

# ---------------------------------------------------------------------
# Load the full dataset ONCE and pre-compute predictions for everyone.
# This runs a single time at server startup, not per-request.
# ---------------------------------------------------------------------
print("Loading dataset...")
_df = pd.read_csv(DATA_PATH)
_df = _df.drop_duplicates(subset="id_student").reset_index(drop=True)

print(f"Running predictions for {len(_df)} students (one-time, at startup)...")
_df["predicted_result"] = predict_batch(_df)
_df["risk_level"] = _df["predicted_result"].apply(risk_label_from_result)
print("Done. Server ready.")


def build_profile_from_row(row: pd.Series) -> StudentRiskProfile:
    return StudentRiskProfile(
        student_id=str(row["id_student"]),
        risk_level=row["risk_level"],
        predicted_result=row["predicted_result"],
        gender=row["gender"],
        region=row["region"],
        highest_education=row["highest_education"],
        num_of_prev_attempts=int(row["num_of_prev_attempts"]),
        studied_credits=int(row["studied_credits"]),
        disability=row["disability"],
    )


@app.route("/meta", methods=["GET"])
def get_meta():
    return jsonify({
        "total_students": len(_df),
        "regions": sorted(_df["region"].unique().tolist()),
        "risk_levels": ["High", "Medium", "Low"],
    })


@app.route("/students", methods=["GET"])
def get_students():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 50))
    search = request.args.get("search", "").strip()
    risk_filter = request.args.get("risk", "").strip()
    region_filter = request.args.get("region", "").strip()

    filtered = _df
    if search:
        filtered = filtered[filtered["id_student"].astype(str).str.contains(search)]
    if risk_filter:
        filtered = filtered[filtered["risk_level"] == risk_filter]
    if region_filter:
        filtered = filtered[filtered["region"] == region_filter]

    total = len(filtered)
    start = (page - 1) * per_page
    end = start + per_page
    page_df = filtered.iloc[start:end]

    result = [{
        "student_id": str(r["id_student"]),
        "region": r["region"],
        "highest_education": r["highest_education"],
        "studied_credits": int(r["studied_credits"]),
        "actual_result": r["final_result"],
        "predicted_result": r["predicted_result"],
        "risk_level": r["risk_level"],
    } for _, r in page_df.iterrows()]

    return jsonify({
        "students": result,
        "total": total,
        "page": page,
        "per_page": per_page,
        "total_pages": (total + per_page - 1) // per_page,
    })


@app.route("/students/<student_id>", methods=["GET"])
def get_student_detail(student_id):
    match = _df[_df["id_student"].astype(str) == student_id]
    if match.empty:
        return jsonify({"error": "Student not found"}), 404

    row = match.iloc[0]
    profile = build_profile_from_row(row)
    recommendation = generate_recommendation(profile)

    return jsonify({
        "student_id": str(row["id_student"]),
        "gender": row["gender"],
        "region": row["region"],
        "highest_education": row["highest_education"],
        "age_band": row["age_band"],
        "num_of_prev_attempts": int(row["num_of_prev_attempts"]),
        "studied_credits": int(row["studied_credits"]),
        "disability": row["disability"],
        "actual_result": row["final_result"],
        "predicted_result": row["predicted_result"],
        "risk_level": row["risk_level"],
        "recommendation": recommendation,
    })


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    try:
        predicted_result = predict_final_result(data)
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e}"}), 400

    risk_level = risk_label_from_result(predicted_result)
    return jsonify({"predicted_result": predicted_result, "risk_level": risk_level})


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    try:
        profile = StudentRiskProfile(**data)
    except TypeError as e:
        return jsonify({"error": f"Invalid input: {e}"}), 400

    recommendation = generate_recommendation(profile)
    return jsonify({"recommendation": recommendation})


if __name__ == "__main__":
    app.run(debug=True, port=5000, use_reloader=False)
