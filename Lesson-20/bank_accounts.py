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
