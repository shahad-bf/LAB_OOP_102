# main.py

from bank_account import BankAccount


result = BankAccount("Salma", 500)

result.deposit(100)



print("Name of the account holder:", result.get_account_holder())


print("Balance now is:", result.get_balance())


result.withdraw(70)


print("a withdrawing the balance:", result.get_balance())
result.withdraw(990) 

end_balance = result.get_balance()
print("Balance at the end is", end_balance)
