
def convert_date_format(date_str):
    """Converts date from YYYY-MM-DD to DD-MM-YYYY"""
    try:
        parts = date_str.split('-')
        if len(parts) != 3:
            return "Invalid"
        year, month, day = parts
        return f"{day}-{month}-{year}"
    except:
        return "Invalid"


def test_convert_date_format():
    """Test cases for date format conversion"""
    tests = [
        ("2023-10-15", "15-10-2023"),
        ("2024-01-01", "01-01-2024"),
        ("2000-12-31", "31-12-2000"),
        ("2023-02-28", "28-02-2023"),
        ("invalid", "Invalid"),
        ("2023-10", "Invalid"),
        ("", "Invalid")
    ]
    
    for date_str, expected in tests:
        result = convert_date_format(date_str)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{date_str}' -> '{result}'")


if __name__ == "__main__":
    test_convert_date_format()