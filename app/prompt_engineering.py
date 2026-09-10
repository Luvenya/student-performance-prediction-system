"""
prompt_engineering.py
----------------------
Builds prompts for the LLM based on the REAL OULAD dataset fields
(no GPA/attendance - this dataset uses demographic + enrollment data).
"""

from dataclasses import dataclass


@dataclass
class StudentRiskProfile:
    student_id: str
    risk_level: str            # "Low" | "Medium" | "High"  (derived, for display)
    predicted_result: str      # "Pass" | "Fail" | "Withdrawn" | "Distinction"
    gender: str
    region: str
    highest_education: str
    num_of_prev_attempts: int
    studied_credits: int
    disability: str


SYSTEM_PROMPT = """You are an academic advisor assistant embedded in a
university early-warning system. You receive a student's predicted
academic outcome and background data, and must produce ONE short,
actionable intervention recommendation for the instructor or advisor.

Rules:
- Be specific and actionable (avoid vague advice like "help the student").
- Base your recommendation on the actual factors given (prior attempts,
  credit load, predicted outcome).
- Keep the response to 2-3 sentences maximum.
- Do not repeat the raw data back verbatim; interpret it.
- Tone: professional, supportive, concise.
- Output plain text only (no markdown, no headers).
"""


FEW_SHOT_EXAMPLES = [
    {
        "input": "Predicted: Fail | Prev Attempts: 2 | Studied Credits: 120 | Disability: N",
        "output": "This student has failed before and is currently carrying a "
                  "heavy credit load, which may be compounding the risk. "
                  "Recommend a course-load review with an academic advisor "
                  "and early referral to subject-specific tutoring."
    },
    {
        "input": "Predicted: Withdrawn | Prev Attempts: 0 | Studied Credits: 60 | Disability: Y",
        "output": "First-time student at risk of withdrawal; disability status "
                  "suggests accessibility support may be a factor. Recommend "
                  "a check-in from the disability support office alongside "
                  "the academic advisor."
    },
    {
        "input": "Predicted: Distinction | Prev Attempts: 0 | Studied Credits: 60 | Disability: N",
        "output": "No intervention needed at this time. Student is on track "
                  "for a strong outcome; continue routine monitoring."
    },
]


def format_student_data(profile: StudentRiskProfile) -> str:
    return (
        f"Predicted: {profile.predicted_result} | "
        f"Prev Attempts: {profile.num_of_prev_attempts} | "
        f"Studied Credits: {profile.studied_credits} | "
        f"Disability: {profile.disability}"
    )


def build_prompt(profile: StudentRiskProfile) -> str:
    examples_block = "\n\n".join(
        f"Student data: {ex['input']}\nRecommendation: {ex['output']}"
        for ex in FEW_SHOT_EXAMPLES
    )

    student_block = format_student_data(profile)

    prompt = f"""Here are examples of the expected output format:

{examples_block}

Now generate a recommendation for this student:

Student data: {student_block}
Recommendation:"""

    return prompt


if __name__ == "__main__":
    test_student = StudentRiskProfile(
        student_id="12345",
        risk_level="High",
        predicted_result="Fail",
        gender="M",
        region="Scotland",
        highest_education="A Level or Equivalent",
        num_of_prev_attempts=2,
        studied_credits=120,
        disability="N",
    )
    print(SYSTEM_PROMPT)
    print(build_prompt(test_student))
