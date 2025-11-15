def is_valid_email(email):
    """Validates email: must have @ and ., single @, no special chars at start/end"""
    if not email or not isinstance(email, str):
        return False
    
    if '@' not in email or '.' not in email:
        return False
    
    if email.count('@') != 1:
        return False
    
    special_chars = set('!@#$%^&*()+=[]{}|;:,<>?/~`"')
    if email[0] in special_chars or email[-1] in special_chars:
        return False
    
    if email[0] in '@.' or email[-1] in '@.':
        return False
    
    return True


# Test Cases
def test_is_valid_email():
    valid = ["user@example.com", "test@domain.co"]
    invalid = ["userexample.com", "user@examplecom", "user@@example.com", 
               "@example.com", "user@example.com.", ""]
    
    print("Valid emails:")
    for email in valid:
        print(f"  {email}: {is_valid_email(email)}")
    
    print("\nInvalid emails:")
    for email in invalid:
        print(f"  {email}: {is_valid_email(email)}")


if __name__ == "__main__":
    test_is_valid_email()