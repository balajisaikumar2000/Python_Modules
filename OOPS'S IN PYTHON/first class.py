
class Employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):                               #here self must and should
        return "{} {}".format(self.first,self.last)


#these were instances of Employee class
emp_1 = Employee("Balaji","Sai Kumar",50000)
emp_2 = Employee("Test","User",60000)

#these were two different objects created with same class
#print(emp_1)
#print(emp_2)

#this should be read by passing "Pass" to the class without passing __init__method
#this is not suggested method ,becuase if there is a large data to be updated we don't want to put it manuallly
"""
emp_1.first = "Balaji"
emp_1.last = "Sai Kumar"
emp_1.email = "balaji.saikumar3@company.com"
emp_1.pay = 50000

emp_2.first = "Test"
emp_2.last = "User"
emp_2.email = "Test.User@company.com"
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)                     """

#we have to this manually for evary employee,better way to do this is keep it in  class ,and call that method
"""  print("{} {}".format(emp_1.first,emp_1.last))    """

print(emp_1.email)
print(emp_2.email)

print(emp_2.fullname)
print(emp_2.fullname())   #this method so () must

print(Employee.fullname(emp_2))          #this is same as this print(emp_2.fullname()) ,but we are passing instanece as self here on class on method






