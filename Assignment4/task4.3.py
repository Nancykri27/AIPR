def get_formatted_name(prompt="Enter full name: "):
    """
    Prompts the user for a full name and returns it formatted as "Last, First".
    If only one name is entered, it is returned unchanged.
    """
    full = input(prompt).strip()
    if not full:
        return ""
    parts = full.split()
    if len(parts) == 1:
        return parts[0]
    last = parts[-1]
    first = " ".join(parts[:-1])
    return f"{last}, {first}"

if __name__ == "__main__":
    result = get_formatted_name()
    if result:
        print(result)