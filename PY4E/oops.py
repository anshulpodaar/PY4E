###   Python Object-Oriented Programming

class Employee:
#    pass

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)      ##    Initializing
emp_2 = Employee('Test', 'User', 60000)

#print(emp_1)        ##   Instances within the class Employee
#print(emp_2)

'''
emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'User'
emp_2.last = 'Test'
emp_2.email = 'User.Test@company.com'
emp_2.pay = 60000
'''

print(emp_1.first, emp_1.last, emp_1.email, emp_1.pay)
print(emp_2.first, emp_2.last, emp_2.email, emp_2.pay)

print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.fullname())
print(emp_2.fullname())

print(emp_1.fullname())
print(Employee.fullname(emp_1))