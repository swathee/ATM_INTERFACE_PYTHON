import random
import sys

class ATM():
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        self.transaction_history.append(f"Deposit: Nu.{self.amount}")
        print("Current account balance: Nu.", self.balance)
        print()

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is Nu.{self.balance} only.")
            print("Try with a lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            self.transaction_history.append(f"Withdrawal: Nu.{self.amount}")
            print(f"Nu.{amount} withdrawal successful!")
            print("Current account balance: Nu.", self.balance)
            print()

    def transaction_history_log(self):
        print("\n----------TRANSACTION HISTORY----------")
        for transaction in self.transaction_history:
            print(transaction)
        print()

    def transfer(self, recipient, amount):
        if recipient:
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                recipient.balance += amount
                self.transaction_history.append(f"Transfer to {recipient.name} (Acc. No: {recipient.account_number}): Nu.{amount}")
                recipient.transaction_history.append(f"Transfer from {self.name} (Acc. No: {self.account_number}): Nu.{amount}")
                print(f"Transfer to {recipient.name} successful. New balance: Nu.{self.balance}")
            else:
                print("Invalid transfer or insufficient funds.")
        else:
            print("Recipient not found. Please check the account number.")

    def transaction(self):
        print("""
            TRANSACTION 
        *********************
            Menu:
            1. Deposit
            2. Withdraw
            3. Transfer
            4. Transaction History
            5. Exit
        *********************
        """)

        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4, or 5:"))
            except ValueError:
                print("Error: Enter a number between 1 and 5 only!\n")
                continue
            else:
                if option == 1:
                    amount = int(input("How much you want to deposit(Nu.):"))
                    self.deposit(amount)
                elif option == 2:
                    amount = int(input("How much you want to withdraw(Nu.):"))
                    self.withdraw(amount)
                elif option == 3:
                    recipient_account_number = input("Enter recipient's account number:")
                    amount = int(input("How much you want to transfer(Nu.):"))
                    recipient = find_account_by_account_number(recipient_account_number)
                    self.transfer(recipient, amount)
                elif option == 4:
                    self.transaction_history_log()
                elif option == 5:
                    print(f"""
                Printing receipt..............
          ******************************************
              Transaction is now complete.                         
              Transaction number: {random.randint(10000, 1000000)} 
              Account holder: {self.name.upper()}                  
              Account number: {self.account_number}                
              Available balance: Nu.{self.balance}                    
 
              Thanks for choosing us as your bank                  
          ******************************************
          """)
                    sys.exit()
                else:
                    print("Invalid option. Please enter a number between 1 and 5.")

# Function to find an account by account number
def find_account_by_account_number(account_number):
    for account in accounts:
        if account.account_number == account_number:
            return account
    return None

print("*******WELCOME TO BANK OF BHUTAN*******")
print("___________________________________________________________\n")
print("----------ACCOUNT CREATION----------")
name = input("Enter your name: ")
account_number = input("Enter your account number: ")
print("Congratulations! Account created successfully......\n")

# Creating accounts
accounts = [ATM("John ", "12345", 1000), ATM("Jane ", "54321", 1500), ATM(name, account_number)]

while True:
    trans = input("Do you want to do any transaction? (y/n): ")
    if trans.lower() == "y":
        account_number = input("Enter your account number: ")
        atm = find_account_by_account_number(account_number)
        if atm:
            atm.transaction()
        else:
            print("Account not found. Please check the account number.")
    elif trans.lower() == "n":
        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
        """)
        break
    else:
        print("Wrong command! Enter 'y' for yes and 'n' for NO.\n")
