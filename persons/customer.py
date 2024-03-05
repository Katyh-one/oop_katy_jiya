from persons.person import Person
# Importing the base class Person from the package persons, file name person
# Sub Class or derived class called employee and inheritance from Person in brackets
# encapsulated the attributes and behaviour related to the data type employee


class Customer(Person):
    def __init__(self, firstname, lastname, age, email, telephone, contact_preferences):
        super().__init__(firstname, lastname, age, email, telephone)
        self._new_rewards_balance = 0
        self.contact_preferences = contact_preferences
        # adding the attribute for address but assigning to none as doesnt need to be passed when initialised.
        #  we can instantiate the address object and the address class
        self.address = None

    # method to work out the new customer reward points balance
    def new_rewards_balance(self, reward_points):
        self._new_rewards_balance += reward_points
    # method to return the value of the new rewards balance

    def get_reward_balance(self):
        return f'Thank you for your purchase.\nYour new rewards balance is {self._new_rewards_balance}'

    # decorate @property - getting the preferences and then changing the value
    @property
    def new_prefs(self):
        return self.contact_preferences

    @new_prefs.setter
    def new_prefs(self, contact_preferences):
        self.contact_preferences = contact_preferences


