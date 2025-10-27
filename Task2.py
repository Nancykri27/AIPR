import math

def is_prime(n: int) -> bool:
    """Return True if n is a prime number, otherwise False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        s = input("Enter an integer (or 'q' to quit): ").strip()
        if s.lower() == 'q':
            print("Exiting.")
        else:
            num = int(s)
            print(f"{num} is {'a prime' if is_prime(num) else 'not a prime'} number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")