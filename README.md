# Referral Agent with Judgeval SDK

This project demonstrates a simple AI agent workflow that generates a referral request email and evaluates it using [Judgment Labs](https://judgment-labs.com)'s `judgeval` SDK. It is built as part of a technical assessment to showcase agent instrumentation, tracing, and evaluation.


## Motivation

The goal of this project is to explore how agent workflows can be developed and evaluated using Judgment Labs’ SDK. The core idea is to simulate a real-world scenario: generating a professional referral request email and evaluating it based on quality and clarity. This project helped me understand how to integrate tracing and scoring systems into agents, and how such tooling can assist in building higher-quality AI-powered systems.


##  Features

-  Dynamically generates a professional referral email using user inputs
-  Traces execution using `judgeval.tracer`
-  Custom scoring logic using a `ReferralScorer` class
-  Evaluates email quality against an ideal example using `judgeval`’s `run_evaluation`
-  Easy to configure and run with `.env` setup

##  How It Works

1. **Input**: You define `user_info` containing:
   - Your name
   - Recipient’s name
   - Target role and company
   - A reason for applying

2. **Agent**: The agent formats the input into a well-written email via `generate_referral_email()`.

3. **Scoring**: A custom `ReferralScorer` compares the generated email with an ideal example.

4. **Evaluation**: The system uses `judgeval` to trace and evaluate the generated email.

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/referral-agent.git
cd referral-agent
```

### 2. Install Dependencies

```python
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

### 3. Create a `.env` file

```env
JUDGEVAL_API_KEY=your_actual_api_key
JUDGEVAL_ORG_ID=your_org_id
```

`judgeval` automatically picks up these variables—no need to pass them manually.

## Run the Agent

```python
python run_referral.py
```
This will:
- Generate a referral email
- Print it to the console
- Run a custom evaluation using the ReferralScorer
- Provide a link to view evaluation results in your Judgment Labs dashboard

## Bug Handling & Debugging

While integrating Judgeval SDK and executing the evaluation pipeline, I encountered several non-trivial bugs. Here's a brief overview of how they were resolved:

- **`NoneType` object is not iterable**  
  Occurred when a custom scorer didn't define `required_params`. This was fixed by explicitly setting `required_params = []` in the `ReferralScorer` class.

- **`model_copy()` on NoneType**  
  This happened when a custom scorer returned `None`. I resolved this by ensuring the `__call__` method of the scorer always returns a valid `ScoringResult` object.

- **AttributeError: object has no attribute `__name__`**  
  Fixed by wrapping the scorer in a `FunctionScorer` wrapper or ensuring proper object metadata is available.

Each bug taught me more about the internal expectations of Judgeval's scoring system and the need for properly shaped return types and metadata.

## Example Output

```
Subject: Request for Referral to Google

        Hi Ravi,

        I hope you're doing well! I recently came across an exciting opportunity for a Software Engineer role at Google and immediately thought of reaching out to you.

        Given your experience and connection with the company, I’d be incredibly grateful if you’d consider referring me for the role. Google's AI research and culture is one of the main reasons I am interested in this role.

        If you’re open to it, I’d be happy to send over my resume and any other details you may need. Thanks in advance for considering this - I really appreciate your time and support.

        Warm regards,
        Pooja
```

## Future Improvements

To further improve the referral agent and explore advanced applications, the following enhancements are planned:

- **OpenAI API Integration**  
  Instead of hardcoding the email content, the agent can dynamically generate referral emails using an LLM (e.g., GPT-4) via the OpenAI API. This will allow the email tone, structure, and content to adapt based on inputs like role, company, or person.

- **UI/CLI Interface**  
  A command-line or basic web UI can make this agent more interactive. Users can input parameters (e.g., job title, company name, referrer name), and the system can generate and evaluate referral drafts accordingly.

- **Advanced Scoring Heuristics**  
  Incorporate custom metrics into the scorer:
  - **Tone**: Check for professional yet friendly tone using sentiment or tone classifiers.
  - **Personalization**: Score how tailored the email is based on presence of specific details like company mission or shared history.
  - **Structure**: Assess clarity and flow using regex and pattern checks.

These ideas aim to evolve the agent from a template-based generator into an intelligent, adaptable assistant.

## File Structure

```bash
.
├── referral_agent.py       # Email-generation logic (agent)
├── referral_scorer.py      # Custom scorer implementation
├── run_referral.py         # Main entrypoint with evaluation
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables for Judgeval
└── README.md               # Documentation (this file)
```


