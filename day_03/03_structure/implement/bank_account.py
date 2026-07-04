class DepositUnderAmount(Exception):
     print("Under amount")

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance


    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Under amount")

        self.__balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Under amount")
        if amount > self.__balance:
            raise ValueError("Over withdraw")
        self.__balance -= amount

    def print_balance(self):
        print(self.__balance)


bank_account = BankAccount()
bank_account.deposit(100)
bank_account.withdraw(70)
bank_account.print_balance()
