from account.transaction import Transaction
from account.user import User
from decimal import Decimal

class BankAccount:
    def __init__(self, balance):
        self.balance = Decimal(balance)
        self.transactions = []

    def deposit(self, amount):
        amount = Decimal(amount)
        self.balance += amount
        self.transactions.append(f"Deposited: Rs. {amount}")

    def withdraw(self, amount):
        amount = Decimal(amount)
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: Rs. {amount}")
        else:
            raise ValueError("Insufficient balance!")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions
        
    def get_account_type(self):
        return self.account_type

    def get_user(self):
        return self.user


class SavingsAccount(BankAccount):
    MIN_BALANCE = 100

    def withdraw(self, amount):
        if self.balance - amount < self.MIN_BALANCE:
            print("")
            return 
        super().withdraw(amount)

    def get_account_type(self):
        return "Savings account"

class CurrentAccount(BankAccount):

    def get_account_type(self):
        return "Current account"

class StudentAccount(BankAccount):

    def withdraw(self, amount):
        if (self.balance - amount) < 100:
            print("A minimum balance of Rs.100 needed to withdraw from a Students account!")
        super().withdraw(amount)

    def get_account_type(self):
        return "Students account"

