class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return self.account_balance
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount):
        if amount <= 0:
            return False
        if amount > self.account_balance:
            return False
        self.account_balance -= amount
        return True

    def display_balance(self):
        return print(f"Current Balance: ${self.account_balance}")
