# this is our capsule
# it's a collection of attributes and methods
from accounts.insufficient_funds_exception import InsufficientFundsException
class Account:
    numCreated = 0
    __bank_name = None
    account_limit = -1000
    # this is a special method called the CONSTRUCTOR
    # a constructor method is used to get your object ready to be used
    def __init__(self, initial_amount, firstname, lastname):
        # _balance is an attribute, it's a piece of data
        # a single underscore means this field is semi-private
        self._balance = initial_amount
        self.first_name = firstname
        # dunder on a field means PRIVATE - KEEP OUT
        # double underscore means fully private
        self.__last_name = lastname
        self._account_holder_name = firstname + " " + lastname

        # class field
        Account.numCreated += 1

    # method
    def deposit(self, amount):
        self._balance += amount

    # method
    def withdraw(self, amount):
        # validation
        if amount >= 0 and self._balance - amount >= -500:
            self._balance -= amount
        else:
            overdrawn_amount = (self._balance - amount) + 500
            raise InsufficientFundsException(overdrawn_amount)

    # this is what Java calls a getter
    # Java uses these to retrieve attribute values
    def get_balance(self):
        return self._balance

#     create a getter method to retrieve the first_name attribute
    def get_firstname(self):
        return self.first_name

    def set_firstname(self, firstname):
        self.first_name = firstname

    #     create a getter method to retrieve the last_name attribute
    def get_lastname(self):
        return self.__last_name.upper()

    # getters READ and setters WRITE
    # getters RETURN something, setters do not
    # setters have parameters
    def set_lastname(self, new_lastname):
        self.__last_name = new_lastname

    # getters can translate or modify the data before returning it
    # setters often validate the incoming data
    # setters often contain if statements

    # overriding a built-in method
    def __str__(self):
        return f"Account\nFirstname: {self.get_firstname()}\nLastname: {self.get_lastname()}" \
               f"\nBalance: ${self.get_balance()}\n********************"

    # operator overloading
    def __add__(self, other):
        return self._balance + other.get_balance()

    def __gt__(self, other):
        return self._balance > other.get_balance()

    def __lt__(self, other):
        return self._balance < other.get_balance()

    def __eq__(self, other):
        return self.get_balance() == other.get_balance()

#     PROPERTIES - .Net way of doing this

    # @property
    # def mday(self):
    #     return self._day
    #
    # @mday.setter
    # def mday(self, day):
    #     self._day = day
    """ Decorators are a very powerful and useful tool in Python since it allows programmers to
    # modify the behaviour of a function or class.
    # decorator @ / annotation
    # preferred syntax - easily identifiable - attribute it's the data
    # equivalent of a getter (java way)
    #  metaprogramming as at compile time a section of program alters another section of the program 
    When you see @property on a method inside a class:
    It means that method is a property, which can be accessed like an attribute.
    You can think of it like a smart attribute that does something when you access it.
    @property makes a method look like a simple attribute.
    account_holder_name is a smart attribute that runs a method to get its value.
    So when you do obj.account_holder_name, it's like asking, "Hey, what's the account holder's name?"
    """
    @property
    def account_holder_name(self):
            return self._account_holder_name
    """@account_holder_name.setter makes a method a special way to change the account_holder_name.
    When you do obj.account_holder_name = "New Name", it's like saying, "Change the account_holder_name to 'New Name'."
    This method then does some extra work to set the first name and last name based on the full name you provide."""
    # same name as the getter method
    # .setter at end
    @account_holder_name.setter
    def account_holder_name(self, name):
            self._account_holder_name = name
            name_parts = name.split()
            self.first_name = name_parts[0]
            self.__last_name = name_parts[1]

    #     CLASS Methods
    """
    Class methods are like special functions that belong to the class itself, not to any specific object made from the class.
    When you see @classmethod on a method inside a class:
    It means that method is a class method, which can be used on the class directly.
    You can think of it like a tool the class has, rather than something each object of the class gets.
    Here's what the two methods do:
    get_bank_name(cls):
    This method is like asking the class, "Hey, what's the bank's name?"
    The cls in get_bank_name(cls) is just a way to refer to the class itself.
    When you call Bank.get_bank_name(), it gets the __bank_name that's set for the class.
    set_bank_name(cls, name):
    This method is like telling the class, "Hey, change the bank's name to this new one!"
    Again, cls is just a way to talk about the class itself.
    When you call Bank.set_bank_name("New Bank"), it changes the __bank_name for the whole class to "New Bank".
    @classmethod makes methods like tools the class can use directly.
    get_bank_name() is a tool to ask the class for the bank's name.
    set_bank_name("NewName") is a tool to tell the class to change the bank's name to "NewName".
    So, these @classmethod methods help us work with information that's shared among all objects of the class, like the name of a bank in this example.
    """
    @classmethod
    def get_bank_name(cls):
        return cls.__bank_name

    @classmethod
    def set_bank_name(cls, name):
        cls.__bank_name = name



