
def factorial(n: int) -> int:
    """Return n! for non-negative integers. Raise ValueError for negatives."""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    try:
        s = input("Enter an integer: ").strip()
        n = int(s)
    except ValueError:
        print("Invalid input: please enter a whole integer.")
        return

    try:
        print(f"{n}! = {factorial(n)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()