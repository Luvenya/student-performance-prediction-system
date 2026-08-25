import streamlit as st
import pandas as pd
from pathlib import Path

# Page settings
st.set_page_config(
    page_title="Student Performance Detection System",
    page_icon="🎓"
)

# Find the project folder
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Dataset location
DATA_FILE = PROJECT_ROOT / "data" / "studentInfo.csv"

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv(DATA_FILE)

df = load_data()

# Title
st.title("🎓 Student Performance Detection System")

st.write(
    "Initial prototype for detecting students who may be at academic risk."
)

st.subheader("Student Information")

# Student ID input
student_id = st.text_input(
    "Enter Student ID",
    placeholder="Example: 28400"
)

# Search student
if student_id:

    try:
        student_id = int(student_id)

        student = df[df["id_student"] == student_id]

        if not student.empty:

            student = student.iloc[0]

            st.success("Student record found!")

            st.write("### Student Details")

            col1, col2 = st.columns(2)

            with col1:
                st.write("**Gender:**", student["gender"])
                st.write("**Region:**", student["region"])
                st.write(
                    "**Highest Education:**",
                    student["highest_education"]
                )
                st.write("**Age Band:**", student["age_band"])

            with col2:
                st.write(
                    "**Previous Attempts:**",
                    student["num_of_prev_attempts"]
                )
                st.write(
                    "**Studied Credits:**",
                    student["studied_credits"]
                )
                st.write(
                    "**Disability:**",
                    student["disability"]
                )

            st.info(
                "Student information has been successfully loaded "
                "from the OULAD dataset."
            )

        else:
            st.warning("Student ID not found in the dataset.")

    except ValueError:
        st.error("Please enter a valid numeric Student ID.")