# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_sum = 0
# odd_sum = 0

# for num in numbers:
#     if num % 2 == 0:
#         even_sum = even_sum + num
#     else:
#         odd_sum = odd_sum + num

# print("Sum of even numbers:", even_sum)
# print("Sum of odd numbers:", odd_sum)
# Refactored code with improved logic

# Ask the user to enter numbers separated by spaces
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))


even_sum = sum(num for num in numbers if num % 2 == 0)
odd_sum = sum(num for num in numbers if num % 2 != 0)

# Display the results
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")
