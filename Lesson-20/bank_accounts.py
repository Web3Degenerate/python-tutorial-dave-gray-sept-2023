class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName

        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self): 
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        # print(f"\nDeposit Complete.\nAccount '{self.name}' balance = ${self.balance:.2f}")
        # use f statement when inserting something
        print("\nDeposit Complete.")
        self.getBalance()

    #Before withdraw, create method to check if balance sufficient.
    #Create new class 'BalanceException' above with pass keyword.
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
    
    # (6:38:40) try - catch block in withdraw function: https://youtu.be/qwAFL1597eM?si=KY4S33efEdkJ9t87&t=23920
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance() #show the balance after withdraw complete.
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    # (6:41:40) Start transfer method: https://youtu.be/qwAFL1597eM?si=db9abBGQWtOpt8pp&t=24100
    def transfer(self, amount, account):
        try: 
            print('\n***********\n\nBeginning Transfer.. 🚀')
            self.viableTransaction(amount) #make sure viable transaction that can proceed
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete! ✅\n\n**********')
        except BalanceException as error:
            print(f'\nTransfer interrupted. ❌ {error}')

# (6:45:58) Create new Interest Rewards Account Class: https://youtu.be/qwAFL1597eM?si=_K0Y3omEcXlptVEo&t=24357
# Inherits from BankAccount
class InterestRewardsAcct(BankAccount):
    #Overwrite the deposit method. Deposit here gets added 5% as reward
    def deposit(self, amount):
        #return super().deposit(amount)
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()

# (6:50:27) Create new Class: https://youtu.be/qwAFL1597eM?si=ThcBQXcEl1wCS2fB&t=24627
# SavingsAcct inherits from InterestRewardsAcct which inherits from BankAccount
class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        #Add new property
        self.fee = 5 #fee on all withdraws

    #override withdraw method
    def withdraw(self, amount):
        try: 
            self.viableTransaction(amount + self.fee) #Check acct can cover amt + $5 fee
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f'\n❌Withdraw interrupted: {error}')

