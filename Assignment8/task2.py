def assign_grade(score):
    """Assigns grade: 90-100=A, 80-89=B, 70-79=C, 60-69=D, <60=F"""
    if not isinstance(score, (int, float)) or score < 0 or score > 100:
        return "Invalid"
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def test_assign_grade():
    """Test cases with boundaries and invalid inputs"""
    tests = [
        (100, "A"), (90, "A"), (89, "B"), (80, "B"),
        (79, "C"), (70, "C"), (69, "D"), (60, "D"), (59, "F"),
        (-5, "Invalid"), (105, "Invalid"), ("eighty", "Invalid")
    ]
    
    for score, expected in tests:
        result = assign_grade(score)
        print(f"{score} -> {result}")


if __name__ == "__main__":
    test_assign_grade()