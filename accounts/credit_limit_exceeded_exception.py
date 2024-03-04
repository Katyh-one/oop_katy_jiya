# inherits from a built-in base class called exception
class CreditLimitExceededException(Exception):
    # passed the breach amount worked out in the credit card class
    def __init__(self, breach_amount):
        self.breach_amount = breach_amount

    def get_breach_amount(self):
        return self.breach_amount

    def set_breach_amount(self, breach_amount):
        self.breach_amount = breach_amount
