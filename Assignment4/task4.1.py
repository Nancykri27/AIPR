def is_leap(year: int) -> bool:
    """ Return True if year is a leap year, otherwise False.
    Leap year rule:
      - divisible by 4 and not divisible by 100, OR
      - divisible by 400 """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_year_from_user(prompt: str = "Enter a year: ") -> int:
    """Prompt the user until a valid integer year is entered and return it."""
    while True:
        s = input(prompt).strip()
        try:
            year = int(s)
            return year
        except ValueError:
            print("Invalid input. Please enter a valid integer year.")


def main():
    year = get_year_from_user()
    if is_leap(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


if __name__ == "__main__":
    main()