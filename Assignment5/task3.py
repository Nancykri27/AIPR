def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.

    Parameters:
    n (int): The position in the Fibonacci sequence.

    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0  # The first Fibonacci number
    elif n == 2:
        return 1  # The second Fibonacci number
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive call

# Get user input
try:
    n = int(input("Enter the position of the Fibonacci number you want to calculate: "))
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")
except ValueError:
    print("Please enter a valid integer.")