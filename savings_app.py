import sys

from accounts.saving_account import SavingAccount
from accounts.minimum_balance_breached_exception import MinimumBalanceBreachedException

#
#  try = where like our program to run
try:
    lisa_saving_account = SavingAccount(300, 'Lisa', 'Simpson', 250)
    print(lisa_saving_account)
    lisa_saving_account.deposit(50)
    print(lisa_saving_account)

    lisa_saving_account.withdraw(125)
    print(lisa_saving_account)

    lisa_saving_account.withdraw(10)
#     toggle between 10 and 100
# catching the exceptions - only executed if an exception comes across and needs catching
# put the class in to a variable so can be called below
except MinimumBalanceBreachedException as ex:
    print("@" * 10)
    print(f"An exception has occurred!")
    print(f"You would have breached your minimum balance by {ex.get_breach_amount()}")
# extension to the try code, not used too much
else:
    print("no exception occurred")
# always runs whether theres been an exception or not
# tidy up
finally:
    print("The FINALLY block always runs")
    print(lisa_saving_account)


