from dataclasses import dataclass

#!/usr/bin/env python3
"""
Simple loan approval system.
Decision logic uses only financial attributes (income, credit_score).
It intentionally does NOT use name or gender so decisions remain unbiased.
"""


@dataclass
class Applicant:
    name: str
    gender: str  # recorded but NOT used in decision
    income: float
    credit_score: int

def decide_loan(applicant: Applicant):
    """
    Decide loan outcome based only on financial factors.
    Returns (decision_str, reason_str).
    """
    income = applicant.income
    score = applicant.credit_score

    # Simple, transparent rules (no use of name/gender).
    if score >= 700 and income >= 30000:
        return "APPROVED", "Strong credit score and sufficient income."
    if score >= 650 and income >= 25000:
        return "APPROVED (CONDITIONAL)", "Good score but borderline income — smaller loan or co-signer recommended."
    if score >= 600 and income >= 20000:
        return "REVIEW", "Fair credit and low income — manual review required."
    return "DENIED", "Credit score and/or income below minimums."

def print_decision(applicant: Applicant):
    decision, reason = decide_loan(applicant)
    print(f"{applicant.name:10s} | {applicant.gender:6s} | Income: ${applicant.income:8.2f} | "
          f"Score: {applicant.credit_score:3d} -> {decision} ({reason})")

def run_sample_tests():
    # Create paired examples to demonstrate lack of name/gender bias:
    samples = [
        Applicant(name="Raj",    gender="Male",   income=50000, credit_score=720),
        Applicant(name="Sara",   gender="Female", income=50000, credit_score=720),
        Applicant(name="Amit",   gender="Male",   income=25000, credit_score=630),
        Applicant(name="Fatima", gender="Female", income=25000, credit_score=630),
        # Additional varied examples
        Applicant(name="Same1",  gender="Male",   income=26000, credit_score=660),
        Applicant(name="Same2",  gender="Female", income=26000, credit_score=660),
        Applicant(name="Low",    gender="Male",   income=18000, credit_score=580),
    ]

    print("Sample loan decisions (demonstrating no bias by name/gender):")
    print("-" * 110)
    for a in samples:
        print_decision(a)
    print("-" * 110)
    print("Note: Decisions are based only on income and credit score, not on name or gender.\n")

def interactive_mode():
    print("Interactive loan check. Enter applicant details.")
    try:
        name = input("Name: ").strip()
        gender = input("Gender (recorded but not used): ").strip()
        income = float(input("Annual income (numbers only): ").strip())
        credit_score = int(input("Credit score (300-850): ").strip())
    except Exception as e:
        print("Invalid input:", e)
        return
    applicant = Applicant(name=name or "Unknown", gender=gender or "Unknown",
                          income=income, credit_score=credit_score)
    print_decision(applicant)

if __name__ == "__main__":
    run_sample_tests()
    # Offer to run interactive check
    ans = input("Run interactive check for a custom applicant? (y/N): ").strip().lower()
    if ans == "y":
        interactive_mode()