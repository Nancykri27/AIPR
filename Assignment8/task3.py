def is_sentence_palindrome(sentence):
    """Checks if sentence is palindrome ignoring case, spaces, and punctuation"""
    if not sentence:
        return False
    
    cleaned = ''.join(ch.lower() for ch in sentence if ch.isalnum())
    return cleaned == cleaned[::-1]


def test_is_sentence_palindrome():
    """Test cases for sentence palindrome"""
    tests = [
        ("A man a plan a canal Panama", True),
        ("race a car", False),
        ("Madam, I'm Adam", True),
        ("Was it a car or a cat I saw?", True),
        ("hello world", False),
        ("", False)
    ]
    
    for sentence, expected in tests:
        result = is_sentence_palindrome(sentence)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{sentence}' -> {result}")


if __name__ == "__main__":
    test_is_sentence_palindrome()