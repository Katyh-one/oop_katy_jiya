class BelowMinPaymentException(Exception):
    # passed the breach amount worked out in the credit card class
    def __init__(self, underpayment_amount):
        self.underpayment_amount = underpayment_amount

    def get_underpayment_amount(self):
        return self.underpayment_amount

    def set_underpayment_amount(self, underpayment_amount):
        self.underpayment_amount = underpayment_amount