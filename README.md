# ATM-Machine-Simulation
🔍 Project Overview: Interactive ATM Simulation
I developed an interactive ATM simulation in Python with several key features. Here’s a detailed look at both user and system interactions.

User Interactions:
1. Create Account:
Action: Users create a new account with a unique account number and PIN.
System Response: A new account is created and saved.
2. Login:
Action: Users login using their account number and PIN.

System Response: Credentials are validated and access is granted.
1. ATM Operations:
Check Balance:
Action: Users check their account balance.
System Response: Displays the current balance.
2. Withdraw Funds:
Action: Users withdraw money from their account.
System Response: Deducts the amount and updates transaction history.
3. Deposit Funds:
Action: Users deposit money into their account.
System Response: Adds the amount and updates transaction history.
4. Show Transaction History:
Action: Users view their transaction history.
System Response: Displays a list of past transactions with timestamps.
5. Exit:
Action: Users end their session.
System Response: Saves changes and exits the application.

System Interactions:
1. Data Persistence:
Action: Saves account details and transaction history to a JSON file.
System Response: Ensures data is available for future sessions.
2. Data Loading:
Action: Loads user data from the JSON file at startup.

System Response: Prepares data for user interactions.

Interaction Insight:

User Interaction Breakdown:
Total Interaction Points: 7
Create Account: 1
Login: 1

ATM Operations: 5 (Check Balance, Withdraw, Deposit, Show History, Exit)
Estimated User Engagement:
Users interact with approximately 4 out of these 7 points, resulting in an engagement rate of about 57.14%.

System Interaction Breakdown:
Total System Actions: 5
Data Persistence: 2 (on transactions and session end)
Data Loading: 1 (at startup)

Estimated System Engagement:
The system achieves 100% engagement in maintaining data integrity and managing user sessions.
This personal project has been a fantastic start to my journey in Python Development, allowing me to apply my Python skills and design a user-centric application.
