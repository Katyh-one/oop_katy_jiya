from persons.employee import Employee
from persons.address import Address

worker1 = Employee('Matt', 'Smith', 40,  'mattsmith@hot.com', '07111111111', 'Doctor Who', 'In charge of everything', 10000, 'Full time')
worker2 = Employee('Taylor', 'Swift', 34, '1989@gmail.com', '87534666227', 'Tortured Poets', 'Lyricist', 5555555, 'Full time')
# print(worker1.employee_status())
worker2_address = Address('First line','Leeds', 'West yorkshire', 'LS2 34G')
worker1.new_job = 'Handy Man'
# print(worker1.job)

worker1.new_contract = 'Left'
# print(worker1.employee_status())

# print(worker2.promotion_salary())

# using the class method to set the new company name
Employee.set_company_name('Holy Global Enterprise inc')
print(f'Employees work for {Employee.get_company_name()}')

print(f'{worker1}\n{worker1.employee_status()}')
print(f'{worker2}\n{worker2_address}\n{worker2.employee_status()}\n{worker2.promotion_salary()}')