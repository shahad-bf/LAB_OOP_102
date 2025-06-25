

class BankAccount:
    def __init__(self, account_holder, balance=0):
        # save name and balance
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        # put money 
        if amount > 0:
            self.balance = self.balance + amount
        else:
            print("You must enter a positive number.")
        return self.balance

    def withdraw(self, amount):
        # take money
        if amount > self.balance:
            print("Not enough money in your account.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
        return self.balance
    


    def get_balance(self):
        return self.balance

    def get_account_holder(self):
        return self.account_holder
