import os

file_path = 'accounts.txt'

def initialize_accounts_file():
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write('')

def load_accounts():
    initialize_accounts_file()
    accounts = {}
    with open(file_path, 'r') as f:
        for line in f:
            account_number, balance = line.strip().split(',')
            accounts[account_number] = float(balance)
    return accounts

def save_accounts(accounts):
    with open(file_path, 'w') as f:
        for account_number, balance in accounts.items():
            f.write(f'{account_number},{balance}\n')

class bank_account:
    def __init__(self, account_number):
        self.account_number = account_number
        self.accounts = load_accounts()
        self.amount = self.accounts.get(account_number, 0)
        self.transactions = []

    def deposit(self, Amount):
        self.amount += Amount
        self.transactions.append(f"Deposited: {Amount}")
        self.update_file()
        print("Amount Successfully Deposited")

    def withdraw(self, Amount):
        if self.amount - Amount >= 500:
            self.amount -= Amount
            self.transactions.append(f"Withdrawn: {Amount}")
            self.update_file()
            print("Amount Successfully Withdrawn")
        else:
            print("Insufficient Balance. You have to keep at least Rs. 500 in your Account")

    def display(self):
        print("Your bank balance is:", self.amount)

    def update_amount(self, Amount):
        self.amount += Amount
        self.transactions.append(f"Updated balance by adding: {Amount}")
        self.update_file()
        print("Amount Successfully Updated")

    def show_statement(self):
        print("Transaction statement:")
        for transaction in self.transactions:
            print(transaction)
        print("Final balance:", self.amount)

    def update_file(self):
        self.accounts[self.account_number] = self.amount
        save_accounts(self.accounts)

# Example usage:
initialize_accounts_file()
account_number = input("Enter your account number: ")
a = bank_account(account_number)

for i in range(0, 50):
    print("1. Deposit 2. Withdraw 3. Update Amount 4. Show Statement 5. Exit")
    p = int(input("Enter Your Choice: "))
    if p == 1:
        Amount = float(input("Enter Amount to be Deposited: "))
        a.deposit(Amount)
    elif p == 2:
        Amount = float(input("Enter Amount to be Withdrawn: "))
        a.withdraw(Amount)
    elif p == 3:
        Amount = float(input("Enter Amount to be Added: "))
        a.update_amount(Amount)
    elif p == 4:
        a.show_statement()
    elif p == 5:
        break
    else:
        print("You have entered a wrong value")


# import os

# file_path = 'accounts.txt'

# def initialize_accounts_file():
#     if not os.path.exists(file_path):
#         with open(file_path, 'w') as f:
#             f.write('')

# def load_accounts():
#     initialize_accounts_file()
#     accounts = {}
#     with open(file_path, 'r') as f:
#         for line in f:
#             account_number, balance = line.strip().split(',')
#             accounts[account_number] = float(balance)
#     return accounts




# # Function to save accounts data to file
# def save_accounts(accounts):
#     with open(file_path, 'w') as f:
#         for account_number, balance in accounts.items():
#             f.write(f"{account_number},{balance}\n")

# # Function to get balance
# def get_balance(account_number: str) -> float:
#     accounts = load_accounts()
#     return accounts.get(account_number, 0.0)  # Return balance or 0.0 if account not found

# # Function to deposit funds
# def deposit(account_number: str, amount: float):
#     accounts = load_accounts()
#     if account_number in accounts:
#         accounts[account_number] += amount
#     else:
#         accounts[account_number] = amount
#     save_accounts(accounts)

# # Function to withdraw funds
# def withdraw(account_number: str, amount: float):
#     accounts = load_accounts()
#     if account_number in accounts and accounts[account_number] >= amount:
#         accounts[account_number] -= amount
#         save_accounts(accounts)
#         return True  # Withdrawal successful
#     else:
#         return False  # Insufficient funds or account not found

# # Function to update account balance
# def update_account(account_number: str, balance: float):
#     accounts = load_accounts()
#     if account_number in accounts:
#         accounts[account_number] = balance
#         save_accounts(accounts)
#     else:
#         print(f"Account {account_number} not found.")

# # Main program for testing
# if __name__ == "__main__":
#     # Example usage:

#     # Example account number
#     account_number = '1234567890'

#     # Checking balance
#     balance = get_balance(account_number)
#     print(f"Current balance for account {account_number}: {balance}")

#     # Depositing funds
#     deposit(account_number, 500)
#     print(f"Deposit of 500 made. New balance: {get_balance(account_number)}")

#     # Withdrawing funds
#     if withdraw(account_number, 300):
#         print(f"Withdrawal of 300 successful. New balance: {get_balance(account_number)}")
#     else:
#         print("Withdrawal failed. Insufficient funds or account not found.")

#     # Updating account balance directly to 1500
#     update_account(account_number, 1500)
#     print(f"After updating balance to 1500, new balance: {get_balance(account_number)}")

#     # Performing another operation (e.g., deposit)
#     deposit(account_number, 200)
#     print(f"After additional deposit, new balance: {get_balance(account_number)}")


# class bank_account:
#     def __init__(self):
#         self.amount = 0
#         self.transactions = []
#         self.file_path = 'accounts.txt'
#
#     def deposit(self, Amount):
#         self.amount += Amount
#         self.transactions.append(f"Deposited: {Amount}")
#         print("Amount Successfully Deposited")
#
#     def withdraw(self, Amount):
#         if self.amount - Amount >= 500:
#             self.amount -= Amount
#             self.transactions.append(f"Withdrawn: {Amount}")
#             print("Amount Successfully Withdrawn")
#         else:
#             print("Insufficient Balance. You have to keep at least Rs. 500 in your Account")
#
#     # def display(self):
#     #     print("Your bank balance is:", self.amount)
#
#     def update_amount(self, Amount):
#         self.amount += Amount
#         self.transactions.append(f"Updated balance by adding: {Amount}")
#         print("Amount Successfully Updated")
#
#     def show_statement(self):
#         print("Transaction statement:")
#         for transaction in self.transactions:
#             print(transaction)
#         print("Final balance:", self.amount)
#
#     def update_file(self):
#         with open(self.file_path, 'w') as file:
#             for transaction in self.transactions:
#                 file.write(transaction + '\n')
#             file.write(f"Final balance: {self.amount}\n")
#
# a = bank_account()
# for i in range(0, 50):
#     print("1. Deposit 2. Withdraw 3. Update Amount 4. Show Statement 5. Exit")
#     p = int(input("Enter Your Choice: "))
#     if p == 1:
#         Amount = float(input("Enter Amount to be Deposited: "))
#         a.deposit(Amount)
#     elif p == 2:
#         Amount = float(input("Enter Amount to be Withdrawn: "))
#         a.withdraw(Amount)
#     elif p == 3:
#         Amount = float(input("Enter Amount to be Added: "))
#         a.update_amount(Amount)
#     elif p == 4:
#         a.show_statement()
#     elif p == 5:
#         break
#     else:
#         print("You have entered a wrong value")

