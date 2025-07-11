from judgeval.tracer import Tracer
from judgeval.judgment_client import JudgmentClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Judgment SDK client (auto-loads from env)
judgment = JudgmentClient()
print("Successfully initialized JudgmentClient!")

Tracer(project_name=os.getenv("JUDGMENT_PROJECT_NAME")).observe(span_type="function")
def generate_referral_email(user_info: dict) -> str:
    """
    Generate a professional referral request email based on the given user information.

    Args:
        user_info (dict): Dictionary containing:
            - 'target_name': Name of the person to ask for referral
            - 'target_company': Company where referral is sought
            - 'target_role': Role applied for
            - 'reason': Motivation for applying
            - 'your_name': Name of the sender

    Returns:
        str: Formatted referral request email string

    Notes:
        This function is called in the main agent script (run_referral.py) to produce the actual email content.
        Uses judgeval's tracer to record and monitor function execution during evaluation.
    """

    # Safely access dictionary fields to avoid runtime errors
    target_name = user_info.get("target_name", "there")
    target_company = user_info.get("target_company", "the company")
    target_role = user_info.get("target_role", "the role")
    reason = user_info.get("reason", "I'm passionate about this opportunity.")
    your_name = user_info.get("your_name", "Your Name")

    # Construct the referral email using formatted multi-line string
    email = f"""
Subject: Request for Referral to {target_company}

Hi {target_name},

I hope you're doing well! I recently came across an exciting opportunity for a {target_role} role at {target_company} and immediately thought of reaching out to you.

Given your experience and connection with the company, I'd be incredibly grateful if you'd consider referring me for the role. {reason} is one of the main reasons I am interested in this role.

If you're open to it, I’d be happy to send over my resume and any other details you may need. Thanks in advance for considering this — I really appreciate your time and support.

Warm regards,  
{your_name}
"""
    return email
