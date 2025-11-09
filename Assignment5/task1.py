import hashlib

users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in users:
        print("Username already exists.")
    else:
        users[username] = hash_password(password)
        print("User registered successfully.")

def login(username, password):
    if username in users and users[username] == hash_password(password):
        print("Login successful!")
    else:
        print("Invalid username or password.")

def main():
    while True:
        choice = input("Do you want to (register/login/exit)? ").strip().lower()
        if choice == 'register':
            username = input("Enter username: ")
            password = input("Enter password: ")
            register(username, password)
        elif choice == 'login':
            username = input("Enter username: ")
            password = input("Enter password: ")
            login(username, password)
        elif choice == 'exit':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()