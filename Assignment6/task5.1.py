class BankAccount:
    def __init__(self):                 # Constructor → initializes balance
        self.balance = 0.0

    def deposit(self, amount):          # Deposit method
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):         # Withdraw method
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):              # Returns current balance
        return self.balance


def main():
    account = BankAccount()             # Create account object

    while True:                         # Controlled loop for user options
        action = input("Enter 'd', 'w', 'b', or 'q': ").lower()

        if action == 'd':               # Deposit
            amount = float(input("Amount to deposit: "))
            account.deposit(amount)
        elif action == 'w':             # Withdraw
            amount = float(input("Amount to withdraw: "))
            account.withdraw(amount)
        elif action == 'b':             # Check balance
            print(f"Balance: ${account.get_balance():.2f}")
        elif action == 'q':             # Quit
            print("Exiting.")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
