"""
llm_service.py
---------------
Wraps the call to the Claude API so app.py doesn't need to know
API details. This is Step 2 (API Integration) reused here.

NOTE: requires an ANTHROPIC_API_KEY environment variable to actually
call the real API. If it's missing, falls back to a mock response
so the rest of the app (backend/frontend) can still be developed
and demoed without a live key.
"""

import os
from prompt_engineering import SYSTEM_PROMPT, build_prompt, StudentRiskProfile

USE_MOCK = os.environ.get("ANTHROPIC_API_KEY") is None


def generate_recommendation(profile: StudentRiskProfile) -> str:
    if USE_MOCK:
        return _mock_recommendation(profile)

    import anthropic
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=200,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": build_prompt(profile)}]
    )
    return response.content[0].text.strip()


def _mock_recommendation(profile: StudentRiskProfile) -> str:
    """Used only when no API key is set, so the app is still testable."""
    if profile.risk_level == "High":
        return ("[MOCK] Critical risk detected. Recommend an immediate "
                "advisor meeting and tutoring referral this week.")
    elif profile.risk_level == "Medium":
        return ("[MOCK] Moderate risk. Recommend an instructor check-in "
                "and assignment reminders.")
    else:
        return "[MOCK] No intervention needed. Continue routine monitoring."
