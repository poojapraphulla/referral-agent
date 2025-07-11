from referral_agent import generate_referral_email
from referral_scorer import ReferralScorer
from judgeval.judgment_client import JudgmentClient
from judgeval.data import Example
from dotenv import load_dotenv
import os

# Load environment variables from .env file (for API key and org ID)
load_dotenv()

# Step 1: Define user input for the referral email
user_info = {
    "your_name": "Pooja",
    "target_name": "Ravi",
    "target_company": "Google",
    "target_role": "Software Engineer",
    "shared_context": "We both went to GITAM",
    "reason": "Google's AI research and culture",
}

# Step 2: Generate the email based on user input
generated_email = generate_referral_email(user_info)

# Check if generation was successful
if not generated_email:
    print(" Failed to generate referral email. Please check your input or generation logic.")
    exit(1)

# Output the generated email for review
print("\nGenerated Email:\n")
print(generated_email)

# Step 3: Prepare an Example object to represent this test case
# Note: Here, we assume the generated email is also the expected ideal output.
# In real evaluations, `ideal` should be a reference email crafted manually or from test data.
example = Example(
    input=user_info,
    ideal=generated_email,
    actual=generated_email
)

# Step 4: Initialize the Judgment client with credentials from .env
judgment = JudgmentClient(
    api_key=os.getenv("JUDGMENT_API_KEY"),
    org_id=os.getenv("JUDGMENT_ORG_ID")
)

# Step 5: Run evaluation using ReferralScorer
try:
    result = judgment.run_evaluation(
        examples=[example],
        scorers=[ReferralScorer()],
        model="gpt-4",
        project_name="referral-agent",
        eval_run_name="initial-test",
        override=True,
        append=False,
        async_execution=False
    )
    print("\n Evaluation completed.")
    print("If available, check trace or result details above.")
except Exception as e:
    print(" Evaluation failed:", str(e))
