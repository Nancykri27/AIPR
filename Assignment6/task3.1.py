def classify_age_match(age):
    match age:
        case a if a < 0:
            return "Invalid age"
        case a if a <= 12:
            return "Child"
        case a if a <= 19:
            return "Teenager"
        case a if a <= 64:
            return "Adult"
        case _:
            return "Senior"

# Example usage
age = int(input("Enter your age: "))
print(classify_age_match(age))
