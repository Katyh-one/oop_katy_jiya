from accounts.account import Account
from accounts.minimum_balance_breached_exception import MinimumBalanceBreachedException
# import account class


class SavingAccount(Account):

    def __init__(self, amount, firstname, lastname, minimum_balance):
        super().__init__(amount, firstname, lastname)
        self._minimum_balance = minimum_balance

    # redefined the with draw method, overriding something you've inherited from the account class
    def withdraw(self, amount):
        if amount >= 0 and self._balance - amount >= self._minimum_balance:
            self._balance -= amount
        else:
            breach_amount = self._minimum_balance - (self._balance - amount)
            # throwing an exception
            # new class - have to use pascal case and must have exception in name
            # exceptions are expensive - change the flow of the program
            raise MinimumBalanceBreachedException(breach_amount)


