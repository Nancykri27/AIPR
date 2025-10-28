# ...existing code...
def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome (ignoring non-alphanumeric and case)."""
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

def prompt_palindrome() -> None:
    """Prompt the user for input and print whether it's a palindrome."""
    text = input("Enter text to check for palindrome (leave empty to cancel): ").strip()
    if not text:
        print("Cancelled.")
        return
    if is_palindrome(text):
        print("Yes — it's a palindrome.")
    else:
        print("No — not a palindrome.")
prompt_palindrome()
# ...existing code...