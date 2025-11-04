import sys

def cm_to_inches(cm):
    """Convert centimeters to inches. Returns value rounded to 3 decimal places."""
    try:
        value = float(cm)
    except (TypeError, ValueError):
        raise ValueError("Input must be a number")
    inches = value / 2.54
    return round(inches, 3)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        inp = sys.argv[1]
    else:
        inp = input("Enter centimeters: ").strip()

    try:
        print(cm_to_inches(inp))
    except ValueError as e:
        print("Error:", e)