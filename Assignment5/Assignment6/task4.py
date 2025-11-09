def sum_to_n(n):
    """
    Calculate the sum of first n natural numbers
    Args:
        n: A positive integer
    Returns:
        The sum of numbers from 1 to n
    """
    if n < 0:
        return "Please enter a positive number"
    return sum(range(1, n + 1))

# Example usage
if __name__ == "__main__":
    n = int(input("Enter a positive number: "))
    result = sum_to_n(n)
    print(f"Sum of first {n} numbers is: {result}")