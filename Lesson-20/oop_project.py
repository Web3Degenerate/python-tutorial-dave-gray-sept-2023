from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Dave.deposit(10)
Sara.deposit(500)

Dave.withdraw(10000) #Trigger error. 
Dave.withdraw(20) #successful withdraw.

Dave.transfer(10000, Sara) #Trigger transfer error
Dave.transfer(100, Sara) #Successful transfer.