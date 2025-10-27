def reverse_string(s: str) -> str:
    """Return the reversed version of the input string."""
    return s[::-1]

if __name__ == "__main__":
    try:
        user_input = input("Enter a string: ")
    except (EOFError, KeyboardInterrupt):
        print("\nNo input provided.")
    else:
        print(reverse_string(user_input))