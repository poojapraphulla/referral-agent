from judgeval.scorers import JudgevalScorer
from judgeval.data import ScoringResult, Example

class ReferralScorer(JudgevalScorer):
    """
    ReferralScorer evaluates generated referral emails by comparing them against ideal outputs.

    This basic implementation uses strict string matching (case-insensitive, trimmed) and assigns
    a perfect score only when the output matches exactly. Ideal for deterministic agents.
    """

    def __init__(self):
        super().__init__(
            score_type="custom",
            threshold=0.5,
        )
        self.required_params = []
        self.__name__ = "ReferralScorer"

    def __call__(self, example: Example) -> ScoringResult:
        """
        Evaluate the generated email by comparing it with the ideal output.

        This method performs an exact string match (case-insensitive and whitespace-stripped).
        It returns a perfect score if actual and ideal are identical, else zero.

        Args:
            example (Example): An object containing 'actual' and 'ideal' strings.

        Returns:
            ScoringResult: Custom result with name, score, and reasoning.
        """
        print("Running ReferralScorer...")

        # Normalize both strings for comparison (trim and lowercase)
        actual = example.actual.strip().lower()
        ideal = example.ideal.strip().lower()

        # Note: This scoring assumes deterministic output.
        score = 1.0 if actual == ideal else 0.0
        reasoning = "Perfect match." if score == 1.0 else "Mismatch between actual and ideal output."

        return ScoringResult(
            name="ReferralScorer",
            score=score,
            reasoning=reasoning
        )
