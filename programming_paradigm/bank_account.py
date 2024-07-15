class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")

#
#
#
#     def __init__(self, account_balance, deposit_amount, withdraw ):
#         self.account_balance = 0
#         self.deposit_amount = deposit_amount
#         self.withdraw = withdraw
#
#
#     def withdraw(self):
#         self.account_balance -= self.withdraw
#
#
#
#
#
#
#
#
#     def deposit_amount(self):
#         self.account_balance += self.deposit_amount
#
#
#
#
#
#     def account_statement(self):
#         pass
#
#
# input_balance = int(input("Enter balance here"))
# input_deposit = int(input("Enter your deposit amount here"))
#
#
#
#
#
#
#
#
#
#
#
#
# class Guy:
#     def __init__(self, name, age, hieght, sex, smoke):
#         self.
#
#
#
#
#
#
# femo = Guy
#
# femo.
#
#
