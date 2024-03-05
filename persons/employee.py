from persons import address
from persons.person import Person
# Importing the base class Person from the package persons, file name person
# Sub Class or derived class called employee and inheritance from Person in brackets
# encapsulated the attributes and behaviour related to the data type employee


class Employee(Person):
    # public variable
    company_name = None

    # constructor - attributes include those inherited from Person base class
    def __init__(self, firstname, lastname, age, email, telephone, department, job, wage, contract):
        super().__init__(firstname, lastname, age, email, telephone)
        self.department = department
        self.job = job
        self.__wage = wage
        self.contract = contract
        self.__new_wage = None
        # uses the composition class created of address
        # empty attribute but will be instantiated under the address class
        self.address = None

    # property - using decorator.
    # method is run to get the value
    @property
    def new_department(self):
        return self.department

    # method is run to change the value
    @new_department.setter
    def new_department(self, department):
        self.department = department

    @property
    def new_job(self):
        return self.job

    @new_job.setter
    def new_job(self, job):
        self.job = job

    @property
    def new_wage(self):
        return self.__wage

    @new_wage.setter
    def new_wage(self, wage):
        self.__wage = wage

    @property
    def new_contract(self):
        return self.contract

    @new_contract.setter
    def new_contract(self, contract):
        self.contract = contract

    # method to establish the employees status within the company
    def employee_status(self):
        if self.contract == 'Full time' or self.contract == 'Part time':
            return 'Employed'
        else:
            return "You don't work here"

    # method to create employees salary
    def promotion_salary(self):
        self.__new_wage = self.__wage + 500
        return f'Your new wage is {self.__new_wage}!'

    # using the built in function from base class Object - overrides the base class function
    def __str__(self):
        return f"\nEmployee\nFull name: {self.full_name}\nDepartment: {self.department}\nJob: {self.job} \nContract: {self.contract}\n********************"

    # class method can be used on the class directly
    # cls refers to the class itself
    # this gets the company name - public variable shared among all objects of the class
    # set = changes the name of the company to the new name
    @classmethod
    def get_company_name(cls):
        return cls.company_name


    @classmethod
    def set_company_name(cls, name):
        cls.company_name = name