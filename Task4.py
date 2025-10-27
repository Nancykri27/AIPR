def factorial_recursive(n: int) -> int:
    """Recursive factorial.
    - Base case: 0! = 1 and 1! = 1
    - Recursive step: n! = n * (n-1)!
    Raises ValueError for negative inputs.
    """
    if n < 0:
        raise ValueError("Negative input not allowed")
    if n <= 1:  # base case
        return 1
    return n * factorial_recursive(n - 1)  # recursive call

def factorial_iterative(n: int) -> int:
    """Iterative factorial using a simple loop.
    - Handles 0! = 1 naturally by starting result = 1.
    Raises ValueError for negative inputs.
    """
    if n < 0:
        raise ValueError("Negative input not allowed")
    result = 1
    # multiply result by each integer from 2 to n
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        s = input("Enter a non-negative integer (or 'q' to quit): ").strip()
        if s.lower() == 'q':
            print("Exiting.")
        else:
            n = int(s)
            if n < 0:
                raise ValueError
            print(f"Iterative factorial of {n} is: {factorial_iterative(n)}")
            print(f"Recursive factorial of {n} is: {factorial_recursive(n)}")
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")