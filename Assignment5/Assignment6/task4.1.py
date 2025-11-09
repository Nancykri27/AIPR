def sum_to_n_for(n):
    if n < 0:
        return "Please enter a positive number"
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Example usage
n = int(input("Enter a positive number: "))
print(f"Sum of first {n} numbers is: {sum_to_n_for(n)}")
