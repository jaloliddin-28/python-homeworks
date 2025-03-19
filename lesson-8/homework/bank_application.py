import random
import os

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account Number: {self.account_number} | Name: {self.name} | Balance: {self.balance}"

class Bank:
    accounts = {}

    @staticmethod
    def create_account():
        account_number = random.randint(10**9, 10**10 - 1)
        name = input("Enter your Name: ")
        initial_deposit = int(input("Enter your initial deposit: "))
        if initial_deposit <= 0:
            raise ValueError("Initial deposit should be greater than 0.")
        
        account = Account(account_number, name, balance=initial_deposit)
        Bank.accounts[account_number] = account
        print("Successfully Created!")
        print(account)

    @staticmethod
    def view_account():
        account_number = int(input("Enter your 10-digit account number: "))
        account = Bank.accounts.get(account_number)
        if account:
            print("Account Found.")
            print(account)
        else:
            print("Account Number Not Found.")

    @staticmethod
    def deposit():
        account_number = int(input("Enter your 10-digit account number: "))
        account = Bank.accounts.get(account_number)
        if account:
            deposit = int(input("Account Found. How much do you want to deposit: "))
            if deposit <= 0:
                raise ValueError("Invalid number for a deposit.")
            account.balance += deposit
            print(f"Successfully deposited!\n{account}")
        else:
            print("Account Number Not Found.")

    @staticmethod
    def withdraw():
        account_number = int(input("Enter your 10-digit account number: "))
        account = Bank.accounts.get(account_number)
        if account:
            withdrawal = int(input("Account Found. How much do you want to withdraw: "))
            if withdrawal <= 0:
                raise ValueError("Invalid number for a withdrawal.")
            if withdrawal > account.balance:
                print("Insufficient funds.")
            else:
                account.balance -= withdrawal
                print(f"Successfully withdrawn!\n{account}")
        else:
            print("Account Number Not Found.")

    @staticmethod
    def save_to_file():
        with open(r"C:\Users\user\Desktop\MAAB\python-homeworks\lesson-8\homework\accounts.txt", "w") as file:
            for account in Bank.accounts.values():
                file.write(f"{account.account_number},{account.name},{account.balance}\n")

    @staticmethod
    def load_from_file():
        if os.path.exists(r"C:\Users\user\Desktop\MAAB\python-homeworks\lesson-8\homework\accounts.txt"):
            with open(r"C:\Users\user\Desktop\MAAB\python-homeworks\lesson-8\homework\accounts.txt", "r") as file:
                for line in file:
                    account_number, name, balance = line.strip().split(",")
                    Bank.accounts[int(account_number)] = Account(int(account_number), name, int(balance))

    @staticmethod
    def run():
        Bank.load_from_file()  # Load accounts on start
        while True:
            try:
                s = int(input("\nChoose an operation:\n1. Create Account\n2. View an Account\n3. Deposit\n4. Withdraw\n5. Exit\n"))
                if s == 1:
                    Bank.create_account()
                elif s == 2:
                    Bank.view_account()
                elif s == 3:
                    Bank.deposit()
                elif s == 4:
                    Bank.withdraw()
                elif s == 5:
                    Bank.save_to_file()  # Save accounts on exit
                    print("Thank you for using our services.")
                    break
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

# Run the bank application
Bank.run()