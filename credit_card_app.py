from accounts.credit_card import CreditCard
from accounts.credit_limit_exceeded_exception import CreditLimitExceededException
from accounts.below_min_payment_exception import BelowMinPaymentException

try:
    jodie_account = CreditCard(900, 'Jodie', 'Whitaker', 1000, 50)
    print(jodie_account)
    jodie_account.spend(10)
    print(jodie_account)
    jodie_account.deposit(500)
    print(jodie_account)
    jodie_account.deposit(60)
    jodie_account.deposit('help')
except CreditLimitExceededException as ex:
    print('WARNING')
    print(f"An exception has occurred!")
    print(f"You would have breached your maximum credit limit by £{ex.get_breach_amount()}")
except BelowMinPaymentException as bp:
    print('WARNING')
    print(f'You have paid £{bp.underpayment_amount} below your minimum payment.')
    print(f'Your minimum payment is £{jodie_account.minimum_payment}')
except TypeError as ty:
    print('This is the wrong data type')

finally:
    print("Your current credit card status")
    print(jodie_account)