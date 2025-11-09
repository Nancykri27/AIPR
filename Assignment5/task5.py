def greet_user():
    # Take user input
    name = input("Enter your name: ")
    gender = input("Enter your gender (male/female/other): ").lower()

    # Assign appropriate title
    if gender == "male":
        title = "Mr."
    elif gender == "female":
        title = "Ms."
    else:
        title = "Mx."   # gender-neutral title

    # Display greeting
    print(f"Hello, {title} {name}! Welcome.")


# Run the function
greet_user()
