from persons.address import Address
# encapsulated the attributes and behaviour related to the data type employee
# this is the base or super class
class Person:
    # constructor - attributes associated with person
    def __init__(self, firstname, lastname, age, email, telephone):
        self.first_name = firstname
        self.last_name = lastname
        self.__full_name = firstname + ' ' + lastname
        self.__age = age
        self.__email = email
        self.__telephone = telephone
        self.__address = Address()

    # getting and setting the attributes using the property decorator
    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, name):
        self.__full_name = name
        name_parts = name.split()
        self.first_name = name_parts[0]
        self.last_name = name_parts[1]

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def telephone(self):
        return self.__telephone

    @telephone.setter
    def telephone(self, telephone):
        self.__telephone = telephone
