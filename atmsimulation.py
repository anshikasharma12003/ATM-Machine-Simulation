# atm_simulation.py

import json
import os
import datetime

class ATM:
    def __init__(self, account_number, pin, balance=0, transaction_history=None):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = transaction_history if transaction_history else []

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.transaction_history.append({
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "type": "withdrawal",
                "amount": amount
            })
            print(f"Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}")
            self.save_data()

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append({
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": "deposit",
            "amount": amount
        })
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        self.save_data()

    def show_transaction_history(self):
        if not self.transaction_history:
            print("There are no transactions in your account.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(f"{transaction['date']}: {transaction['type']} of ${transaction['amount']:.2f}")
            print(f"Total Balance: ${self.balance:.2f}")

    def save_data(self):
        data = load_data()
        data[self.account_number] = {
            "pin": self.pin,
            "balance": self.balance,
            "transaction_history": self.transaction_history
        }
        save_data(data)

def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            return json.load(f)
    else:
        return {}

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f)

def create_account():
    data = load_data()
    while True:
        new_account_number = input("Enter your new account number (11 digits): ")
        if len(new_account_number) != 11 or not new_account_number.isdigit():
            print("Account number must be 11 digits long and only contain digits!")
            continue
        if new_account_number in data:
            print("Account number already exists. Please try again.")
            continue
        break

    while True:
        new_pin = input("Enter your new PIN (5 digits): ")
        if len(new_pin) != 5 or not new_pin.isdigit():
            print("PIN must be 5 digits long and only contain digits!")
            continue
        break

    data[new_account_number] = {
        "pin": new_pin,
        "balance": 0,
        "transaction_history": []
    }
    save_data(data)
    data = load_data()  # Reload the data dictionary
    print("Account created successfully!")

def main():
    data = load_data()

    while True:
        print("\nLogin or Create Account:")
        print("1. Login")
        print("2. Create Account")
        choice = input("Enter your choice: ")

        if choice == "1":
            new_account_number = input("Enter your account number: ")
            new_pin = input("Enter your PIN: ")

            if len(new_account_number) != 11 or not new_account_number.isdigit():
                print("Account number must be 11 digits long and only contain digits!")
                continue

            if len(new_pin) != 5 or not new_pin.isdigit():
                print("PIN must be 5 digits long and only contain digits!")
                continue

            if new_account_number in data and data[new_account_number]["pin"] == new_pin:
                atm = ATM(new_account_number, new_pin, data[new_account_number]["balance"], data[new_account_number]["transaction_history"])
                break
            else:
                if new_account_number in data:
                    print("Invalid PIN!")
                else:
                    print("Account not found. Please create an account first.")
        elif choice == "2":
            create_account()
            data = load_data()  # Reload the data dictionary
        else:
            print("Invalid choice. Please try again.")

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Show Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: $"))
            atm.withdraw(amount)
        elif choice == "3":
            amount = float(input("Enter amount to deposit: $"))
            atm.deposit(amount)
        elif choice == "4":
            atm.show_transaction_history()
        elif choice == "5":
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()