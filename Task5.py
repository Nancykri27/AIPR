# Simple CLI that reads a list of numbers from the user and prints the largest value.
from typing import List

def max_in_list_iterative(nums: List[float]) -> float:
    """Return the largest number using an O(n) iterative scan. Raises ValueError for empty list."""
    if not nums:
        raise ValueError("empty list")
    max_val = nums[0]
    for x in nums[1:]:
        if x > max_val:
            max_val = x
    return max_val

def max_in_list_builtin(nums: List[float]) -> float:
    """Return the largest number using Python's built-in max (O(n))."""
    if not nums:
        raise ValueError("empty list")
    return max(nums)

def parse_numbers(s: str) -> List[float]:
    """Parse comma/space-separated numbers into a list of floats. Raises ValueError on invalid tokens."""
    if not s:
        return []
    tokens = s.replace(",", " ").split()
    return [float(t) for t in tokens]

if __name__ == "__main__":
    try:
        s = input("Enter numbers separated by spaces or commas (or 'q' to quit): ").strip()
        if s.lower() == "q":
            print("Exiting.")
        else:
            nums = parse_numbers(s)
            if not nums:
                print("No numbers provided.")
            else:
                print("Largest (iterative):", max_in_list_iterative(nums))
                print("Largest (builtin)   :", max_in_list_builtin(nums))
    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces or commas.")