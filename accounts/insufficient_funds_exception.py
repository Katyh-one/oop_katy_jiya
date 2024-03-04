class InsufficientFundsException(Exception):
    def __init__(self, overdrawn_amount):
        self.overdrawn_amount = overdrawn_amount

    # getting the overdrawn_amount value
    def get_overdrawn_amount(self):
        return self.overdrawn_amount

    # setting what the overdrawn amount value is
    def set_overdrawn_amount(self, overdrawn_amount):
        self.overdrawn_amount = overdrawn_amount
