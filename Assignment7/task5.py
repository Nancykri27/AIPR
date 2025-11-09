numbers = [1, 2, 3]

try:
    print(numbers[5])
except IndexError:
    print("Error: Tried to access an invalid index.")
