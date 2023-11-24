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

# Test the InterestRewardsAcct class
Jim = InterestRewardsAcct(1000, "Jim")
Jim.getBalance()
Jim.deposit(100) #Should be 1,105 b/c of 5% bonus

Jim.transfer(100, Dave)

# Test the SavingsAcct class
Blaze = SavingsAcct(1000, 'Blaze')
Blaze.getBalance()
Blaze.deposit(100) #Has 1,105 b/c inherited 5% on deposit from parent InterestRewardsAcct class. 

Blaze.transfer(10000, Sara) #Trigger transfer error
Blaze.transfer(1000, Sara) #Successful transfer. Docked an extra $5 b/c overwrote withdraw method which is used by the transfer method.


