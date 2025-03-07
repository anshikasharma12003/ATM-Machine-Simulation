ATM Simulation
This is a simple ATM simulation program written in Python. The program allows users to create an account, log in, check their balance, withdraw money, deposit money, and view their transaction history.

Features
Create a new account with a unique account number and PIN.

Login with an existing account number and PIN.

Check the current balance.

Withdraw money from the account.

Deposit money into the account.

View transaction history.

Getting Started
Prerequisites
Python 3.x

json module (comes pre-installed with Python)

os module (comes pre-installed with Python)

datetime module (comes pre-installed with Python)

Installation
Clone the repository or download the source code.

Navigate to the directory containing the source code.

Usage
Run the atm_simulation.py file.

Follow the on-screen instructions to create an account, log in, and perform transactions.

Code Structure
ATM Class: Represents an ATM account with methods for checking balance, withdrawing money, depositing money, and showing transaction history.

load_data(): Loads account data from a JSON file.

save_data(data): Saves account data to a JSON file.

create_account(): Creates a new account with a unique account number and PIN.

main(): Main function to run the ATM simulation program.

Example

if __name__ == "__main__":
    main()
