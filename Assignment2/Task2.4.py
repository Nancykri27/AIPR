"""Utility to compute the sum of squares from user input.

Run directly:
    python sum_of_squares.py
"""

from typing import List, Optional


def sum_of_squares_from_input(prompt: str = "Enter integers separated by spaces: ") -> Optional[int]:
    """Prompt the user for space-separated integers and return the sum of their squares.

    Returns None if parsing fails.
    """
    user_text: str = input(prompt).strip()
    if not user_text:
        print("No input provided.")
        return None

    parts: List[str] = user_text.split()
    try:
        numbers: List[int] = [int(p) for p in parts]
    except ValueError:
        print("Invalid input. Please enter only integers separated by spaces.")
        return None

    result: int = sum(n * n for n in numbers)
    return result


if __name__ == "__main__":
    computed: Optional[int] = sum_of_squares_from_input()
    if computed is not None:
        print(f"Sum of squares: {computed}")
