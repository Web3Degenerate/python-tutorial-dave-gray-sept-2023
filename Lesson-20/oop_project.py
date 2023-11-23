from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Dave.deposit(38)
Sara.deposit(500)

Dave.withdraw(10000) #Trigger error. 
Dave.withdraw(38) #successful withdraw.

