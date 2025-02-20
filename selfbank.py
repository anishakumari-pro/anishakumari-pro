#import random

class BankAccount:
    def __init__(self, name, balance=0.0):
        self.__account_number = 21345712738  # Private attribute
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully!")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully!")
        else:
            print("Insufficient funds or invalid amount!")

    def get_balance(self):
        return self.__balance

    def get_account_info(self):
        return f"Account Holder: {self.name}\nAccount Number: {self.__account_number}\nBalance: ₹{self.__balance}"

class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0.0, interest_rate=3.5):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)
        self.deposit(interest)
        print(f"Interest of ₹{interest:.2f} applied!")

class CurrentAccount(BankAccount):
    def __init__(self, name, balance=0.0, overdraft_limit=5000):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance() + self.overdraft_limit:
            self._BankAccount__balance -= amount  # Access private attribute
            print(f"₹{amount} withdrawn successfully!")
        else:
            print("Overdraft limit exceeded or invalid amount!")

# Testing the Bank System
def main():
    print("Welcome to Self Bank!")
    name = input("Enter your name: ")
    acc_type = input("Enter account type (savings/current): ").strip().lower()

    if acc_type == "savings":
        account = SavingsAccount(name, balance=1000)  # Default ₹1000 deposit
    else:
        account = CurrentAccount(name, balance=1000)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Apply Interest (Savings Only)\n5. Account Info\n6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == "3":
            print(f"Current Balance: ₹{account.get_balance()}")

        elif choice == "4" and isinstance(account, SavingsAccount):
            account.apply_interest()

        elif choice == "5":
            print(account.get_account_info())

        elif choice == "6":
            print("Thank you for banking with us!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
