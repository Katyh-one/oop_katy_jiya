from accounts.account import Account
from accounts.credit_limit_exceeded_exception import CreditLimitExceededException
from accounts.below_min_payment_exception import BelowMinPaymentException
# derived or sub class


class CreditCard(Account):

    def __init__(self, amount, firstname, lastname, maximum_credit_limit, minimum_payment):
        super().__init__(amount, firstname, lastname)
        self.maximum_credit_limit = maximum_credit_limit
        self.minimum_payment = minimum_payment
    # If person tries to spend above their credit limit it will workout the amount they are overspending
    # it will then raise the exception that is in a separate file and named as the below classname
    """Created a method which will look at if the amount spent on the card is above takes 
    the customer above their credit limit.
    Amount passed in = the balance on their account
    if statement - balance plus what they are spending is less than or equal to their credit limit then 
    it will add the amount to their balance otherwise it will raise the exception
    The breach amount is working out the difference between 
    the total of the balance and amount spent minus from the credit card limit"""
    def spend(self, amount):
        if self._balance + amount <= self.maximum_credit_limit:
            self._balance += amount
        else:
            breach_amount = (self._balance + amount) - self.maximum_credit_limit
            # raising the error which then goes off to the exceptions file
            raise CreditLimitExceededException(breach_amount)
    """created a method for paying the bill but if the amount paid is less than the minimum payment 
    the exception is raised
    Amount is the amount paid - if the amount paid is greater than or equal to the minimum payment 
    it will reduce the balance
    For the exception work out the difference between the minimum amount and amount paid"""
    # is this an example of polymorphism because this is the deposit method from account but does something different
    def deposit(self, amount):
        if amount >= self.minimum_payment:
            self._balance -= amount
        else:
            underpayment_amount = self.minimum_payment - amount
            raise BelowMinPaymentException(underpayment_amount)




