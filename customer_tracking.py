from persons.customer import Customer
from persons.address import Address

new_customer = Customer('Jodie', 'Whitaker', 40, 'jodie@hotmail.com', '043295327952', 'email')
# instantiate the address class on the object new_customer_Address
new_customer_address = Address('Computer lane', 'Computer city', 'computerville', 'CP23 0BH')

new_customer.new_rewards_balance(50)
# object.method get reward balance - to then show to the customer their current points
print(new_customer.get_reward_balance())
# using the address from object new_customer_address
print(f"We'll send your rewards statement.\n{new_customer_address}")
new_customer.new_rewards_balance(75)
print(new_customer.get_reward_balance())
# updating to a list of customer contact preferences - using the getter/ setter methods
new_customer.new_prefs = ['email', 'telephone']
print(new_customer.contact_preferences)
print(type(new_customer.contact_preferences))
