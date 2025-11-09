class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance

def main():
    account = BankAccount()
    
    while True:
        action = input("Enter 'd' to deposit, 'w' to withdraw, 'b' to check balance, or 'q' to quit: ").lower()
        
        if action == 'd':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif action == 'w':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif action == 'b':
            print(f"Current balance: ${account.get_balance():.2f}")
        elif action == 'q':
            print("Exiting.")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()