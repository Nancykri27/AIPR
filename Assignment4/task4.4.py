def count_vowels(text: str) -> int:
    """
    Return the number of vowels (a, e, i, o, u) in the given string.
    Counts both uppercase and lowercase vowels.
    """
    if text is None:
        return 0
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in text if ch in vowels)


# Example usage / quick tests
if __name__ == "__main__":
    samples = [
        "Hello, World!",
        "AEIOU aeiou",
        "",
        "Python Programming",
        None
    ]
    for s in samples:
        print(repr(s), "->", count_vowels(s))