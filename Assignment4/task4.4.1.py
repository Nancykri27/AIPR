def count_vowels(string):
    # Define vowels
    vowels = 'aeiouAEIOU'
    
    # Initialize counter
    count = 0
    
    # Loop through each character in string
    for char in string:
        # If character is a vowel, increment counter
        if char in vowels:
            count += 1
            
    return count

# Get input from user
user_string = input("Enter a string: ")

# Print the result
print(f"Number of vowels: {count_vowels(user_string)}")